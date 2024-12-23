
# Food Recognition and Calorie Estimation using AI and Image Processing

## Abstract
This project explores the integration of artificial intelligence (AI) and image processing to automatically recognize food items and estimate their calorie content. Using deep learning techniques, specifically convolutional neural networks (CNNs), the system classifies food items based on images and estimates their calories by referencing a nutritional database. This tool can assist users in tracking their food intake, thereby promoting healthier lifestyle choices.

## Description
This system employs AI and image processing to detect food items from images and provide accurate calorie estimates. By leveraging convolutional neural networks (CNNs) for image classification and a nutritional database to calculate calorie values, the project aims to offer a seamless way for users to track their daily food intake. The system also estimates portion sizes based on image scaling, ensuring more accurate calorie computations.

## Features
- **Automated Food Recognition:** Recognizes food items from uploaded images.
- **Calorie Estimation:** Estimates calorie content based on recognized food items and portion sizes.
- **Wide Food Categorization:** Supports various food categories such as fruits, vegetables, fast food, etc.
- **Nutritional Database Integration:** Uses a database to calculate calorie values.
- **Real-Time Recognition:** Allows food detection via camera feed.
- **User Interface:** Upload images and display results with an intuitive interface.
- **Portion Size Estimation:** Adjusts calorie estimates according to portion size.
- **Mobile Extension:** Potential to extend the system to mobile apps for calorie tracking on-the-go.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Gopi-githubb/Food-Recogintion-and-Calorie-Estimation.git
2.	Navigate to the project directory:
   cd Food-Recogintion-and-Calorie-Estimation  	
4.	Install the required dependencies:
   pip install -r requirements.txt

## Requirements
- Python 3.x
- Flask
- TensorFlow 2.x
- OpenCV
- NumPy
- Pillow
- Pandas
- Matplotlib
- scikit-learn

## Usage
Once the dependencies are installed, you can run the project as follows:
1.	To recognize food from an image:
   python food_recognition.py --image path_to_image
2.	To estimate calories from the recognized food:
   python calorie_estimation.py --image path_to_image

## Dataset
This project uses the Food-101 dataset which contains 101 categories of food with 1000 images per category. Preprocessing includes resizing images to 224x224 pixels and augmenting them for better model generalization.

## Model Training..
The food recognition model is based on the ResNet-50 architecture, trained on the Food-101 dataset with the following settings:
-	Learning rate: 0.001
-	Batch size: 32
-	Epochs: 25

## Results..
The model achieved an accuracy of 85% on the test dataset. Example of an input and output:
-	Input: Image of a pizza
-	Output: Pizza, 285 calories per slice

## Contributing
If you’d like to contribute to this project, feel free to fork the repository and submit a pull request with a detailed description of your changes.

## License 
This project is licensed under the MIT License.  See the LICENSE file for more details.

## Contact Information

**Maintainers**:  
- [GopiChand](https://github.com/Gopi-githubb)  
- [Sujal](https://github.com/Sujal-Bangari)  
- [Mahathi] 
- [Pranab]

This project is a collaborative effort by students at **Sreyas Institute of Engineering and Technology**. For more information about the college, visit [Sreyas Institute of Engineering and Technology](https://sreyas.ac.in/). 

Feel free to reach out to us through the GitHub links above for any questions or contributions.

---

