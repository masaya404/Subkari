document.addEventListener('DOMContentLoaded', function() {
    //このページ入る同時に、画像を表示する（あった場合）
            loadUploadedImages();
        });
// 画像編集へ
function goToUploadPage() {          
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

//画像表示
function loadUploadedImages() {
    const saved = sessionStorage.getItem('uploadedImages');
    if (saved) {
        const images = JSON.parse(saved);
        console.log('Loaded images:', images);
        // ここで images を使用
        displayFirstImage(images[0]);
    }
}

function displayFirstImage(image) {
    const displayArea = document.getElementById('imageDisplayArea');
    const noImageArea = document.getElementById('noImageArea');
    const displayImage = document.getElementById('displayImage');
    
    if (displayArea && displayImage) {
        displayImage.src = image.src;  // Base64 データURLを設定
        displayArea.classList.remove('hidden');
        
        if (noImageArea) {
            noImageArea.classList.add('hidden');
        }
    }
}

loadUploadedImages();

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
    const category = form.querySelector('[name="category"]').value;
    if (!category) {
        document.getElementById('categoryError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('categoryError').classList.add('hidden');
    }

    // カテゴリー2
    const brand = form.querySelector('[name="brand"]').value;
    if (!brand) {
        document.getElementById('brandError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('brandError').classList.add('hidden');
    }

    // サイズ
    const sizeDisplay = document.getElementById('sizeDisplay').innerText.trim();
    if (sizeDisplay === '未選択') {
        document.getElementById('sizeError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('sizeError').classList.add('hidden');
    }

    // 洗濯表示
    const washingDisplay = document.getElementById('washingDisplay').innerText.trim();
    if (washingDisplay === '未選択') {
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

 //サイズと洗濯表示を sessionStorage から読み込む
// function loadSizeAndWashing() {
//     // サイズ
//     const sizeFromSession = sessionStorage.getItem('size');
//     if (sizeFromSession && sizeFromSession !== '未選択') {
//         document.getElementById('sizeDisplay').innerText = sizeFromSession;
//     }
//     else{
//         isValid = false;
//     }
//     // 洗濯表示
//     const washingFromSession = sessionStorage.getItem('washing');
//     if (washingFromSession && washingFromSession !== '未選択') {
//         document.getElementById('washingDisplay').innerText = washingFromSession;
//     }
//     else{
//         isValid = false;
//     }
// }

/**
 * フォーム送信
 */
// document.getElementById('sellerForm').addEventListener('submit', function(e) {
//     e.preventDefault();
//     //検証成功
//     if (validateForm()) {
//         const formData = new FormData(this);
//         const data = Object.fromEntries(formData);
//         console.log('送信データ:', data);
//         // 実際はここでサーバーに送信
//         alert('フォームが送信されました');
//     } 
//     //検証失敗
//     else {
//         alert('すべての必須項目を入力してください');
//     }
// });
/**
 * フォーム送信
 */
function submitForm() {
    // バリデーション
    if (!validateForm()) {
        return;
    }

    // sessionStorage から画像を取得
    const uploadedImages = JSON.parse(sessionStorage.getItem('uploadedImages') || '[]');
    
    if (uploadedImages.length === 0) {
        alert('最低1つの画像をアップロードしてください');
        return;
    }

    // hidden input に JSON を設定
    document.getElementById('imagesData').value = JSON.stringify(uploadedImages);
    
    // フォーム送信
    document.getElementById('sellerForm').submit();
}
// 下書き保存
function saveDraft() {
    const form = document.getElementById('sellerForm');
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    alert('下書きが保存されました');
}