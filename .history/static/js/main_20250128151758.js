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
