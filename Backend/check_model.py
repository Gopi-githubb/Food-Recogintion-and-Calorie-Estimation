from tensorflow.keras.models import load_model

# Load your model (ensure the path to your .h5 file is correct)
MODEL_PATH = 'model/vgg16_pretrained.keras'  # Update this path to your model location

# Load the model
model = load_model(MODEL_PATH)

# Print model output shape
print("Model output shape:", model.output_shape)
