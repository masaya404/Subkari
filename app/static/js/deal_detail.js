document.addEventListener('DOMContentLoaded', function() {
        const statusButton = document.getElementById("status");
        const status = statusButton.textContent.trim();
        updateTimeline(status);
        loadComments();
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

// function comment(){
//     const commentText = document.querySelector('textarea[name="comment"]').value;
//     const transactionId = document.querySelector('input[name="transactionID"]').value;  // 
//     const productId = document.querySelector('input[name="productID"]').value;;  // 
    
//     if (!commentText.trim()) {
//         return;
//     }
    
//     const formData = new FormData();
//     formData.append('comment', commentText);
//     formData.append('transaction_id', transactionId);
//     formData.append('product_id', productId);
    
//     fetch('/deal/comment', {
//         method: 'POST',
//         body: formData
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             alert('メッセージを送信しました');
//             // clear
//             document.querySelector('textarea[name="comment"]').value = '';
        
//             // window.location.reload();
//         } else {
//             alert('失敗: ' + data.message);
//         }
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         alert('エラーが発生しました');
//     });

// }

 // /////////////////////// load comments //////////////////////////////
    function loadComments() {
        // const transactionID = document.getElementById('transactionID').value;
        const productID = document.getElementById('productID').value;
        fetch(`/deal/get-comments?product_id=${productID}`)
            .then(response => response.json())
            .then(data => {
                console.log('Comments loaded:', data);
                renderComments(data);
            })
            .catch(error => console.error('Error loading comments:', error));
    }

    // render comments to page
    function renderComments(comments) {
        const container = document.getElementById('commentsContainer');
        const account = 
        container.innerHTML = comments.map(comment => `
            <div class="border rounded-xs p-6 mb-6">
                <p class="font-semibold">${comment.firstName}</p>
                <p class="text-gray-700 mt-2">${comment.content}</p>
                <p class="text-gray-400 text-sm mt-2">${new Date(comment.createdDate).toLocaleString('ja-JP')}</p>
            </div>
        `).join('');
    }

    // 新しい comment　提出
    function submitComment() {
        const productID = document.getElementById('productID').value;
        const content = document.getElementById('commentInput').value.trim();

        if (!content) {
            return;
        }

        // バックエンドに送る
        fetch('/deal/add-comment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                product_id: productID,
                content: content
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Comment added:', data);
                
                // clear 
                document.getElementById('commentInput').value = '';
                
                //  comments reload
                loadComments();
                
                alert('メッセージを送信しました');
            } else {
                alert('エラー: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('送信に失敗しました');
        });
    }