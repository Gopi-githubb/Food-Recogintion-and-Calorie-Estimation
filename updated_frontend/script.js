async function uploadImage() {
    const input = document.getElementById('imageUpload');
    const file = input.files[0];
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('/predict', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        const result = await response.json();
        console.log(result);  // Debugging: Log the response to see its structure
        document.getElementById('result').innerText = `Food: ${result.food}, Calories: ${result.calories}`;
        document.getElementById('feedback').style.display = 'block';
    } else {
        const errorText = await response.text();
        document.getElementById('result').innerText = `Error: ${response.status} - ${errorText}`;
        document.getElementById('feedback').style.display = 'none';
    }
}

document.querySelector('button').onclick = uploadImage;

async function submitFeedback() {
    const correctFoodName = document.getElementById('correctFoodName').value;
    const response = await fetch('/feedback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ correctFoodName })
    });

    if (response.ok) {
        alert('Thank you for your feedback!');
        document.getElementById('feedback').style.display = 'none';
    } else {
        const errorText = await response.text();
        alert(`Error: ${response.status} - ${errorText}`);
    }
}

function previewImage() {
    const input = document.getElementById('imageUpload');
    const file = input.files[0];
    const reader = new FileReader();
    reader.onload = function (e) {
        const imagePreview = document.getElementById('imagePreview');
        imagePreview.src = e.target.result;
        document.getElementById('imagePreviewContainer').style.display = 'block';
    };
    reader.readAsDataURL(file);
}

const navMenu = document.getElementById('nav-menu');
const toggleMenu = document.getElementById('toggle-menu');
const closeMenu = document.getElementById('close-menu');
toggleMenu.addEventListener('click', ()=>{
    navMenu.classList.toggle('show');
});

closeMenu.addEventListener('click', ()=>{
    navMenu.classList.remove('show');
});