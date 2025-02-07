document.addEventListener('DOMContentLoaded', function() {
    console.log('JavaScript is working!');

    // Add zoom effect on image click
    const images = document.querySelectorAll('img');
    images.forEach(image => {
        image.addEventListener('click', function() {
            window.location.href = this.dataset.url;
        });
    });
});