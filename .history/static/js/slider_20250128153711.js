let currentSlide = 0;

function moveSlide(step) {
    const slides = document.querySelectorAll('.post-slide');
    const totalSlides = slides.length;
    currentSlide += step;

    if (currentSlide < 0) {
        currentSlide = totalSlides - 1;
    } else if (currentSlide >= totalSlides) {
        currentSlide = 0;
    }

    const sliderContainer = document.querySelector('.slider-container');
    sliderContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
}

// Optionally, you can add automatic sliding:
setInterval(function() {
    moveSlide(1);
}, 5000);  // Moves every 5 seconds
