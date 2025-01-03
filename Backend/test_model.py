import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import logging
from PIL import Image

# Constants for model and test image
MODEL_PATH = 'model/vgg16_pretrained.keras'  # Path to your trained model
TEST_IMAGE_PATH = 'Uploads/693210.jpg'  # Path to your test image

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the pre-trained VGG16 model
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    logging.info(f"Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    logging.error(f"Error loading model: {e}")
    raise e

# Function to preprocess the image for prediction
def preprocess_image(img_path):
    """
    Preprocess the image to fit the input requirements of the VGG16 model.

    Parameters:
    - img_path (str): Path to the image file.

    Returns:
    - img_array: Preprocessed image ready for prediction.
    """
    try:
        img = Image.open(img_path).resize((224, 224))  # Resize image to 224x224
        img_array = np.array(img) / 255.0  # Normalize pixel values to [0, 1]
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        return img_array
    except Exception as e:
        logging.error(f"Error preprocessing image: {e}")
        raise e

# Function to make prediction on the image
def predict_food(img_path):
    """
    Predict the food item from the image using the pre-trained model.

    Parameters:
    - img_path (str): Path to the image.

    Returns:
    - food_item: The predicted food item (class name).
    - confidence: The confidence of the prediction.
    """
    try:
        img_array = preprocess_image(img_path)
        predictions = model.predict(img_array)  # Model prediction

        # Get the predicted class and confidence
        predicted_class_idx = np.argmax(predictions, axis=1)[0]
        confidence = np.max(predictions, axis=1)[0]

        food_item = str(predicted_class_idx)  # Convert the predicted index to class name if you have a mapping
        return food_item, confidence
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        raise e

# Main function to run the test
if __name__ == '__main__':
    try:
        food_item, confidence = predict_food(TEST_IMAGE_PATH)
        logging.info(f"Predicted Food Item: {food_item}, Confidence: {confidence*100:.2f}%")
    except Exception as e:
        logging.error(f"Test failed: {e}")
