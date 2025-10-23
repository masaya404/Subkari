from flask import Blueprint , render_template ,request,make_response,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


#Login画面表示----------------------------------------------------------------------------------------------------------------------------------------------------------
@auth_bp.route('/login',methods=['GET'])
def login():
    #errorメッセージ
    etbl={}
    account={}
      
    return render_template('auth/login.html',etbl=etbl,account=account)

#Login確認--------------------------------------------------------------------------------------------------------------------------------------------------------------
@auth_bp.route('/login/auth',methods=['POST'])
def login_auth():
    account = request.form
    ecnt = 0
    data = {}
    error = "を入力してください。"
    etbl={}
    stbl={"ID":"ID","password":"パスワード"}
    
    for key,value in account.items():
        if not value:
            ecnt+=1
            etbl[key] = stbl[key] + error
    if ecnt !=0:
        return render_template('auth/login.html',etbl=etbl,account=account)
    
    sql = "SELECT * FROM user WHERE userid = %s;"
    con=connect_db()
    cur=con.cursor(dictionary=True)
    cur.execute(sql,(account['ID'],))
    # 入力した資料がデータベースに存在するかどうかを確認
    userExist = cur.fetchone()
    #ユーザーが存在しない　、　パスワードが間違い 
    if not userExist or userExist['password'] != account['password']:
        etbl['ID'] = "IDまたはパスワードが間違がっています。"
        return render_template('login.html',etbl = etbl,account=account)
    
    session['ID'] = account['ID']
    session['authority'] = userExist['authority']
    return render_template('index.html',user = session.get('ID'),authority = session.get('authority'))
    
#Logout--------------------------------------------------------------------------------------------------------------------------------------------------------------
@auth_bp.route('/logout',methods=['GET'])
def logout():
    session.pop('user', None)
    session.pop('authority', None)
    session.clear()
    return render_template('auth/index.html')

#Register-------------------------------------------------------------------------------------------------------------------------------------------------------------
@auth_bp.route('/register_user',methods=['GET'])
def register_user():
    account = {}
    etbl ={}
    return render_template('auth/register_user.html',account=account,etbl=etbl)

#Register確認----------------------------------------------------------------------------------------------------------------------------------------------------------
@auth_bp.route('/register_user/complete',methods=['POST'])
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
        return render_template('auth/register_user.html',etbl=etbl,account=account)
    
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

    return render_template('auth/register_user_complete.html',account = account)

#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con
