document.addEventListener('DOMContentLoaded', function() {
            loadUploadedImages();
        });

        function loadUploadedImages() {
            try {
                const images = JSON.parse(sessionStorage.getItem('uploadedImages'));
                
                if (images && images.length > 0) {
                    // 最新画像
                    const latestImage = images[0];
                    const displayImage = document.getElementById('displayImage');
                    const imageDataInput = document.getElementById('imageDataInput');
                    
                    displayImage.src = latestImage.src;
                    imageDataInput.value = latestImage.src;
                    
                    // 画像表示エリア　
                    document.getElementById('imageDisplayArea').classList.remove('hidden');
                    document.getElementById('noImageArea').classList.add('hidden');
                    
                    console.log('イメージローディング');
                } else {
                    
                    document.getElementById('imageDisplayArea').classList.add('hidden');
                    document.getElementById('noImageArea').classList.remove('hidden');
                    console.log('画像がない');
                }
            } catch (e) {
                console.error('失敗:', e);
                document.getElementById('imageDisplayArea').classList.add('hidden');
                document.getElementById('noImageArea').classList.remove('hidden');
            }
        }

        function goToUploadPage() {
            // 點擊圖片進入編輯頁面
            window.location.href = "{{url_for('seller.seller_uploadImg')}}";
        }
// 価格トグル
const rentalCheckbox = document.querySelector('.rentalCheckbox');
const purchaseCheckbox = document.querySelector('.purchaseCheckbox');
const rentalPriceSection = document.getElementById('rentalPriceSection');
const purchasePriceSection = document.getElementById('purchasePriceSection');
const rentalPrice = document.getElementById('rentalPrice');
const purchasePrice = document.getElementById('purchasePrice');
const rentalPurchaseError = document.getElementById('rentalPurchaseError');

// レンタル可能チェックボックス
rentalCheckbox.addEventListener('change', function() {
    const existingSection = document.getElementById('rentalPriceSection');
    
    if (this.checked) {
        // 存在しない場合のみ作成
        if (!existingSection) {
            createRentalPriceSection();
        }
    } else {
        // 削除
        if (existingSection) {
            existingSection.remove();
        }
    }
    validateSelection();
});

// 購入可能チェックボックス
purchaseCheckbox.addEventListener('change', function() {
    const existingSection = document.getElementById('purchasePriceSection');
    
    if (this.checked) {
        // 存在しない場合のみ作成
        if (!existingSection) {
            createPurchasePriceSection();
        }
    } else {
        // 削除
        if (existingSection) {
            existingSection.remove();
        }
    }
    validateSelection();
});

// レンタル価格セクション作成
function createRentalPriceSection() {
    const newSection = document.createElement('div');
    newSection.id = 'rentalPriceSection';
    newSection.className = 'flex flex-col gap-2';
    newSection.innerHTML = `
        <div class="price-input-wrapper">
        <input type="number" id="rentalPrice" name="rentalPrice" placeholder="0" min="0" class="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500">
        </div>
        `;
    
    const rentalLabel = rentalCheckbox.closest('label');
    rentalLabel.after(newSection);
    
    document.getElementById('rentalPrice').focus();
}

// 購入価格セクション作成
function createPurchasePriceSection() {
    const newSection = document.createElement('div');
    newSection.id = 'purchasePriceSection';
    newSection.className = 'flex flex-col gap-2';
    newSection.innerHTML = `
        <div class="price-input-wrapper">
        <input type="number" id="purchasePrice" name="purchasePrice" placeholder="0" min="0" class="w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:border-blue-500">
        </div>
        `;
    
    const purchaseLabel = purchaseCheckbox.closest('label');
    purchaseLabel.after(newSection);
    
    document.getElementById('purchasePrice').focus();
}

// ページ遷移（サイズ・洗濯）
function openSizePage() {
    const size = prompt('サイズを入力してください (例: M, L, XL):');
    if (size) {
        document.getElementById('sizeInput').value = size;
        document.getElementById('sizeDisplay').textContent = `選択済み: ${size}`;
    }
}

function openWashingPage() {
    const washing = prompt('洗濯表示を入力してください:');
    if (washing) {
        document.getElementById('washingInput').value = washing;
        document.getElementById('washingDisplay').textContent = `選択済み: ${washing}`;
    }
}

// フォーム検証
function validateForm() {
    let isValid = true;
    const form = document.getElementById('sellerForm');

    // 商品名
    const productName = form.querySelector('[name="productName"]').value.trim();
    if (!productName) {
        document.getElementById('productNameError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('productNameError').classList.add('hidden');
    }

    // レンタル・購入
    const rental = form.querySelector('[name="rental"]').checked;
    const purchase = form.querySelector('[name="purchase"]').checked;
    if (!rental && !purchase) {
        document.getElementById('rentalPurchaseError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('rentalPurchaseError').classList.add('hidden');
    }

    // 系統カラー
    const color = form.querySelector('[name="color"]').value.trim();
    if (!color) {
        document.getElementById('colorError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('colorError').classList.add('hidden');
    }

    // カテゴリー1
    const category1 = form.querySelector('[name="category1"]').value;
    if (!category1) {
        document.getElementById('category1Error').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('category1Error').classList.add('hidden');
    }

    // カテゴリー2
    const category2 = form.querySelector('[name="category2"]').value;
    if (!category2) {
        document.getElementById('category2Error').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('category2Error').classList.add('hidden');
    }

    // サイズ
    const size = form.querySelector('[name="size"]').value;
    if (!size) {
        document.getElementById('sizeError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('sizeError').classList.add('hidden');
    }

    // 洗濯
    const washing = form.querySelector('[name="washing"]').value;
    if (!washing) {
        document.getElementById('washingError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('washingError').classList.add('hidden');
    }

    // 返却場所
    const returnLocation = form.querySelector('[name="returnLocation"]').value.trim();
    if (!returnLocation) {
        document.getElementById('returnLocationError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('returnLocationError').classList.add('hidden');
    }

    return isValid;
}
// フォーム送信
document.getElementById('sellerForm').addEventListener('submit', function(e) {
    e.preventDefault();
    if (validateForm()) {
        const formData = new FormData(this);
        const data = Object.fromEntries(formData);
        console.log('送信データ:', data);
        // 実際はここでサーバーに送信
        alert('フォームが送信されました');
    } else {
        alert('すべての必須項目を入力してください');
    }
});

// 下書き保存
function saveDraft() {
    const form = document.getElementById('sellerForm');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    alert('下書きが保存されました');
}