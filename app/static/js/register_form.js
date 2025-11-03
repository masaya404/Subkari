    // ------------------------------------
    // フォーム送信ハンドラ (デモ用)
    // ------------------------------------
    // function handleRegisterForm(event) {
    //     event.preventDefault();
        
    //     const account = document.getElementById('account').value.trim();
    //     const lastname = document.getElementById('lastname').value.trim();
    //     const prefecture = document.querySelector('.rfo-prefecture-selected').textContent;
    //     const phone = document.getElementById('phone').value.trim();
    //     const postal = document.getElementById('postal').value.trim();

    //     if (prefecture === '選択してください') {
    //          alert('都道府県を選択してください。');
    //          return false;
    //     }

    //     if (phone.length < 10 || phone.length > 11 || postal.length !== 7) {
    //          alert('入力内容に誤りがあります。（電話番号は10-11桁、郵便番号は7桁）');
    //          return false;
    //     }

    //     console.log('登録実行:', { account, lastname, prefecture, phone });
    //     alert(`アカウント名: ${account} での登録を完了しました！`);
    //     // 実際の遷移: window.location.href = 'registration-complete.html';
    //     return false;
    // }


    // // ------------------------------------
    // // カスタムセレクトボックス (都道府県) 動作
    // // ------------------------------------
    // document.addEventListener('DOMContentLoaded', function() {
    //     const prefectureFrame = document.getElementById('prefectureFrame');
    //     if (!prefectureFrame) return;

    //     const selectedDiv = prefectureFrame.querySelector('.rfo-prefecture-selected');
    //     const optionsList = prefectureFrame.querySelector('.rfo-prefecture-options');
    //     const options = optionsList.querySelectorAll('li');

    //     // 1. フレームをクリックしたらリストの表示/非表示を切り替える
    //     prefectureFrame.addEventListener('click', function(e) {
    //         // クリックがリスト内の要素でない場合、リストの表示を切り替える
    //         if (e.target.closest('.rfo-prefecture-options') === null) {
    //             optionsList.style.display = optionsList.style.display === 'block' ? 'none' : 'block';
    //         }
    //     });

    //     // 2. リストの項目をクリックしたときの処理
    //     options.forEach(option => {
    //         option.addEventListener('click', function() {
    //             // 選択された値を表示部に反映させる
    //             selectedDiv.textContent = this.textContent;
                
    //             // リストを非表示にする
    //             optionsList.style.display = 'none';
    //         });
    //     });

    //     // 3. 画面のどこかをクリックしたらリストを閉じる（UX向上）
    //     document.addEventListener('click', function(e) {
    //         if (!prefectureFrame.contains(e.target)) {
    //             optionsList.style.display = 'none';
    //         }
    //     });
    // });

    // ------------------------------------
    // 郵便番号から住所を自動入力するダミー機能
    // ------------------------------------
document.getElementById('postal').addEventListener('blur', function() {
    const postal = this.value.replace(/[^0-9]/g, ''); // 数字だけ抽出
    if (postal.length === 7) {
        fetch(`https://zipcloud.ibsnet.co.jp/api/search?zipcode=${postal}`)
        .then(res => res.json())
        // .then(data => {
        //     if (data.status === 200 && data.results) {
        //         const result = data.results[0];
        //         document.querySelector('.rfo-prefecture-selected').textContent = result.address1; // 都道府県
        //         document.getElementById('city').value = result.address2; // 市区町村
        //         document.getElementById('address').value = result.address3; // 番地
        //         document.getElementById('building').focus(); // 次の入力欄にフォーカス
        //     } else {
        //         console.log('住所が見つかりません');
        //     }
            .then(data => {
            if (data.status === 200 && data.results) {
                const result = data.results[0];
                
                const prefectureInput = document.getElementById('prefecture'); // hidden input
                const prefectureDisplay = document.querySelector('.rfo-prefecture-selected'); // 表示部分

                prefectureDisplay.textContent = result.address1; // 表示部分の更新
                prefectureInput.value = result.address1; // ★隠しフィールドにも値を設定★
                
                document.getElementById('city').value = result.address2; // 市区町村
                document.getElementById('address').value = result.address3; // 番地
                document.getElementById('building').focus(); // 次の入力欄にフォーカス
            } else {
                console.log('住所が見つかりません');
            }
        })
        .catch(err => console.error(err));
    }
});

// DOM（HTML）の読み込みが完了したら実行
document.addEventListener('DOMContentLoaded', function() {
    
    // 必要な要素を取得
    const frame = document.getElementById('prefectureFrame');
    const selectedDisplay = frame.querySelector('.rfo-prefecture-selected');
    const optionsList = frame.querySelector('.rfo-prefecture-options');
    const options = optionsList.querySelectorAll('li');
    
    // 「隠しフィールド」を取得
    const hiddenInput = document.getElementById('prefecture');

    // --- 1. ドロップダウンの「開閉」処理 ---
    selectedDisplay.addEventListener('click', function() {
        // 現在の表示状態を取得し、逆にする
        const isHidden = optionsList.style.display === 'none';
        optionsList.style.display = isHidden ? 'block' : 'none';
    });

    // --- 2. 選択肢（li）がクリックされたときの処理 ---
    options.forEach(function(li) {
        li.addEventListener('click', function() {
            
            // クリックされた li から値（都道府県名）を取得
            const selectedValue = li.textContent; // "東京都" など
            
            // (A) 「選択してください」の表示テキストを更新
            selectedDisplay.textContent = selectedValue || '選択してください';
            
            // (B) ★最重要★ 隠しフィールドの value を更新
            hiddenInput.value = selectedValue;

            // (C) 選択肢リストを閉じる
            optionsList.style.display = 'none';
        });
    });

    // --- (オプション) ドロップダウンの外側をクリックしたら閉じる ---
    document.addEventListener('click', function(event) {
        // クリックされた場所がフレーム（frame）の内側でない場合
        if (!frame.contains(event.target)) {
            optionsList.style.display = 'none';
        }
    });
});