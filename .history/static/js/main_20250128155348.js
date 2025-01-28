// main.js
document.addEventListener('DOMContentLoaded', function() {
    const readMoreLinks = document.querySelectorAll('.read-more');
    
    readMoreLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            const contentFull = this.parentElement.querySelector('.content-full');
            contentFull.style.display = (contentFull.style.display === 'none') ? 'block' : 'none';
        });
    });
});
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
