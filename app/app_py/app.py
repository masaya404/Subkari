from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# 仮ユーザーデータ（通常はDBを使用）
users = {
    "test@example.com": {"password": "password123", "phone": "09012345678"}
}

# ----------------------
# ログイン処理
# ----------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email in users and users[email]['password'] == password:
            session['user'] = email
            flash("ログインしました")
            return redirect(url_for('dashboard'))
        else:
            flash("メールアドレスまたはパスワードが間違っています")
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"{session['user']} さん、ようこそ！"
    return redirect(url_for('login'))

# ----------------------
# メールアドレス忘れた場合
# ----------------------
@app.route('/forgot_email', methods=['GET', 'POST'])
def forgot_email():
    if request.method == 'POST':
        phone = request.form.get('phone', '').strip()
        if phone and len(phone) in [10,11]:
            flash("登録された電話番号にメールアドレスをSMSで送信しました")
            return redirect(url_for('email_sent'))
        else:
            flash("正しい電話番号を入力してください")
            return redirect(url_for('forgot_email'))
    return render_template('forgot_email.html')

@app.route('/email_sent')
def email_sent():
    return "メール送信完了ページ"

# ----------------------
# 新規登録（メールアドレス・パスワード）
# ----------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('password_confirm')

        if password != confirm:
            flash("パスワードが一致しません")
            return redirect(url_for('register'))
        if len(password) < 8:
            flash("パスワードは8文字以上で入力してください")
            return redirect(url_for('register'))

        session['register_email'] = email
        session['register_password'] = password
        flash("確認メールを送信しました")
        return redirect(url_for('register_form'))
    return render_template('register.html')

# ----------------------
# 新規登録フォーム（個人情報）
# ----------------------
@app.route('/register_form', methods=['GET', 'POST'])
def register_form():
    if request.method == 'POST':
        phone = request.form.get('phone', '').strip()
        postal = request.form.get('postal', '').strip()
        birthday = request.form.get('birthday')
        prefecture = request.form.get('prefecture')

        if len(phone) not in [10,11]:
            flash("電話番号は10桁または11桁で入力してください")
            return redirect(url_for('register_form'))

        if len(postal) != 7:
            flash("郵便番号は7桁で入力してください")
            return redirect(url_for('register_form'))

        if not birthday:
            flash("生年月日を選択してください")
            return redirect(url_for('register_form'))

        if prefecture == '選択してください':
            flash("都道府県を選択してください")
            return redirect(url_for('register_form'))

        # 登録完了（ここでDB登録などを行う）
        flash("会員登録が完了しました")
        return redirect(url_for('registration_complete'))
    return render_template('register_form.html')

@app.route('/registration_complete')
def registration_complete():
    return "登録完了ページ"

# ----------------------
# 認証コード入力
# ----------------------
@app.route('/verify_code', methods=['GET', 'POST'])
def verify_code():
    if request.method == 'POST':
        code = request.form.get('code', '')
        if len(code) == 6 and code.isdigit():
            flash(f"認証コード {code} で認証しました")
            return redirect(url_for('dashboard'))
        else:
            flash("6桁の認証コードを入力してください")
            return redirect(url_for('verify_code'))
    return render_template('verify_code.html')

if __name__ == "__main__":
    app.run(debug=True)
