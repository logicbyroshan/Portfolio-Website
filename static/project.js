const sliderWrapper = document.querySelector('.project-slider-wrapper');
const prevBtn = document.querySelector('.project-prev-btn');
const nextBtn = document.querySelector('.project-next-btn');

let currentIndex = 0;
const images = document.querySelectorAll('.project-slider-wrapper img');
const totalImages = images.length;

function updateSlider() {
    sliderWrapper.style.transform = `translateX(-${currentIndex * 1280}px)`;
}

prevBtn.addEventListener('click', () => {
    currentIndex = (currentIndex > 0) ? currentIndex - 1 : totalImages - 1;
    updateSlider();
});

nextBtn.addEventListener('click', () => {
    currentIndex = (currentIndex < totalImages - 1) ? currentIndex + 1 : 0;
    updateSlider();
});
