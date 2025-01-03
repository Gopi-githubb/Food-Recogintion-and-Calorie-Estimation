import os
import uuid
import logging
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import tensorflow as tf
from food_recognition import recognize_food  # Ensure this file exists and contains the function
from calorie_estimation import estimate_calories  # Ensure this file exists and contains the function

# Initialize the Flask app and configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change to a secure key for production

# Corrected SQLite URI (absolute path) or use relative path as needed
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/gopic/PROJECT/Backend/users.db'  # Absolute path
# OR
# app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.root_path, 'users.db')}"  # Relative path

# Set up upload folder for file storage (Corrected the path here)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'Backend', 'Uploads')  # Correct path to 'Uploads' folder
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed file extensions
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Enable auto reloading of templates

# Ensure uploads directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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

# Load pre-trained model for food recognition (loaded once)
model_path = os.path.join(app.root_path, 'model', 'vgg16_pretrained.keras')  # Corrected model path

try:
    vgg16_model = tf.keras.models.load_model(model_path)
    logging.info(f"Model loaded successfully from {model_path}")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    raise e

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Routes for the app
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('Register/index.html')  # Correct path for dashboard

# Image Upload and Processing Route (No login required)
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    if not allowed_file(file.filename):
        return jsonify({"message": "File format not supported. Please upload a valid image."}), 400

    # Generate a unique filename
    filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Predict food item and calculate calories
    try:
        food_item, confidence = recognize_food(filepath, vgg16_model)

        if food_item == 'Unknown':
            return jsonify({"message": "Food item not recognized. Please upload a clearer image with food names included."}), 400

        # Estimate calories based on the recognized food item
        calories_per_100g, total_calories = estimate_calories(food_item)

        if calories_per_100g == 0 or total_calories == 0:
            return jsonify({
                'message': "We couldn't calculate the calories. Please upload a valid image."
            }), 400

        # Return the result as JSON response
        return jsonify({
            'food_item': food_item,
            'confidence': confidence,
            'calories_per_100g': calories_per_100g,
            'total_calories': total_calories,
            'image_url': f"/uploads/{filename}",  # Return image URL for display
            'message': f"Food detected: {food_item} with {confidence*100:.2f}% confidence. Estimated calories: {total_calories} kcal."
        })

    except Exception as e:
        logging.error(f"Error during food recognition: {str(e)}")
        return jsonify({"message": f"Failed to recognize the food item. Error: {str(e)}"}), 400

# Serve the uploaded images (for frontend display)
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid credentials!', 'danger')
    return render_template('Register/login.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email is already in use. Please choose another one.', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Registration successful!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('Register/register.html')

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Forgot Password Route
@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        username = request.form['username']
        new_password = request.form['newPassword']
        confirm_password = request.form['confirmPassword']

        if new_password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('forgot'))

        if not username or not new_password:
            flash('Please fill in all fields!', 'danger')
            return redirect(url_for('forgot'))

        user = User.query.filter_by(email=username).first()
        if user:
            hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256')
            user.password = hashed_password
            db.session.commit()
            flash('Password reset successful!', 'success')
            return redirect(url_for('login'))
        flash('Username not found!', 'danger')
        return redirect(url_for('forgot'))

    return render_template('Register/forgot.html')

# Initialize the database (run once)
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

if __name__ == '__main__':
    app.run(debug=True)
