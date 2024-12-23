# Food Recognition and Calorie Estimation using AI and Image Processing

## Abstract
This project explores the integration of artificial intelligence (AI) and image processing to automatically recognize food items and estimate their calorie content. Using deep learning techniques, specifically convolutional neural networks (CNNs), the system classifies food items based on images and estimates their calories by referencing a nutritional database. In addition to food recognition and calorie estimation, the system offers dietary suggestions and enables users to track their food intake, thereby promoting healthier lifestyle choices.

## Description
This system employs AI and image processing to detect food items from images and provide accurate calorie estimates. By leveraging convolutional neural networks (CNNs) for image classification and a nutritional database to calculate calorie values, the project aims to offer a seamless way for users to track their daily food intake. The system also estimates portion sizes based on image scaling, ensuring more accurate calorie computations.

Additionally, the webpage will provide services such as personalized dietary plans based on the user's food intake and health goals, and it will allow users to track their daily progress. The platform will enable users to maintain a healthier lifestyle by making informed food choices and monitoring their nutrition.

## SERVICES
The following services are provided through the webpage:

- **Automated Food Recognition:** The system recognizes food items from uploaded images using AI-powered image processing.
- **Calorie Estimation:** After identifying the food, the system estimates the calorie content based on recognized food items and portion sizes.
- **Dietary Suggestions:** Personalized dietary plans are generated for users based on their health goals, preferences, and food intake.
- **Food Intake Tracking:** Users can log their daily food intake and track their calorie consumption, helping them stay on top of their nutrition goals.
- **Real-Time Recognition:** The platform allows users to use a camera feed for real-time food recognition.
- **Wide Food Categorization:** Supports various food categories, including fruits, vegetables, fast food, and more.
- **Portion Size Estimation:** The system adjusts calorie estimates according to portion size, estimated via image scaling.
- **Mobile Extension:** The platform has the potential to be extended to mobile applications for on-the-go food recognition and calorie tracking.

## Features
- **Nutritional Database Integration:** Utilizes a comprehensive nutritional database to calculate accurate calorie values for recognized food items.
- **User Interface:** Provides a user-friendly interface for uploading images and displaying recognition results.
- **Web-Based Platform:** The service is available on a webpage, where users can interact with the system, track their food intake, and receive personalized dietary suggestions.

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

## Model Performance
- Accuracy: 85% on the test dataset
## Example Input and Output:
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

