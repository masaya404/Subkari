
let selectedPaymentMethod = 'card1';
let selectedDeliveryLocation = '玄関前';
let cardToDelete = null;

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
        closeDeleteConfirm();
        closePaymentEditModal();
    }
}

function editCard(event, cardId) {
    event.preventDefault();
    event.stopPropagation();
    alert('カード編集画面へ遷移します');
}

function goToCardRegister() {
    window.location.href = '#card-register';
}

function openDeliveryModal(event) {
    event.preventDefault();
    alert('配送先変更画面へ遷移します');
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

// モーダル外クリックで閉じる
document.querySelectorAll('.modal').forEach(modal => {
    modal.addEventListener('click', function(e) {
        if (e.target === this) {
            this.classList.remove('active');
        }
    });
});