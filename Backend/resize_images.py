from PIL import Image
import os

# Set paths for train and test directories
train_dir = "C:/Users/gopic/PROJECT/Backend/data/food-101/train/"
test_dir = "C:/Users/gopic/PROJECT/Backend/data/food-101/test/"

# Resize images for each class in the train and test folders
def resize_images(directory):
    for class_folder in os.listdir(directory):
        class_folder_path = os.path.join(directory, class_folder)
        if os.path.isdir(class_folder_path):
            for img_name in os.listdir(class_folder_path):
                img_path = os.path.join(class_folder_path, img_name)
                try:
                    img = Image.open(img_path)
                    img = img.resize((224, 224))  # Resize to 224x224
                    img.save(img_path)
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")

# Resize images in both train and test directories
resize_images(train_dir)
resize_images(test_dir)

print("Images resized to 224x224.")
