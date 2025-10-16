// モーダル開閉処理
document.addEventListener("DOMContentLoaded", () => {
    const modals = document.querySelectorAll(".modal");
    const openButtons = document.querySelectorAll(".change-btn");
    const closeButtons = document.querySelectorAll(".modal-close");

    // モーダルを開く
    openButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const modalId = btn.dataset.modal;
            document.getElementById(modalId).style.display = "block";
        });
    });

    // モーダルを閉じる
    closeButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            modals.forEach(m => m.style.display = "none");
        });
    });

    // モーダル外クリックで閉じる
    window.addEventListener("click", e => {
        modals.forEach(m => {
            if (e.target === m) {
                m.style.display = "none";
            }
        });
    });

    // 購入確定ボタン
    const confirmBtn = document.querySelector(".confirm-btn");
    confirmBtn.addEventListener("click", () => {
        if (confirm("購入を確定しますか？")) {
            alert("購入が確定しました！");
            // Flaskに送信する場合はここでフォーム送信などを行う
            // location.href = "/purchase_complete";
        }
    });
});
