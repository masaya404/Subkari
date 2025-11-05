//Timer
function startTimer() {
    let hours = 12, minutes = 59, seconds = 59;
    const timerEl = document.getElementById('timer');

    setInterval(() => {
        if (seconds > 0) {
            seconds--;
        } else if (minutes > 0) {
            minutes--;
            seconds = 59;
        } else if (hours > 0) {
            hours--;
            minutes = 59;
            seconds = 59;
        }

        const h = String(hours).padStart(2, '0');
        const m = String(minutes).padStart(2, '0');
        const s = String(seconds).padStart(2, '0');
        timerEl.textContent = `${h}:${m}:${s}`;
    }, 1000);
}

startTimer();

//コンタンツswitch toggle
 function switchTab(tabIndex) {
    const tabs = document.querySelectorAll('.tab');
    const contents = document.querySelectorAll('.tab-content');
    
    tabs.forEach((tab, index) => {
        tab.classList.toggle('active', index === tabIndex);
    });
    
    contents.forEach((content, index) => {
        content.classList.toggle('active', index === tabIndex);
    });
}

//right area
document.querySelectorAll('.product-item').forEach(item => {
  item.addEventListener('click', function() {
    // Remove highlight from all items
    document.querySelectorAll('.product-item').forEach(el => {
      el.classList.remove('bg-blue-50', 'border-blue-400');
    });
    
    // Add highlight to clicked item
    this.classList.add('bg-blue-50', 'border-blue-400');
    
    // Get product data
    const productData = JSON.parse(this.dataset.product);
    
    // Update right area with product details
    // document.getElementById('detailProductName').textContent = productData.name || '商品名なし';
    document.getElementById('detailProductExplanation').textContent = productData.explanation || '説明文なし';
    
    // document.getElementById('detailProductSituation').textContent = productData.situation || '-';
    // document.getElementById('detailProductStatus').textContent = productData.status || '-';
    
    // Update image if available
    if (productData.img) {
      const basePath = "{{url_for('static',filename='img/productImg')}}";
      document.getElementById('detailProductImg').src = basePath + productData.img;
    }
  });
});

// Auto-select first product on load
window.addEventListener('DOMContentLoaded', function() {
  const firstProduct = document.querySelector('.product-item');
  if (firstProduct) {
    firstProduct.click();
  }
});
