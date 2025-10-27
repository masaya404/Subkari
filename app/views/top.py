from flask import Blueprint,render_template,request,make_response,redirect,url_for,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

top_bp = Blueprint('top',__name__)

#sessionの中にuserの登録状態を確認し、ゲストまたはメンバーのtop pageに遷移する
#訪客のtop page表示--------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/')
def guest_index():
    #sessionの登録資料確認
    if 'user_id' in session:
        user_id = session.get('user_id')
        resp = make_response(redirect(url_for('top.member_index')))
    else :
        user_id = None
    
    resp = make_response(render_template('top/guest_index.html', user_id = user_id))
    return resp
    
#会員のtop page表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/top',methods=['GET'])
def member_index():
    #sessionの登録資料確認   
    if 'user_id' not in session:
        resp = make_response(url_for('login.login'))
        user_id = None
    else:
        user_id = session.get('user_id')
        
    resp = make_response(render_template('top/member_index.html', user_id = user_id))
    return resp

#subkariについての表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/about_subkari', methods=['GET'])
def about_subkari():
    # sessionからuser_idを取得
    if 'user_id' in session:
        user_id = session.get('user_id')
    else :
        user_id = None
    
    # 'top/welcome_subkari.html' テンプレートをレンダリング
    resp = make_response(render_template('top/welcome_subkari.html', user_id = user_id))
    return resp
#検索結果についての表示-----------------------------------------------------------------------------------------------------------------------------------------------------------


# ... (connect_db 関数は省略)
#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con