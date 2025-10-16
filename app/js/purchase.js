
let selectedPaymentMethod = 'card1';
let selectedDeliveryLocation = '玄関前';
let selectedAddress = 'address1';
let cardToDelete = null;
let addressToDelete = null;

function openPaymentModal(event) {
    event.preventDefault();
    const modal = document.getElementById('paymentModal');
    if (modal) modal.classList.add('active');
}

function closePaymentModal() {
    const modal = document.getElementById('paymentModal');
    if (modal) modal.classList.remove('active');
}

function editPaymentMethods(event) {
    event.preventDefault();
    const paymentModal = document.getElementById('paymentModal');
    const editModal = document.getElementById('paymentEditModal');
    if (paymentModal) paymentModal.classList.remove('active');
    if (editModal) editModal.classList.add('active');
}

function closePaymentEditModal() {
    const modal = document.getElementById('paymentEditModal');
    if (modal) modal.classList.remove('active');
}

function completePaymentEdit(event) {
    event.preventDefault();
    closePaymentEditModal();
    const modal = document.getElementById('paymentModal');
    if (modal) modal.classList.add('active');
}

function selectPayment(method) {
    selectedPaymentMethod = method;
    
    document.querySelectorAll('.radio-btn').forEach(btn => {
        btn.classList.remove('selected');
    });
    
    const radioBtn = document.getElementById('radio-' + method);
    if (radioBtn) {
        radioBtn.classList.add('selected');
    }
}

function updatePaymentMethod() {
    const selectedCardElement = document.getElementById('selectedCard');
    
    switch(selectedPaymentMethod) {
        case 'card1':
            selectedCardElement.textContent = '************1234 01/01';
            break;
        case 'card2':
            selectedCardElement.textContent = '************1234 02/02';
            break;
        case 'card3':
            selectedCardElement.textContent = '************1234 03/03';
            break;
        case 'conveni':
            selectedCardElement.textContent = 'コンビニ支払い';
            break;
        case 'paypay':
            selectedCardElement.textContent = 'PayPay';
            break;
    }
    
    closePaymentModal();
    closePaymentEditModal();
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
    const page = document.getElementById('cardRegisterPage');
    if (page) {
        page.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
}

function closeCardRegister() {
    const page = document.getElementById('cardRegisterPage');
    if (page) {
        page.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
}

function openAddressModal(event) {
    event.preventDefault();
    const modal = document.getElementById('addressModal');
    if (modal) modal.classList.add('active');
}

function closeAddressModal() {
    const modal = document.getElementById('addressModal');
    if (modal) modal.classList.remove('active');
}

function editAddresses(event) {
    event.preventDefault();
    closeAddressModal();
    const modal = document.getElementById('addressEditModal');
    if (modal) modal.classList.add('active');
}

function closeAddressEditModal() {
    const modal = document.getElementById('addressEditModal');
    if (modal) modal.classList.remove('active');
}

function completeAddressEdit(event) {
    event.preventDefault();
    closeAddressEditModal();
    const addressModal = document.getElementById('addressModal');
    if (addressModal) addressModal.classList.add('active');
}

function selectAddress(addressId) {
    selectedAddress = addressId;
    
    document.querySelectorAll('[id^="radio-address"], [id^="radio-edit-address"]').forEach(btn => {
        btn.classList.remove('selected');
    });
    
    const radioBtn = document.getElementById('radio-' + addressId);
    const editRadioBtn = document.getElementById('radio-edit-' + addressId);
    if (radioBtn) radioBtn.classList.add('selected');
    if (editRadioBtn) editRadioBtn.classList.add('selected');
}

function updateAddress() {
    const selectedAddressElement = document.getElementById('selectedAddress');
    
    const addresses = {
        'address1': 'HAL 大阪（ハル オオサカ）<br>〒530-0001<br>大阪府 大阪市 北区 梅田3丁目3−1',
        'address2': 'HAL 東京（ハル トウキョウ）<br>〒160-0023<br>東京都新宿区西新宿1丁目7−3',
        'address3': 'HAL 名古屋（ハル ナゴヤ）<br>〒450-0002<br>愛知県名古屋市中村区名駅4丁目27−1'
    };
    
    selectedAddressElement.innerHTML = addresses[selectedAddress];
    closeAddressModal();
    closeAddressEditModal();
}

function confirmDeleteAddress(event, addressId) {
    event.stopPropagation();
    addressToDelete = addressId;
    document.getElementById('deleteConfirmModal').classList.add('active');
}

function addNewAddress() {
    // 住所が3件以上ある場合は制限アラート表示
    if (true) { // 実際には住所の数をチェック
        document.getElementById('addressLimitModal').classList.add('active');
    } else {
        openAddressRegister();
    }
}

function openAddressRegister() {
    closeAddressModal();
    closeAddressEditModal();
    document.getElementById('addressRegisterPage').style.display = 'block';
    document.body.style.overflow = 'hidden';
}

function closeAddressRegister() {
    document.getElementById('addressRegisterPage').style.display = 'none';
    document.body.style.overflow = 'auto';
}

function closeAddressLimitModal() {
    document.getElementById('addressLimitModal').classList.remove('active');
}

function registerNewAddress(e) {
    e.preventDefault();
    alert('新しい住所が登録されました');
    closeAddressRegister();
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

    // モーダル外クリックで閉じる
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.addEventListener('click', function(e) {
            if (e.target === this) {
                this.classList.remove('active');
            }
        });
    });
});