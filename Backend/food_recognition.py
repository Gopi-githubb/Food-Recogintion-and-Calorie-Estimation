import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications.vgg16 import decode_predictions, preprocess_input

# Load pre-trained VGG16 model for food recognition
model = tf.keras.applications.VGG16(weights='imagenet')

def recognize_food(img_path, model):
    # Load the image file and resize it to 224x224 for VGG16
    img = image.load_img(img_path, target_size=(224, 224))

    # Convert image to numpy array and preprocess it for the model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make prediction using the VGG16 model
    preds = model.predict(img_array)

    # Decode the predictions and get the food item and confidence
    decoded_preds = decode_predictions(preds, top=1)[0]
    food_item = decoded_preds[0][1]
    confidence = decoded_preds[0][2]

    return food_item, confidence
