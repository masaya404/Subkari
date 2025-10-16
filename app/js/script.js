let currentSlide = 0;
const slides = document.querySelectorAll('.hero-slide-item');
const totalSlides = slides.length;
const slideContainer = document.querySelector('.hero-slide');

function showSlide(index) {
  const slideWidth = 100 / 4; // 1スライドあたり幅（4枚並べ）
  slideContainer.style.transition = 'transform 0.8s ease';
  slideContainer.style.transform = `translateX(-${index * slideWidth}%)`;
}

function nextSlide() {
  currentSlide++;
  if (currentSlide > totalSlides - 4) { // 4枚表示なので最後から戻す
    currentSlide = 0;
  }
  showSlide(currentSlide);
}

function previousSlide() {
  currentSlide--;
  if (currentSlide < 0) {
    currentSlide = totalSlides - 4;
  }
  showSlide(currentSlide);
}

// 自動スライド
let autoSlide = setInterval(nextSlide, 4000);

// マウスで一時停止
const hero = document.querySelector('.hero');
hero.addEventListener('mouseenter', () => clearInterval(autoSlide));
hero.addEventListener('mouseleave', () => {
  autoSlide = setInterval(nextSlide, 4000);
});
