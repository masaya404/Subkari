let currentSlide = 0;

function nextSlide() {
    const slider = document.getElementById('heroSlider');
    currentSlide = (currentSlide + 1) % 2;
    slider.style.transform = `translateX(-${currentSlide * 100}%)`;
}

function previousSlide() {
    const slider = document.getElementById('heroSlider');
    currentSlide = (currentSlide - 1 + 2) % 2;
    slider.style.transform = `translateX(-${currentSlide * 100}%)`;
}

// Auto slide every 5 seconds
setInterval(nextSlide, 5000);
