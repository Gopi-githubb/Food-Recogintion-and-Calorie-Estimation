// Trigger file input on click
function triggerFileInput() {
    document.getElementById('file-input').click(); // Simulate click on hidden input element
}

// Validate file type and size before uploading
function validateFile(file) {
    const allowedTypes = ['image/jpeg', 'image/png', 'image/jpg'];
    const maxSize = 5 * 1024 * 1024; // 5MB

    if (!allowedTypes.includes(file.type)) {
        alert('Only JPEG, PNG, or JPG images are allowed.');
        return false;
    }
    if (file.size > maxSize) {
        alert('File size should not exceed 5MB.');
        return false;
    }
    return true;
}

async function uploadAndProcessImage(event) {
    const file = event.target.files[0]; // Get the uploaded file
    if (!file) {
        alert('Please select an image to upload.');
        return; // Exit if no file is selected
    }

    // Validate file type and size
    if (!validateFile(file)) return;

    const formData = new FormData();
    formData.append("file", file); // Append file to form data

    // Show uploading status
    const uploadMessageElement = document.getElementById('upload-message');
    uploadMessageElement.style.display = 'block';
    uploadMessageElement.textContent = 'Uploading...';

    // Clear previous results
    clearPreviousResults();

    try {
        // Send the image to the backend for processing
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        // Check if response is OK, else handle error
        if (!response.ok) {
            throw new Error('Error uploading image.');
        }

        const data = await response.json(); // Expect JSON response

        // Handle the response and show results
        if (data.message) {
            uploadMessageElement.textContent = data.message;
        }

        // Display the uploaded image and its name
        if (data.image_url) {
            document.getElementById('uploaded-image').src = data.image_url;
            document.getElementById('image-name').textContent = file.name;
            document.getElementById('image-info').style.display = 'block';  // Show image section
        }

        // Display food item and calorie details
        if (data.food_item && data.calories_per_100g && data.total_calories) {
            document.getElementById('food-name').textContent = data.food_item;
            document.getElementById('calories-per-100g').textContent = data.calories_per_100g;
            document.getElementById('total-calories').textContent = data.total_calories;
            document.getElementById('result').style.display = 'block';  // Show result section
        } else {
            // Handle case where food recognition didn't return valid data
            uploadMessageElement.textContent = 'Could not recognize the food or calculate calories. Please try again.';
        }

        // Show the submit button after successful upload
        document.getElementById('submit-container').style.display = 'block';

    } catch (error) {
        uploadMessageElement.textContent = 'Error uploading image.';
        console.error('Error:', error);

        // Provide more specific feedback for different types of errors
        if (error.message.includes('NetworkError')) {
            alert('Network error! Please check your connection.');
        } else {
            alert('An unexpected error occurred. Please try again.');
        }
    } finally {
        // Hide the uploading message after processing
        setTimeout(() => {
            uploadMessageElement.style.display = 'none';
        }, 3000); // Hide after 3 seconds
    }
}

// Clear previous results from previous image uploads
function clearPreviousResults() {
    // Hide previously displayed image and results
    document.getElementById('uploaded-image').src = '';
    document.getElementById('image-name').textContent = '';
    document.getElementById('image-info').style.display = 'none';
    document.getElementById('food-name').textContent = '';
    document.getElementById('calories-per-100g').textContent = '';
    document.getElementById('total-calories').textContent = '';
    document.getElementById('result').style.display = 'none';
}

// Submit the image for further analysis or processing
function submitImageForAnalysis() {
    alert("Image submitted for further analysis!");
    // You can add additional logic to handle any further actions required after submission
}



// // Trigger file input on click
// function triggerFileInput() {
//     document.getElementById('file-input').click(); // Simulate click on hidden input element
// }

// // Validate file type and size before uploading
// function validateFile(file) {
//     const allowedTypes = ['image/jpeg', 'image/png', 'image/jpg'];
//     const maxSize = 5 * 1024 * 1024; // 5MB

//     if (!allowedTypes.includes(file.type)) {
//         alert('Only JPEG, PNG, or JPG images are allowed.');
//         return false;
//     }
//     if (file.size > maxSize) {
//         alert('File size should not exceed 5MB.');
//         return false;
//     }
//     return true;
// }

// async function uploadAndProcessImage(event) {
//     const file = event.target.files[0]; // Get the uploaded file
//     if (!file) {
//         alert('Please select an image to upload.');
//         return; // Exit if no file is selected
//     }

//     // Validate file type and size
//     if (!validateFile(file)) return;

//     const formData = new FormData();
//     formData.append("file", file); // Append file to form data

//     // Show uploading status
//     const uploadMessageElement = document.getElementById('upload-message');
//     uploadMessageElement.style.display = 'block';
//     uploadMessageElement.textContent = 'Uploading...';

//     // Clear previous results
//     clearPreviousResults();

//     try {
//         // Send the image to the backend for processing
//         const response = await fetch('/upload', {
//             method: 'POST',
//             body: formData
//         });

//         // Check if response is OK, else handle error
//         if (!response.ok) {
//             throw new Error('Error uploading image.');
//         }

//         const data = await response.json(); // Expect JSON response

//         // Handle the response and show results
//         if (data.message) {
//             uploadMessageElement.textContent = data.message;
//         }

//         // Display the uploaded image and its name
//         if (data.image_url) {
//             document.getElementById('uploaded-image').src = data.image_url;
//             document.getElementById('image-name').textContent = file.name;
//             document.getElementById('image-info').style.display = 'block';  // Show image section
//         }

//         // Display food item and calorie details
//         if (data.food_item && data.calories_per_100g && data.total_calories) {
//             document.getElementById('food-name').textContent = data.food_item;
//             document.getElementById('calories-per-100g').textContent = data.calories_per_100g;
//             document.getElementById('total-calories').textContent = data.total_calories;
//             document.getElementById('result').style.display = 'block';  // Show result section
//         } else {
//             // Handle case where food recognition didn't return valid data
//             uploadMessageElement.textContent = 'Could not recognize the food or calculate calories. Please try again.';
//         }
//     } catch (error) {
//         uploadMessageElement.textContent = 'Error uploading image.';
//         console.error('Error:', error);

//         // Provide more specific feedback for different types of errors
//         if (error.message.includes('NetworkError')) {
//             alert('Network error! Please check your connection.');
//         } else {
//             alert('An unexpected error occurred. Please try again.');
//         }
//     } finally {
//         // Hide the uploading message after processing
//         setTimeout(() => {
//             uploadMessageElement.style.display = 'none';
//         }, 3000); // Hide after 3 seconds
//     }
// }

// // Clear previous results from previous image uploads
// function clearPreviousResults() {
//     // Hide previously displayed image and results
//     document.getElementById('uploaded-image').src = '';
//     document.getElementById('image-name').textContent = '';
//     document.getElementById('image-info').style.display = 'none';
//     document.getElementById('food-name').textContent = '';
//     document.getElementById('calories-per-100g').textContent = '';
//     document.getElementById('total-calories').textContent = '';
//     document.getElementById('result').style.display = 'none';
// }
