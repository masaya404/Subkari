    
// フォーム要素の取得
const form = document.getElementById('transferForm');
const amountInput = document.getElementById('amount');
const errorMessage = document.getElementById('errorMessage');
const submitButton = document.querySelector('.submit-button');

// 金額入力時のバリデーション
amountInput.addEventListener('input', function() {
    validateAmount();
});

// 金額のバリデーション関数
function validateAmount() {
    const amount = parseInt(amountInput.value);
    errorMessage.classList.remove('show');
    
    if (!amountInput.value) {
        return false;
    }

    if (amount < 0) {
        errorMessage.textContent = '金額は0円以上を入力してください。';
        errorMessage.classList.add('show');
        return false;
    }

    if (amount > 1000000) {
        errorMessage.textContent = '一度に振り込める限度額は1,000,000円までです。';
        errorMessage.classList.add('show');
        return false;
    }

    // 手数料200円を考慮した最低金額チェック
    if (amount > 0 && amount < 201) {
        errorMessage.textContent = '振込手数料200円を含め、最低201円以上の金額を入力してください。';
        errorMessage.classList.add('show');
        return false;
    }

    return true;
}

// フォーム送信時の処理
form.addEventListener('submit', function(e) {
    e.preventDefault();

    if (!amountInput.value) {
        errorMessage.textContent = '金額を入力してください。';
        errorMessage.classList.add('show');
        return;
    }

    if (validateAmount()) {
        const amount = parseInt(amountInput.value);
        const fee = 200;
        const total = amount + fee;

        // 確認メッセージ
        const confirmed = confirm(
            `振込金額: ${amount.toLocaleString()}円\n` +
            `振込手数料: ${fee.toLocaleString()}円\n` +
            `合計: ${total.toLocaleString()}円\n\n` +
            `この内容で振込申請を確定しますか？`
        );

        if (confirmed) {
            // 実際の処理ではここでサーバーにデータを送信
            console.log('振込金額:', amount);
            console.log('振込手数料:', fee);
            console.log('合計:', total);
            
            alert('振込申請が完了しました。');
            // 次のページへ遷移（実装時は適切なURLを指定）
            // window.location.href = 'next-page.html';
        }
    }
});

// 数字のみ入力を許可
amountInput.addEventListener('keypress', function(e) {
    if (e.key === '-' || e.key === '+' || e.key === 'e' || e.key === 'E') {
        e.preventDefault();
    }
});

// カンマ区切りの表示（オプション）
amountInput.addEventListener('blur', function() {
    if (this.value) {
        const amount = parseInt(this.value);
        if (!isNaN(amount)) {
            // カンマを追加して表示したい場合はここで処理
            // this.value = amount.toLocaleString();
        }
    }
});