document.addEventListener('DOMContentLoaded', function() {
    //このページ入る同時に、画像を表示する（あった場合）
            loadUploadedImages();
    //session資料回復
            loadFromSessionStorage()
    //sizeデータ取得
            fetch('/seller/get_size_selected')
                .then(res => res.json())
                .then(size => {
                    console.log("Session size資料：", size);
                });
    //cleanデータ取得
            fetch('/seller/get_clean_selected')
                .then(res => res.json())
                .then(cleanNotes => {
                    console.log("Session cleanNotes資料：", cleanNotes);
                });
        });


// 価格トグル
const rentalCheckbox = document.querySelector('.rentalCheckbox');
const purchaseCheckbox = document.querySelector('.purchaseCheckbox');
const rentalPriceSection = document.getElementById('rentalPriceSection');
const purchasePriceSection = document.getElementById('purchasePriceSection');
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
    //アップロードした画像があった場合
    if (saved) {
        const images = JSON.parse(saved);
        console.log('Loaded images:', images);
        // ここで images を使用
        displayFirstImage(images[0]);
    }
}
//画像フィールドで表示 画像アップロード提示フィールドを隠す
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

//sessionに記録の関数//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function saveToSessionStorage(){
    //資料
    const productName = document.getElementById("name").value;
    const rental = document.getElementById("rental").checked;
    const purchase = document.getElementById("purchase").checked;
    const rentalPrice = document.getElementById("rentalPrice")?.value || '';
    const purchasePrice = document.getElementById("purchasePrice")?.value || '';
    const smokingValue = document.querySelector('input[name="smoking"]:checked').value;
    const color = document.getElementById("color").value;
    const category1 = document.getElementById("category1").value;
    const category2 = document.getElementById("category2").value;
    const brand = document.getElementById("brand").value;
    const explanation = document.getElementById("explanation").value;
    const returnLocation = document.querySelector('input[name="returnLocation"]').value;
    const rentalCheckbox = document.querySelector('.rentalCheckbox');
    const purchaseCheckbox = document.querySelector('.purchaseCheckbox');
    const rentalPriceSection = document.getElementById('rentalPriceSection');
    const purchasePriceSection = document.getElementById('purchasePriceSection');
    const rentalPurchaseError = document.getElementById('rentalPurchaseError');   
///////////////// Session保存//////////////////////////////////////////////////////////////////
    console.log("session saved");

    sessionStorage.setItem("name", productName);

    if (!rental) {
    sessionStorage.removeItem("rentalPrice");
    sessionStorage.setItem("rental", "false");
    } else {
        sessionStorage.setItem("rental", "true");
        sessionStorage.setItem("rentalPrice", rentalPrice);
    }

    if (!purchase) {
        sessionStorage.removeItem("purchasePrice");
        sessionStorage.setItem("purchase", "false");
    } else {
        sessionStorage.setItem("purchase", "true");
        sessionStorage.setItem("purchasePrice",purchasePrice);
    }

    sessionStorage.setItem("smoking", smokingValue);
    sessionStorage.setItem("color", color);
    sessionStorage.setItem("category1", category1);
    sessionStorage.setItem("category2", category2);
    sessionStorage.setItem("brand", brand);
    sessionStorage.setItem("explanation", explanation);
    sessionStorage.setItem("returnLocation", returnLocation);
  
    
}


// Session恢復////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function loadFromSessionStorage() {
    console.log("sessionStorageからデータを復元");

    // 商品名
    const name = sessionStorage.getItem("name");
    if (name) document.getElementById("name").value = name;

    // レンタル・購入
    const rental = sessionStorage.getItem("rental") === "true";
    const purchase = sessionStorage.getItem("purchase") === "true";
    const rentalCheckbox = document.getElementById("rental");
    const purchaseCheckbox = document.getElementById("purchase");
    if (rentalCheckbox) rentalCheckbox.checked = rental;
    if (purchaseCheckbox) purchaseCheckbox.checked = purchase;

    // レンタル価格
    const rentalPrice = sessionStorage.getItem("rentalPrice");
    if (rentalPrice) {
        if (!document.getElementById("rentalPrice")) {
            createRentalPriceSection(); // 動的に生成
        }
        document.getElementById("rentalPrice").value = rentalPrice;
    }

    // 購入価格
    const purchasePrice = sessionStorage.getItem("purchasePrice");
    if (purchasePrice) {
        if (!document.getElementById("purchasePrice")) {
            createPurchasePriceSection();
        }
        document.getElementById("purchasePrice").value = purchasePrice;
    }

    // 喫煙
    const smoking = sessionStorage.getItem("smoking");
    if (smoking) {
        const smokingRadio = document.querySelector(`input[name="smoking"][value="${smoking}"]`);
        if (smokingRadio) smokingRadio.checked = true;
    }

    // 系統カラー
    const color = sessionStorage.getItem("color");
    if (color) document.getElementById("color").value = color;

    // カテゴリー1・2
    const category1 = sessionStorage.getItem("category1");
    if (category1) document.getElementById("category1").value = category1;

    const category2 = sessionStorage.getItem("category2");
    if (category2) document.getElementById("category2").value = category2;

    // ブランド
    const brand = sessionStorage.getItem("brand");
    if (brand) document.getElementById("brand").value = brand;

    // 商品説明
    const explanation = sessionStorage.getItem("explanation");
    if (explanation) document.getElementById("explanation").value = explanation;

    // 返却場所
    const returnLocation = sessionStorage.getItem("returnLocation");
    if (returnLocation) {
        const el = document.querySelector('input[name="returnLocation"]');
        if (el) el.value = returnLocation;
    }
    console.log("sessionStorageからの復元完了");
}

//他の資料をsessionStorage裡面保存 その後size画面遷移/////////////////////////////////////////////////////////////////////////////////////////
function goToSize(sizeUrl){
    saveToSessionStorage();
    window.location.href = sizeUrl;
}
//他の資料をsessionStorage裡面保存 その後clean画面遷移/////////////////////////////////////////////////////////////////////////////////////////
function goToClean(sizeUrl){
    saveToSessionStorage();
    window.location.href = sizeUrl;
}

// document.getElementById("saveBtn").addEventListener("click", function() {
//   // 各 input 欄位的值を取得


//   // formDateで囲む
//   const formData = {
//     name: name,
//     email: email,
//     comment: comment
//   };

//   // JSONに変換して保存
//   sessionStorage.setItem("formData", JSON.stringify(formData));

//   alert("入力データを sessionStorage に保存しました！");
// });

// フォーム検証
function validateForm() {
    let isValid = true;

    // 商品名
    const productName = document.getElementById('name').value.trim();
    if (!productName) {
        document.getElementById('productNameError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('productNameError').classList.add('hidden');
    }

    // レンタル・購入
    const rental = document.getElementById('rental').checked;
    const purchase = document.getElementById('purchase').checked;
    if (!rental && !purchase) {
        document.getElementById('rentalPurchaseError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('rentalPurchaseError').classList.add('hidden');
    }

    // 系統カラー
    const color = document.getElementById('color').value.trim();
    if (!color) {
        document.getElementById('colorError').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('colorError').classList.add('hidden');
    }

    // カテゴリー1
    const category1 =document.getElementById('category1').value;
    if (!category1) {
        document.getElementById('category1Error').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('category1Error').classList.add('hidden');
    }

    // カテゴリー2
    const category2 = document.getElementById('category2').value;
    if (!category2) {
        document.getElementById('category2Error').classList.remove('hidden');
        isValid = false;
    } else {
        document.getElementById('category2Error').classList.add('hidden');
    }
     // brand
    const brand = document.getElementById('brand').value;
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
    const returnLocation = document.getElementById('returnLocation').value.trim();
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
///////////////////////////////////////////////////////画像の形式変換の関数///////////////////////////////////////////////////////////////////////////
function base64ToFile(base64Data, filename) {
  const arr = base64Data.split(',');
  const mime = arr[0].match(/:(.*?);/)[1];
  const bstr = atob(arr[1]);
  let n = bstr.length;
  const u8arr = new Uint8Array(n);
  while (n--) u8arr[n] = bstr.charCodeAt(n);
  return new File([u8arr], filename, { type: mime });
}

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
        console.log("未入力項目存在.")
        return;
    }

    // sessionStorage から画像を取得
    const uploadedImages = JSON.parse(sessionStorage.getItem('uploadedImages') || '[]');
    
    if (uploadedImages.length === 0) {
        alert('最低1つの画像をアップロードしてください');
        return;
    }
    console.log('=== 画像の格式確認 ===');
    console.log('uploadedImages:', uploadedImages);
    console.log('最初の画像:', uploadedImages[0]);

    // 全部のデータ変数
    const formData = new FormData();

     // ===== 画像 →　formData =====
        uploadedImages.forEach((imageData, index) => {
            try {
                const base64String = imageData.src;

                // Base64　転換　→　File
                const file = base64ToFile(base64String, `product_image_${index}.png`);
                formData.append('images', file);  // keyは'images'，複数あり
                console.log(`画像${index}FormDataに追加`);
            } catch (error) {
                console.error(`画像${index}形式変換失敗:`, error);
            }
        });

    //  sessionStorage 取得
    const productData = {
        name: sessionStorage.getItem("name"),
        rental: sessionStorage.getItem("rental") === "true",
        purchase: sessionStorage.getItem("purchase") === "true",
        rentalPrice: sessionStorage.getItem("rentalPrice") || null,
        purchasePrice: sessionStorage.getItem("purchasePrice") || null,
        smoking: sessionStorage.getItem("smoking") === "yes", // "yes" OR "no"
        color: sessionStorage.getItem("color"),
        category1: sessionStorage.getItem("category1"),
        category2: sessionStorage.getItem("category2"),
        brand: sessionStorage.getItem("brand"),
        explanation: sessionStorage.getItem("explanation"),
        returnLocation: sessionStorage.getItem("returnLocation"),
    };

    //すべてのデータ　→　formData
    formData.append('productData', JSON.stringify(productData));

    console.log('=== 準備完了 ===');
    console.log('画像の枚数:', uploadedImages.length);
    console.log('商品名:', productData.name);
    console.log('バックエンドに送る');

    fetch('/seller/format/save-product', {
        method: 'POST',
        body:formData
        // headers: {
        //     'Content-Type': 'application/json',
        // },
        // body: JSON.stringify(productData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('Success:', data);
            alert('登録成功ID: ' + data.product_id);
            // 成功後　sessionStorageのデータすべて消す
            sessionStorage.clear();
            window.location.href=url
        } else {
            alert('失敗: ' + data.message);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('catch失敗');
    });


}
// 下書き保存
function saveDraft(url) {
    // const form = document.getElementById('sellerForm');
    // const formData = new FormData(form);
    // const data = Object.fromEntries(formData);
    // alert('下書きが保存されました');
    window.location.href = url;
}


