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



# DBスキーマに対応するバリデーションルール
# m_address テーブルの定義に基づき設定

# Flaskのルート関数（registration_form_complete）の「前」に、
# この辞書を定義します。

# 'name属性': (最大文字数, 必須か否か) のタプル
# 最大文字数: SQLのVARCHAR(N)やCHAR(N)のNの値。
#             DATE, INT, BOOLEAN型は文字列長ではないため「None」とします。
# 必須か否か: SQLで「NOT NULL」が指定されていれば「True」。
#             「NULL」許容（指定なし）であれば「False」。

ACCOUNT_SCHEMA = {
    # --- m_account ---------------------------------------------
    # 1. アカウント名
    'account':          (12, True),   # m_account.username VARCHAR(12) NOT NULL
    
    # 2. 姓 (全角)
    'last_name':        (50, True),   # m_account.last_name VARCHAR(50) NOT NULL
    
    # 3. 名 (全角)
    'first_name':       (50, True),   # m_account.first_name VARCHAR(50) NOT NULL
    
    # 4. セイ (全角)
    'last_name_kana':   (50, True),   # m_account.last_name_kana VARCHAR(50) NOT NULL
    
    # 5. メイ (全角)
    'first_name_kana':  (50, True),   # m_account.first_name_kana VARCHAR(50) NOT NULL
    
    # 6. 生年月日
    'birthday':         (None, True), # m_account.birthday DATE NOT NULL
    
    # --- m_address ---------------------------------------------
    # 7. 郵便番号
    'zip':              (7, True),    # m_address.zip CHAR(7) NOT NULL
    
    # 8. 都道府県
    'pref':             (10, True),   # m_address.pref VARCHAR(10) NOT NULL
    
    # 9. 市区町村
    'address1':         (20, True),   # m_address.address1 VARCHAR(20) NOT NULL
    
    # 10. 番地
    'address2':         (20, True),   # m_address.address2 VARCHAR(20) NOT NULL
    
    # 11. 建物名
    'address3':         (40, False),  # m_address.address3 VARCHAR(40) NULL
    
    # --- m_account (続き) --------------------------------------
    # 12. 電話番号
    'tel':              (20, True),   # m_account.tel VARCHAR(20) NOT NULL
                                      # (HTMLのmaxlength(11)よりDBが大きいので安全)
    # 13. 喫煙の有無
    'smoker':           (None, True), # m_account.smoker boolean NOT NULL
}

#入力フォーム確認-電話番号や住所
@login_bp.route("register_user/form_complete", methods=["POST"])
def registration_form_complete():

    # セッションにデータがなければ、フォームに戻す
    if 'registration_data' not in session:
        return redirect(url_for('login.show_register_user'))
    
    # 1. フォームからデータを取得
    form_data = request.form
    errors = {} # エラーメッセージを格納する辞書


    #文字数チェック
    #ADDRESS_SCHEMAに入っているmax_lengthを参考に比較する。
    
    # 2. バリデーションループ
    for name, (max_length, is_required) in ACCOUNT_SCHEMA.items():
        value = form_data.get(name)
        
        # --- 必須チェック ---
        if is_required and not value:
            # 「建物名」のように必須(False)でない項目は、
            # 未入力でもこのエラーを通過します。
            
            # (特殊ケース) 「喫煙の有無」は
            # HTMLで 'yes' が default checked なので、
            # 'smoker' が未入力になることは通常ありません。
            
            errors[name] = "この項目は必須です。"
            continue # 必須エラーなら文字数チェックはスキップ
            
        # --- 文字数チェック (値が入力されている場合のみ) ---
        if value:
            # max_length が None (DATE型など) の場合はチェックをスキップ
            if max_length is not None:
                if len(value) > max_length:
                    errors[name] = f"{max_length}文字以内で入力してください。"
    
    # (オプション) その他のカスタムバリデーション
    # (例：電話番号が本当に数字か？など)
    tel_value = form_data.get('tel')
    if tel_value and not tel_value.isdigit():
        errors['tel'] = "電話番号はハイフンなしの半角数字で入力してください。"


    # 3. バリデーション結果の確認
    if errors:
        # エラーがある場合：
        # フォームのページをエラーメッセージと共に「再表示」する
        # ※HTML側で errors[name] を表示する処理をする
        
        # register_form.html を再描画
        return render_template(
            'login/register_form.html', 
            errors=errors, 
            form_data=form_data # 入力値をフォームに復元するために渡す
        )
    
    # 4. バリデーション成功時
    else:
        # セッションにデータを保存する
        # (dict()で、不変なMultiDictから変更可能な通常の辞書に変換)
        session['registration_data'] = dict(form_data)
        
        # PRGパターン: 次のページ（電話番号認証）にリダイレクトする
        return redirect(url_for('login.show_phone_verification'))

    # return render_template('login/Phone_verification.html')

# 電話番号認証ページ（GET）
@login_bp.route("/phone_verification", methods=["GET"])
def show_phone_verification():
    if 'registration_data' not in session:
        # flash("セッションが切れました。もう一度入力してください。")
        return redirect(url_for('login.show_register_form')) # ★登録フォームのGETルート
        
    return render_template('login/Phone_verification.html')


#SMS確認
@login_bp.route("register_user/phone_auth", methods=["POST"])
def phone_auth():

    return render_template('login/identity_verification.html')


#SMS再送
@login_bp.route("register_user/phone_auth_resend", methods=["POST"])
def phone_auth_resend():

    return render_template('login/Phone_verification.html')

#本人確認-登録完了
@login_bp.route("register_user/verification", methods=["POST"])
def verification():

    return render_template('login/registration_complete.html')


#

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
    return render_template('login/forgot_password.html', error=error, success=success)




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
        return render_template('login/password_reset.html', error=error, success=success)

    else:
        # 実際にはここでDBにパスワードを更新
        success = "パスワードを更新しました。"

    return render_template('login/password_update.html', error=error, success=success)


# パスワード再設定画面の遷移
@login_bp.route('/forgot_password', methods=['POST'])
def forgot_password():

    return render_template('login/password_reset.html')


#メールアドレス忘れ画面の遷移
@login_bp.route('/forgot_email', methods=['GET'])
def forgot_email():


    return render_template('login/forgot_email.html')









