document.addEventListener('DOMContentLoaded', function() {
    let slideIndex = 0;

    // Define the moveSlide function inside DOMContentLoaded event
    function moveSlide(step) {
        const slides = document.querySelectorAll('.post-slide');
        const totalSlides = slides.length;

        slideIndex += step;

        // Wrap around if we go past the first or last slide
        if (slideIndex < 0) {
            slideIndex = totalSlides - 1;
        } else if (slideIndex >= totalSlides) {
            slideIndex = 0;
        }

        const sliderContainer = document.querySelector('.slider-container');
        sliderContainer.style.transform = `translateX(-${slideIndex * 100}%)`;
    }

    // Attach moveSlide to button clicks
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');

    if (prevButton && nextButton) {
        prevButton.onclick = function() {
            moveSlide(-1);
        };

        nextButton.onclick = function() {
            moveSlide(1);
        };
    }

    // Optional: Auto slide (if you want it to auto-slide after a few seconds)
    setInterval(() => {
        moveSlide(1); // Move to the next slide automatically every 5 seconds
    }, 5000);
});
