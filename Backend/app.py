from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from food_recognition import recognize_food  # Make sure this file exists
from calorie_estimation import estimate_calories  # Make sure this file exists
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask app and configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Initialize the database and login manager
# Initialize the database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User model for handling logins
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(100), nullable=False)

# Define the user loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Load pre-trained VGG16 model for food recognition
model = tf.keras.applications.VGG16(weights='imagenet')

# Define the user loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes for the app
@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
@login_required
def upload():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    # Save the uploaded image
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Make sure the uploads directory exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    file.save(filepath)

    # Predict food item and calculate calories
    try:
        food_item, confidence = recognize_food(filepath, model)
        calories_per_100g, total_calories = estimate_calories(food_item)

        # Check if the recognized food item exists in the predefined calorie list
        if calories_per_100g == 0:
            return jsonify({
                'message': "We couldn't recognize the food item. Please upload the image with the food name included."
            }), 400

        # Respond with food item and calorie information
        return jsonify({
            'food_item': food_item,
            'confidence': confidence,
            'calories_per_100g': calories_per_100g,
            'total_calories': total_calories
        })
    except Exception as e:
        return jsonify({"message": "Failed to recognize the food item. Please upload the image with a name."}), 400

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        return 'Invalid credentials!'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Hash the password before storing
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['newPassword']
        confirm_password = request.form['confirmPassword']

        if new_password != confirm_password:
            return 'Passwords do not match!'

        user = User.query.filter_by(email=username).first()
        if user:
            # Hash the new password
            hashed_password = generate_password_hash(new_password, method='sha256')
            user.password = hashed_password
            db.session.commit()
            return redirect(url_for('login'))
        return 'Username not found!'

    return render_template('forgot.html')

# Create the database tables manually (with application context)
def create_tables():
    with app.app_context():
        db.create_all()

# Initialize the database (run once)
create_tables()

if __name__ == '__main__':
    app.run(debug=True)
