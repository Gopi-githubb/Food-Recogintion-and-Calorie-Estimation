from tensorflow.keras.applications import VGG16

# Load the VGG16 model pre-trained on ImageNet
model = VGG16(weights='imagenet')

# Save the model as a .h5 file
model.save('model/food_recognition_model.keras')# Adjust path as needed
