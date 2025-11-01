//carousel
document.addEventListener('DOMContentLoaded', function() {
        const items = document.querySelectorAll('.carousel-item');
        const dots = document.querySelectorAll('.carousel-dot');
        let currentIndex = 0;

        function showSlide(n) {
            items.forEach(item => item.classList.remove('active'));
            dots.forEach(dot => {
                dot.classList.remove('bg-gray-600', 'border-gray-600');
                dot.classList.add('bg-white', 'border-gray-400');
            });
            
            items[n].classList.add('active');
            dots[n].classList.remove('bg-white', 'border-gray-400');
            dots[n].classList.add('bg-gray-600', 'border-gray-600');
        }

        document.getElementById('carousel-prev').addEventListener('click', function() {
            currentIndex = (currentIndex - 1 + items.length) % items.length;
            showSlide(currentIndex);
        });

        document.getElementById('carousel-next').addEventListener('click', function() {
            currentIndex = (currentIndex + 1) % items.length;
            showSlide(currentIndex);
        });

        dots.forEach(dot => {
            dot.addEventListener('click', function() {
                currentIndex = parseInt(this.getAttribute('data-index'));
                showSlide(currentIndex);
            });
        });
    });


//コンタンツswitch toggle
//  function switchTab(tabIndex) {
//     const tabs = document.querySelectorAll('.tab');
//     const contents = document.querySelectorAll('.tab-content');
    
//     tabs.forEach((tab, index) => {
//         tab.classList.toggle('active', index === tabIndex);
//     });
    
//     contents.forEach((content, index) => {
//         content.classList.toggle('active', index === tabIndex);
//     });
// }

function switchTab(tabIndex) {
    const tabs = document.querySelectorAll('.tab');
    const contents = document.querySelectorAll('.tab-content');
    const activeTabInput = document.getElementById('active_tab');
    
    tabs.forEach((tab, index) => {
        tab.classList.toggle('active', index === tabIndex);
    });
    contents.forEach((content, index) => {
        content.classList.toggle('active', index === tabIndex);
    });
    
    // 根據 tabIndex 設定目前 active tab 名稱
    activeTabInput.value = (tabIndex === 0) ? 'tops' : 'bottoms';
}