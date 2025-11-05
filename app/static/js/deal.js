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
    updateTimeline(productData.status);

    const transactionId = productData.transaction_id || productData.id;
    document.getElementById('detailTransactionId').textContent = transactionId;

    const dealDetailUrl = `/deal/deal/${transactionId}`;
    document.getElementById('dealDetailLink').href = dealDetailUrl;
  });
});

// Auto-select first product on load
window.addEventListener('DOMContentLoaded', function() {
  const firstProduct = document.querySelector('.product-item');
  if (firstProduct) {
    firstProduct.click();
  }
});

//medium area
const statusMap = {
  '支払い待ち': 1,
  '発送待ち': 2,
  '配送中': 3,
  '到着': 4,
  'レンタル中': 5,
  'クリーニング期間': 6,
  '発送待ち': 7,
  '取引完了': 8
};

function updateTimeline(status) {
  const step = statusMap[status] || 0;
  
  // Update all timeline items
  for (let i = 1; i <= 8; i++) {
    const circles = document.querySelectorAll(`.timeline-item-${i} .timeline-circle`);
    
    if (i < step) {
      // Completed steps - show checkmark
      circles.forEach(circle => {
        circle.classList.remove('bg-white', 'border-2', 'border-gray-400', 'text-gray-600');
        circle.classList.add('bg-gray-800', 'text-white');
        circle.innerHTML = '✓';
      });
    } else if (i === step) {
      // Current step - show number with highlight
      circles.forEach(circle => {
        circle.classList.remove('bg-white', 'border-2', 'border-gray-400', 'text-gray-600');
        circle.classList.add('bg-gray-800', 'text-white');
        circle.innerHTML = i;
      });
    } else {
      // Future steps - show number
      circles.forEach(circle => {
        circle.classList.remove('bg-gray-800', 'text-white');
        circle.classList.add('bg-white', 'border-2', 'border-gray-400', 'text-gray-600');
        circle.innerHTML = i;
      });
    }
  }
}
