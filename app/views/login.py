from flask import Blueprint, render_template, request, make_response, redirect, url_for, session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import mysql.connector
import json
import os

login_bp = Blueprint('login', __name__, url_prefix='/login')


# Login画面表示 ----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/login', methods=['GET'])
def login():
    # errorメッセージ
    etbl = {}
    account = {}
    return render_template('login/login.html', etbl=etbl, account=account)


# Login確認 --------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/login/auth', methods=['POST'])
def login_auth():
    # mail,password取得
    account = request.form

    # error回数とメッセージ
    ecnt = 0
    error_message = {}

    # 空欄確認
    for key, value in account.items():
        if not value:
            ecnt += 1
    # 空欄あり、登録できない
    if ecnt != 0:
        return render_template('login/login.html', account=account)

    # 入力した資料がデータベースに存在するかどうかを確認
    sql = "SELECT * FROM m_account WHERE mail = %s;"
    con = connect_db()
    cur = con.cursor(dictionary=True)
    cur.execute(sql, (account['mail'],))
    userExist = cur.fetchone()
    # ユーザーが存在しないまたはパスワードが一致しない
    if not userExist or userExist['password'] != account['password']:
        error_message = "メールアドレスまたはパスワードが正しくありません。"
        return render_template('login/login.html', account=account, error_message=error_message)

    # 登録成功の処理
    session['user_id'] = userExist['username']
    # 後始末
    cur.close()
    con.close()

    return redirect(url_for('top.member_index'))


# Logout --------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/login/logout', methods=['GET'])
def logout():
    session.pop('user_id', None)
    return render_template('top/guest_index.html')


# Register確認 ----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/register', methods=['GET'])
def show_register():
    return render_template("login/new_account.html", account={}, error=None, error_same=None)


@login_bp.route("/", methods=["GET"])
def show_register_user():
    account = {}
    return render_template("login/new_account.html", account=account, error=None, error_same=None)


@login_bp.route("/register_user_complete", methods=["POST"])
def register_user_complete():
    mail = request.form.get("mail")
    password = request.form.get("password")
    password_confirm = request.form.get("password_confirm")

    error = None
    error_same = None

    # バリデーション
    if not mail or not password or not password_confirm:
        error = "全ての項目を入力してください。"
    elif password != password_confirm:
        error = "パスワードが一致しません。"
    else:
        # 仮登録（セッションに保存）
        users = session.get("users", {})
        if mail in users:
            error_same = "このメールアドレスはすでに登録されています。"
        else:
            users[mail] = password
            session["users"] = users
            # 登録成功 → register_form.html に遷移
            return render_template("login/register_form.html", account={"mail": mail})

    # エラーがあった場合は再表示
    return render_template("login/new_account.html", account={"mail": mail}, error=error, error_same=error_same)


# DB設定 ------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        db='db_subkari'
    )
    return con


# password-reset ----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/password-reset', methods=['GET'])
def password_reset():
    error = None
    success = None
    return render_template('login/password_reset.html', error=error, success=success)


@login_bp.route('/password-reset', methods=['POST'])
def reset_password():
    password = request.form.get('password')
    password_confirm = request.form.get('password_confirm')
    error = None
    success = None

    # バリデーション
    if not password or not password_confirm:
        error = "パスワードを入力してください。"
    elif password != password_confirm:
        error = "パスワードが一致しません。"
    elif len(password) < 8:
        error = "パスワードは8文字以上で入力してください。"
    else:
        # 実際にはここでDBにパスワードを更新
        success = "パスワードを更新しました。"

    return render_template('login/password_reset.html', error=error, success=success)
