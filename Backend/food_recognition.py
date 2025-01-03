import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions

def load_model():
    """
    Load the pre-trained VGG16 model. This can be loaded once and reused for faster inference.
    """
    try:
        model = VGG16(weights='imagenet')  # Load pre-trained VGG16 model with ImageNet weights
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise

# Initialize the model globally (only once)
model = load_model()

def recognize_food(image_path):
    """
    Recognizes the food in the given image using the VGG16 model.

    Parameters:
    - image_path (str): The file path to the image to be recognized.

    Returns:
    - tuple: (food_item, confidence) where:
        - food_item (str): The name of the food item recognized.
        - confidence (float): The confidence level of the prediction.
    """
    try:
        # Load and preprocess the image
        img = image.load_img(image_path, target_size=(224, 224))  # VGG16 requires 224x224 images
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = preprocess_input(img_array)  # Preprocessing for VGG16 model

        # Predict the food class
        predictions = model.predict(img_array)

        # Decode predictions to readable format
        decoded_predictions = decode_predictions(predictions, top=3)[0]  # Get top 3 predictions

        # Get the top prediction (food item and confidence score)
        food_item = decoded_predictions[0][1]  # Food label
        confidence = decoded_predictions[0][2]  # Confidence score

        return food_item, confidence

    except Exception as e:
        print(f"Error during food recognition: {e}")
        return 'Unknown', 0.0
