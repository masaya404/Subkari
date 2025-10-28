from flask import Flask, Blueprint, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # セッション用の秘密鍵

login_bp = Blueprint("login", __name__, url_prefix="/login")

# -----------------------------
# ログイン画面表示
# -----------------------------
@login_bp.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html", error=None)

# -----------------------------
# ログイン処理
# -----------------------------
@login_bp.route("/login", methods=["POST"])
def login_auth():
    mail = request.form.get("mail")
    password = request.form.get("password")

    users = session.get("users", {})

    if mail in users and users[mail] == password:
        session["user_id"] = mail
        return redirect(url_for("login.member_index"))
    else:
        error = "メールアドレスまたはパスワードが正しくありません。"
        return render_template("login.html", error=error)

# -----------------------------
# 新規登録画面
# -----------------------------
@login_bp.route("/register", methods=["GET"])
def show_register():
    return render_template("register.html", account={}, error=None)

# -----------------------------
# 新規登録処理
# -----------------------------
@login_bp.route("/register", methods=["POST"])
def register_user_complete():
    mail = request.form.get("mail")
    password = request.form.get("password")
    password_confirm = request.form.get("password_confirm")

    if not mail or not password or not password_confirm:
        error = "全ての項目を入力してください。"
        return render_template("register.html", account=request.form, error=error)

    if password != password_confirm:
        error = "パスワードが一致しません。"
        return render_template("register.html", account=request.form, error=error)

    users = session.get("users", {})

    if mail in users:
        error = "このメールアドレスは既に登録されています。"
        return render_template("register.html", account=request.form, error=error)

    # セッションにユーザーを保存
    users[mail] = password
    session["users"] = users

    # 登録後ログイン
    session["user_id"] = mail
    return redirect(url_for("login.member_index"))

# -----------------------------
# 会員ページ
# -----------------------------
@login_bp.route("/member", methods=["GET"])
def member_index():
    if "user_id" not in session:
        return redirect(url_for("login.show_login"))
    return f"ようこそ {session['user_id']} さん！"

# -----------------------------
# ログアウト
# -----------------------------
@login_bp.route("/logout", methods=["GET"])
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login.show_login"))

# -----------------------------
# パスワードリセット（セッション内のみ）
# -----------------------------
@login_bp.route("/password-reset", methods=["GET"])
def password_reset():
    return render_template("password_reset.html", error=None, success=None)

@login_bp.route("/password-reset", methods=["POST"])
def reset_password():
    mail = request.form.get("mail")
    password = request.form.get("password")
    password_confirm = request.form.get("password_confirm")
    users = session.get("users", {})
    
    if not mail or not password or not password_confirm:
        error = "全ての項目を入力してください。"
        return render_template("password_reset.html", error=error, success=None)
    
    if mail not in users:
        error = "登録されていないメールアドレスです。"
        return render_template("password_reset.html", error=error, success=None)

    if password != password_confirm:
        error = "パスワードが一致しません。"
        return render_template("password_reset.html", error=error, success=None)

    users[mail] = password
    session["users"] = users
    success = "パスワードを更新しました。"
    return render_template("password_reset.html", error=None, success=success)

