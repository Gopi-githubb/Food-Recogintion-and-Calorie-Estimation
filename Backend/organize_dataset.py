import os
import shutil
import random

# Set your source image folder
source_folder = "C:/Users/gopic/PROJECT/Backend/data/food-101/images/"
train_folder = "C:/Users/gopic/PROJECT/Backend/data/food-101/train/"
test_folder = "C:/Users/gopic/PROJECT/Backend/data/food-101/test/"

# Get list of all classes (subfolders in the source folder)
classes = os.listdir(source_folder)

# Split images into train and test for each class
for food_class in classes:
    # Only process if it's a directory (ignore files like .DS_Store)
    if os.path.isdir(os.path.join(source_folder, food_class)):
        # Create train/test subfolders
        os.makedirs(os.path.join(train_folder, food_class), exist_ok=True)
        os.makedirs(os.path.join(test_folder, food_class), exist_ok=True)

        # Get list of images for this class
        images = os.listdir(os.path.join(source_folder, food_class))

        # Shuffle the images
        random.shuffle(images)

        # Split into 80% train and 20% test
        train_size = int(0.8 * len(images))
        train_images = images[:train_size]
        test_images = images[train_size:]

        # Move files to the respective folders
        for img in train_images:
            shutil.move(os.path.join(source_folder, food_class, img),
                        os.path.join(train_folder, food_class, img))
        for img in test_images:
            shutil.move(os.path.join(source_folder, food_class, img),
                        os.path.join(test_folder, food_class, img))

print("Dataset organized into train and test folders.")
