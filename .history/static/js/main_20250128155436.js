// main.js

let slideIndex = 0;

function moveSlide(step) {
    const slides = document.querySelectorAll('.post-slide');
    const totalSlides = slides.length;
    
    slideIndex += step;

    if (slideIndex < 0) {
        slideIndex = totalSlides - 1;
    } else if (slideIndex >= totalSlides) {
        slideIndex = 0;
    }

    const sliderContainer = document.querySelector('.slider-container');
    sliderContainer.style.transform = `translateX(-${slideIndex * 100}%)`;
}
