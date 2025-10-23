
// 画像プレビュー
function previewImage(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('profilePreview').src = e.target.result;
        }
        reader.readAsDataURL(file);
    }
}

// 文字数カウント
function updateCharCount(inputId, countId, maxLength) {
    const input = document.getElementById(inputId);
    const count = document.getElementById(countId);
    count.textContent = input.value.length;
}

// アカウント名のバリデーション
function validateAccountName() {
    const input = document.getElementById('accountName');
    const error = document.getElementById('nameError');
    
    if (input.value.trim() === '') {
        input.classList.add('error');
        error.classList.add('show');
        return false;
    } else {
        input.classList.remove('error');
        error.classList.remove('show');
        return true;
    }
}

// 自己紹介のバリデーション
function validateBio() {
    const input = document.getElementById('bio');
    const error = document.getElementById('bioError');
    const countWrapper = document.getElementById('bioCountWrapper');
    
    if (input.value.length > 1000) {
        input.classList.add('error');
        error.classList.add('show');
        countWrapper.classList.add('error');
        return false;
    } else {
        input.classList.remove('error');
        error.classList.remove('show');
        countWrapper.classList.remove('error');
        return true;
    }
}

// フォーム送信
function handleSubmit(event) {
    event.preventDefault();
    
    const isNameValid = validateAccountName();
    const isBioValid = validateBio();
    
    if (isNameValid && isBioValid) {
        alert('プロフィールを更新しました');
        // ここで実際の更新処理を行う
    }
}

// キャンセル機能を削除
// function handleCancel() は不要になったため削除

// ページ読み込み時に文字数を更新
window.onload = function() {
    updateCharCount('accountName', 'nameCount', 20);
    updateCharCount('bio', 'bioCount', 1000);
}