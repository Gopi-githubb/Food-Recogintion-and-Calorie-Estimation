from tensorflow.keras.applications import VGG16
import os

# Path where you want to save the model (Backend/model)
MODEL_SAVE_PATH = 'C:/Users/gopic/PROJECT/Backend/model/vgg16_pretrained.keras'

def load_and_save_vgg16_model():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)

    # Load the VGG16 model with ImageNet weights
    model = VGG16(weights='imagenet')

    # Save the model to the specified path
    model.save(MODEL_SAVE_PATH)

    print(f"Model saved to {MODEL_SAVE_PATH}")
    return model

# Call this function to load and save the model
if __name__ == "__main__":
    load_and_save_vgg16_model()
