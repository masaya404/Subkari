from flask import Blueprint,render_template,request,make_response,redirect,url_for,jsonify,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

seller_bp = Blueprint('seller',__name__,url_prefix='/seller')

#seller TOP画面表示----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller',methods=['GET'])
def seller():
    if 'user_id' not in session:
        resp = make_response(url_for('login.login'))
        user_id = None
        
    else:
        user_id = session.get('user_id')
        
    resp = make_response(render_template('seller/seller_index.html', user_id = user_id))
    return resp

#seller フォーマット----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/format',methods=['GET'])
def seller_format():
    if 'user_id' not in session:
        resp = make_response(url_for('login.login'))
        user_id = None
    
    else:
        user_id = session.get('user_id')    
    return render_template('seller/seller_format.html', user_id = user_id)

#seller フォーマット画像アップロード----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/uploadImg',methods=['GET'])
def seller_uploadImg():
    if 'user_id' not in session:
        resp = make_response(url_for('login.login'))
        user_id = None
    
    else:
        user_id = session.get('user_id')
        file = request.files.get('file')
        if not file:
            return jsonify({'error': 'No file'}), 400
        
        # filename = secure_filename(file.filename)
        # filepath = os.path.join(app.config['UPLOAD_FOLDER'], f"{int(time.time())}_{filename}")
        # file.save(filepath)
        
    # return jsonify({'success': True, 'path': filepath})
            
    return render_template('seller/seller_uploadImg.html', user_id = user_id)




















#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con