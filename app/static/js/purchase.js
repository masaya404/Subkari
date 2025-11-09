
let selectedPaymentMethod = 'card1';
let selectedDeliveryLocation = '玄関前';
// let selectedAddress = 'address1';
let cardToDelete = null;
let addressToDelete = null;





// Pythonから渡された全ての住所データをJSON形式でJSの配列に格納
    //: tojson と safe フィルタに加えて、default('[]') を追加
    // 目的: 
    // 1. |tojson: PythonオブジェクトをJSON形式に変換
    // 2. |default('[]'): address_listがNoneやUndefinedの場合、空の配列 [] を代入してJSの構文エラーを防ぐ
    // 3. |safe: Jinja2がJSON文字列をエスケープしないようにし、JSで正しくパースできるようにする
    // const addressDataList = {{ address_list | tojson | default('[]') }};

    // 【代替案】: address_list が None の場合に先にデフォルト値を設定し、その後で tojson を適用する
    // const addressDataList = {{ address_list | default([]) | tojson | safe }};
    // // 現在選択されている住所のインデックス（0, 1, 2, ...）を保持
    // // 初期値として、最初の住所（0番目）を選択状態とします。
    // let selectedAddressIndex = 0; 
    
    // // ページロード時: 住所リストが存在すれば、初期表示（0番目の住所）をメイン画面に反映
    // document.addEventListener('DOMContentLoaded', () => {
    //     if (addressDataList.length > 0) {
    //         updateShippingInfo(selectedAddressIndex);
    //     }
    // });

console.log(addressDataList);


/**
 * 選択された住所のインデックスに基づいて、メイン画面の配送先情報を更新する
 * @param {number} index - 選択された住所データの配列インデックス (0, 1, 2, ...)
 */
function updateShippingInfo(index) {
    const shippingInfoElement = document.getElementById('selectedAddress');
    
    // インデックスが有効で、データが存在することを確認
    if (index >= 0 && index < addressDataList.length) {
        const selectedAddr = addressDataList[index];
        
        // HTML文字列を生成
        let htmlContent = `
            〒${selectedAddr.zip}<br>
            ${selectedAddr.pref} ${selectedAddr.address1} ${selectedAddr.address2}<br>
        `;
        
        // address3 が存在する場合のみ追加
        if (selectedAddr.address3) {
            htmlContent += `${selectedAddr.address3}`;
        }
        
        // メイン画面の内容を更新
        shippingInfoElement.innerHTML = htmlContent;

        // グローバル変数に新しいインデックスを保存
        selectedAddressIndex = index;

    } else if (addressDataList.length === 0) {
        // 住所データが一つもない場合の表示
         shippingInfoElement.innerHTML = '<p>配送先の住所が登録されていません。「変更する」ボタンから登録してください。</p>';
    }
}

function openPaymentModal(event) {
    event.preventDefault();
    document.getElementById('paymentModal').classList.add('active');
}

function closePaymentModal() {
    document.getElementById('paymentModal').classList.remove('active');
}

function editPaymentMethods(event) {
    event.preventDefault();
    document.getElementById('paymentModal').classList.remove('active');
    document.getElementById('paymentEditModal').classList.add('active');
}

function closePaymentEditModal() {
    document.getElementById('paymentEditModal').classList.remove('active');
}

function completePaymentEdit(event) {
    event.preventDefault();
    closePaymentEditModal();
    document.getElementById('paymentModal').classList.add('active');
}

function selectPayment(method) {
    selectedPaymentMethod = method;
    
    // paymentModalとpaymentEditModalの両方のラジオボタンの状態を同期させる
    document.querySelectorAll('#paymentModal .radio-btn, #paymentEditModal .radio-btn').forEach(btn => {
        btn.classList.remove('selected');
    });
    
    const radioBtn = document.getElementById('radio-' + method);
    const editRadioBtn = document.getElementById('radio-edit-' + method);

    if (radioBtn) radioBtn.classList.add('selected');
    if (editRadioBtn) editRadioBtn.classList.add('selected');
}

// ▼▼▼ 変更点3: このJavaScript関数を全面的に修正しました ▼▼▼
function updatePaymentMethod() {
    const paymentInfoDisplay = document.getElementById('payment-info-display');
    const paymentSummaryValue = document.getElementById('payment-summary-value');

    switch(selectedPaymentMethod) {
        case 'card1':
            paymentInfoDisplay.innerHTML = `クレジットカード決済 <div class="masked-card" id="selectedCard">************1234 01/01</div>`;
            paymentSummaryValue.textContent = 'クレジットカード';
            break;
        case 'card2':
            paymentInfoDisplay.innerHTML = `クレジットカード決済 <div class="masked-card" id="selectedCard">************1234 02/02</div>`;
            paymentSummaryValue.textContent = 'クレジットカード';
            break;
        case 'card3':
            paymentInfoDisplay.innerHTML = `クレジットカード決済 <div class="masked-card" id="selectedCard">************1234 03/03</div>`;
            paymentSummaryValue.textContent = 'クレジットカード';
            break;
        case 'conveni':
            paymentInfoDisplay.innerHTML = 'コンビニ支払い';
            paymentSummaryValue.textContent = 'コンビニ支払い';
            break;
        case 'paypay':
            paymentInfoDisplay.innerHTML = 'PayPay';
            paymentSummaryValue.textContent = 'PayPay';
            break;
    }
    
    closePaymentModal();
    closePaymentEditModal();
}



/**
 * 選択された支払い方法 (bank-X, conveni, paypay) に基づいてメイン画面を更新する
 * (住所の updateShippingInfo と同じロジック)
 */
function updatePaymentInfo(methodId) {
    const paymentInfoDisplay = document.getElementById('selectedPaymentInfo');
    let htmlContent = '';

    if (methodId.startsWith('bank-')) {
        const index = parseInt(methodId.split('-')[1]);
        if (index >= 0 && index < bankInfoList.length) {
            const info = bankInfoList[index];
            const maskedNum = maskedAccountNumbers[index];
            
            htmlContent = `
                銀行口座 (${info.bankName})<br>
                口座番号: ${maskedNum}
            `;
            // グローバル変数とサマリー表示を更新
            selectedPaymentMethod = methodId; 
            document.getElementById('payment-summary-value').textContent = '銀行口座';
            selectedBankIndex = index; // インデックスも保存
        }
    } else {
        // 静的な支払い方法 (conveni, paypay)
        let methodText = '';
        if (methodId === 'conveni') {
            methodText = 'コンビニ支払い';
        } else if (methodId === 'paypay') {
            methodText = 'PayPay';
        } else {
            // その他、初期値 'card1' など、ハードコードされた古い値の場合のフォールバック
            methodText = 'クレジットカード決済'; 
        }
        
        htmlContent = methodText;
        selectedPaymentMethod = methodId;
        document.getElementById('payment-summary-value').textContent = methodText;
    }

    paymentInfoDisplay.innerHTML = htmlContent;
}

// 既存の selectPayment 関数も、選択後にメイン画面を更新するように修正
function selectPayment(methodId) {
    // ... (既存のラジオボタン切り替えロジック) ...
    
    // メイン画面の支払い情報を更新
    updatePaymentInfo(methodId);
    
    // グローバル変数 selectedPaymentMethod を更新
    selectedPaymentMethod = methodId; 
}





function confirmDeleteCard(event, cardId) {
    event.stopPropagation();
    cardToDelete = cardId;
    document.getElementById('deleteConfirmModal').classList.add('active');
}

function closeDeleteConfirm() {
    document.getElementById('deleteConfirmModal').classList.remove('active');
    cardToDelete = null;
}

function executeDelete() {
    if (cardToDelete) {
        alert('カード ' + cardToDelete + ' が削除されました');
        cardToDelete = null;
    }
    if (addressToDelete) {
        alert('住所 ' + addressToDelete + ' が削除されました');
        addressToDelete = null;
    }
    closeDeleteConfirm();
    closePaymentEditModal();
    closeAddressEditModal();
}

function editCard(event, cardId) {
    event.preventDefault();
    event.stopPropagation();
    alert('カード編集画面へ遷移します');
}

function goToCardRegister() {
    closePaymentModal();
    closePaymentEditModal();
    document.getElementById('cardRegisterPage').style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeCardRegister() {
    document.getElementById('cardRegisterPage').style.display = 'none';
    document.body.style.overflow = 'auto';
}

function openAddressModal(event) {
    event.preventDefault();
    document.getElementById('addressModal').classList.add('active');
}

function closeAddressModal() {
    document.getElementById('addressModal').classList.remove('active');
}

function editAddresses(event) {
    event.preventDefault();
    document.getElementById('addressModal').classList.remove('active');
    document.getElementById('addressEditModal').classList.add('active');
}

function closeAddressEditModal() {
    document.getElementById('addressEditModal').classList.remove('active');
}

function completeAddressEdit(event) {
    event.preventDefault();
    closeAddressEditModal();
    document.getElementById('addressModal').classList.add('active');
}

// function selectAddress(addressId) {
//     selectedAddress = addressId;
    
//     document.querySelectorAll('[id^="radio-address"], [id^="radio-edit-address"]').forEach(btn => {
//         btn.classList.remove('selected');
//     });
    
//     const radioBtn = document.getElementById('radio-' + addressId);
//     const editRadioBtn = document.getElementById('radio-edit-' + addressId);
//     if (radioBtn) radioBtn.classList.add('selected');
//     if (editRadioBtn) editRadioBtn.classList.add('selected');
// }


function selectAddress(addressId) {
    // 例: addressId が 'address-0' の場合、インデックス 0 を抽出
    const indexStr = addressId.split('-')[1];
    const index = parseInt(indexStr);
    
    // ラジオボタンの選択状態を切り替える (既存のロジック)
    document.querySelectorAll('[id^="radio-address"], [id^="radio-edit-address"]').forEach(btn => {
        btn.classList.remove('selected');
    });
    
    // 通常用と編集用の両方のラジオボタンを選択状態にする
    const radioBtn = document.getElementById('radio-' + addressId);
    const editRadioBtn = document.getElementById('radio-edit-' + addressId);
    if (radioBtn) radioBtn.classList.add('selected');
    if (editRadioBtn) editRadioBtn.classList.add('selected');

    // 【新しい処理】: メイン画面の配送先情報を更新
    if (!isNaN(index)) { // インデックスが有効な数値であることを確認
        updateShippingInfo(index);
    }

    // 選択後、モーダルを閉じたい場合はここで閉じます
    // document.getElementById('addressModal').classList.remove('active');
}

// function updateAddress() {
//     const selectedAddressElement = document.getElementById('selectedAddress');
    
//     const addresses = {
//         'address1': 'HAL 大阪（ハル オオサカ）<br>〒530-0001<br>大阪府 大阪市 北区 梅田3丁目3−1',
//         'address2': 'HAL 東京（ハル トウキョウ）<br>〒160-0023<br>東京都新宿区西新宿1丁目7−3',
//         'address3': 'HAL 名古屋（ハル ナゴヤ）<br>〒450-0002<br>愛知県名古屋市中村区名駅4丁目27−1'
//     };
    
//     selectedAddressElement.innerHTML = addresses[selectedAddress];
//     closeAddressModal();
//     closeAddressEditModal();
// }

function confirmDeleteAddress(event, addressId) {
    event.stopPropagation();
    addressToDelete = addressId;
    document.getElementById('deleteConfirmModal').classList.add('active');
}

function addNewAddress() {
    alert('新しい住所登録画面へ遷移します');
}

function openDeliveryLocationModal(event) {
    event.preventDefault();
    document.getElementById('deliveryLocationModal').classList.add('active');
}

function closeDeliveryLocationModal() {
    document.getElementById('deliveryLocationModal').classList.remove('active');
}

function selectDeliveryLocation(location) {
    selectedDeliveryLocation = location;
    
    document.querySelectorAll('#deliveryLocationModal .radio-btn').forEach(btn => {
        btn.classList.remove('selected');
    });
    
    const locationMap = {
        '玄関前': 'door',
        '宅配ボックス': 'box',
        'ガスメーターボックス': 'gas',
        '自転車のカゴ': 'bicycle',
        '車庫': 'garage',
        '建物内受付/管理人': 'reception',
        '選択しない': 'none'
    };
    
    const radioId = 'radio-' + locationMap[location];
    const radioBtn = document.getElementById(radioId);
    if (radioBtn) {
        radioBtn.classList.add('selected');
    }
}

function updateDeliveryLocation() {
    document.getElementById('selectedDeliveryLocation').textContent = selectedDeliveryLocation;
    closeDeliveryLocationModal();
}

function confirmPurchase() {
    alert('購入が確定されました。ありがとうございます！');
}

function openSecurityHelp() {
    document.getElementById('securityHelpModal').classList.add('active');
}

function closeSecurityHelp() {
    document.getElementById('securityHelpModal').classList.remove('active');
}

function registerNewCard(e) {
    e.preventDefault();
    const cardNumber = document.getElementById('newCardNumber').value;
    const cardExpiry = document.getElementById('newCardExpiry').value;
    const securityCode = document.getElementById('newSecurityCode').value;

    if (!cardNumber || !cardExpiry || !securityCode) {
        alert('すべての項目を入力してください');
        return;
    }

    alert('クレジットカードが登録されました');
    closeCardRegister();
    
    // フォームをリセット
    document.getElementById('newCardNumber').value = '';
    document.getElementById('newCardExpiry').value = '';
    document.getElementById('newSecurityCode').value = '';
}

// カード番号の自動フォーマット
document.addEventListener('DOMContentLoaded', function() {
    const cardNumberInput = document.getElementById('newCardNumber');
    if (cardNumberInput) {
        cardNumberInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\s/g, '');
            let formattedValue = value.match(/.{1,4}/g)?.join(' ') || value;
            e.target.value = formattedValue;
        });
    }

    const cardExpiryInput = document.getElementById('newCardExpiry');
    if (cardExpiryInput) {
        cardExpiryInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length >= 2) {
                value = value.slice(0, 2) + '/' + value.slice(2, 4);
            }
            e.target.value = value;
        });
    }
});

// モーダル外クリックで閉じる
document.querySelectorAll('.modal').forEach(modal => {
    modal.addEventListener('click', function(e) {
        if (e.target === this) {
            this.classList.remove('active');
        }
    });
});