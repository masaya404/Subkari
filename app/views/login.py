from flask import Blueprint , render_template ,request,make_response,redirect,url_for,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

login_bp = Blueprint('login', __name__, url_prefix='/login')


#Login画面表示----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/login',methods=['GET'])
def login():
    #errorメッセージ
    etbl={}
    account={}
      
    return render_template('login/login.html',etbl=etbl,account=account)

#Login確認--------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/login/auth',methods=['POST'])
def login_auth():
    #mail,password取得
    account = request.form
    
    #error回数とメッセージ
    ecnt = 0
    error_message={}
    
    #空欄確認
    for key,value in account.items():
        if not value:
            ecnt+=1
    #空欄あり、登録できない      
    if ecnt !=0:
        return render_template('login/login.html',account=account)
    
    # 入力した資料がデータベースに存在するかどうかを確認
    sql = "SELECT * FROM m_account WHERE mail = %s;"
    con=connect_db()
    cur=con.cursor(dictionary=True)
    cur.execute(sql,(account['mail'],))
    # ここで確認
    userExist = cur.fetchone()
    #ユーザーが存在しないまたはパスワードが一致しない
    if not userExist or userExist['password'] != account['password']:
        error_message = "メールアドレスまたはパスワードが正しくありません。"
        return render_template('login/login.html',account=account,error_message = error_message)
    
    #登録成功の処理
    session['user_id'] = userExist['id']

    return redirect(url_for('top.member_index'))
    
#Logout--------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/login/logout',methods=['GET'])
def logout():
    session.pop('user_id', None)
    return render_template('top/guest_index.html')

#Register-------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route("/register_user", methods=["GET"])
def show_register_user():
    account = {}
    return render_template("login/new_account.html", account=account)


##りんた、これいらないよね⇂
# @login_bp.route('login/register_user',methods=['GET'])
# def register_user():
#     account = {}
   
#     return render_template('login/new_account.html',account=account)





#Register確認----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/register_user/complete',methods=['POST'])
def register_user_complete():
    account = request.form
    error = ""
    error_same = ""
    # 入力確認
    if account['password'] != account['password_confirm']:
        error = "パスワードと確認用パスワードが一致していません。"
        return render_template('login/new_account.html', error=error, account=account)
    
    
    #同一user確認    
    # con = None  # データベース接続オブジェクトを初期化
    # cur = None  # カーソルオブジェクトを初期化
    

    # 参考コードをここに応用します
    sql = "SELECT * FROM m_account WHERE mail = %s;"
    
    # connect_db() はご自身の環境で定義されているDB接続関数と想定しています
    con = connect_db() 
    cur = con.cursor(dictionary=True)
    
    # フォームから受け取ったメールアドレスをプレースホルダ(%s)に渡します
    # (account['mail'],) のようにカンマを付けてタプルにすることが重要です
    cur.execute(sql, (account['mail'],)) 
    
    # fetchone() で結果を1件取得します
    userExist = cur.fetchone()
    
    # existing_user が None でない場合 ＝ データが取得できた ＝ 既に使用されている
    if userExist:
        error_same = "このメールアドレスは既に使用されています。"
        # エラーなので、テンプレートをレンダリングして処理を終了します

        cur.close()
        con.close()
        return render_template('login/new_account.html', error=error, error_same=error_same)

    #ここからセッション登録して次の画面にせんいする
    # account の中身（イメージ）
    # {
    #   'mail': 'test@example.com',
    #   'password': 'password123',
    #   'password_confirm': 'password123'
    # }

    # データをセッションに登録
    # request.form (ImmutableMultiDict) を通常の辞書 (dict) に変換して保存
    session_data = dict(account)
    # セッションに 'registration_data' というキーで保存
    #このキーをつくってログイン状態のセッションと区別する(user_id)。
    # session オブジェクト全体の中身（イメージ）
    # {
    #   'registration_data': {
    #     'mail': 'test@example.com',
    #     'password': 'password123',
    #     'password_confirm': 'password123'
    #   }
    session['registration_data'] = session_data

    # ◆ 処理が正常終了した場合もDB接続をクローズします
    cur.close()
    con.close()
    return render_template('login/register_form.html', error=error, error_same=error_same)



    #DBに登録
    # user = (account['mail'],account['password'])
    # sql = "INSERT INTO m_account (mail,password) VALUES(%s,%s)"
    # cur.execute(sql,user)  
    # con.commit()
    # cur.close()
    # con.close()



# @login_bp.route("/register_user_complete", methods=["POST"])
# def handle_register_user_complete():
#     mail = request.form.get("mail")
#     password = request.form.get("password")
#     password_confirm = request.form.get("password_confirm")

#     if password != password_confirm:
#         error = "パスワードが一致しません。"
#         return render_template("register_user.html", error=error, account={"mail": mail})

#     session["user"] = {
#         "mail": mail,
#         "password": password
#     }

#     return redirect(url_for("login.register_complete"))


    # return redirect(url_for('top.new_account',account_id = account["mail"]))

@login_bp.route("register_user/form_complete", methods=["POST"])
def registration_form_complete():

    return render_template('login/Phone_verification.html')


#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con
    


#password-reset----------------------------------------------------------------------------------------------------------------------------------------------------------

@login_bp.route('/password-reset', methods=['GET'])
def password_reset():
    # 初期表示用に空の辞書を渡す
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














