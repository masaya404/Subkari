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
    sql = "SELECT * FROM user WHERE mail = %s;"
    con=connect_db()
    cur=con.cursor(dictionary=True)
    cur.execute(sql,(account['mail'],))
    # ここで確認
    userExist = cur.fetchone()
    #ユーザーが存在しないまたはパスワードが一致しない
    if not userExist or userExist['password'] != account['password']:
        error_message['password'] = "メールアドレスまたはパスワードが正しくありません。"
        return render_template('login/login.html',account=account,error_message = error_message)
    
    #登録成功の処理
    session['user_id'] = userExist['mail']

    return redirect(url_for('top.member_index'))
    
#Logout--------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/login/logout',methods=['GET'])
def logout():
    session.pop('user_id', None)
    return render_template('top/guest_index.html')

#Register-------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/register_user',methods=['GET'])
def register_user():
    account = {}
    etbl ={}
    return render_template('login/register_user.html',account=account,etbl=etbl)

#Register確認----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/register_user/complete',methods=['POST'])
def register_user_complete():
    account = request.form
    error = "を入力してください。"
    etbl={}
    stbl={"ID":"ID","password":"パスワード"}
    #入力確認
    ecnt =0
    for key,value in account.items():
        if not value:
            ecnt+=1
            etbl[key] = stbl[key] + error
    if ecnt !=0:
        return render_template('login/register_user.html',etbl=etbl,account=account)
      
    
    
    #同一user確認    
    sql = "SELECT * FROM user WHERE userid = %s;"
    con=connect_db()
    cur=con.cursor(dictionary=True)
    cur.execute(sql,(account['ID'],))
    userSame = cur.fetchone()    
    if userSame:
        etbl['ID'] = "このIDは既に使用されています。"
        return render_template('register_user.html',etbl = etbl,account=account)

    if account['authority']  == "管理者":
        authority = 0
    else:
        authority = 1   
    #DBに登録
    user = (account['ID'],account['password'],authority)
    sql = "INSERT INTO user (userid,password,authority) VALUES(%s,%s,%s)"
    cur.execute(sql,user)  
    con.commit()
    cur.close()
    con.close()

    return render_template('login/register_user_complete.html',account = account)

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
