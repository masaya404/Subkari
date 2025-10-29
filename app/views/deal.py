from flask import Blueprint, render_template, request, make_response, redirect, url_for, current_app, session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import mysql.connector
import json
import os

deal_bp = Blueprint('deal', __name__, url_prefix='/deal')


# 取引TOP画面表示 ----------------------------------------------------------------------------------------------------------------------------------------------------------
@deal_bp.route('/deal', methods=['GET'])
def deal():
    # user検証成功
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
        
    return render_template('deal/deal_index.html', user_id = user_id)
# 取引一覧画面表示 ----------------------------------------------------------------------------------------------------------------------------------------------------------
@deal_bp.route('/deal/list', methods=['GET'])
def deal_list():
    # euser検証成功
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
        
    return render_template('deal/deal_detail.html', user_id = user_id)

# 取引詳細の画像添付 ----------------------------------------------------------------------------------------------------------------------------------------------------------
@deal_bp.route('/deal/list/imageUpload', methods=['GET','POST'])
def deal_list_imageUpload():
    # euser検証成功
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
    #アップロードと送信の判断
    if request.method == 'GET':
        return render_template('deal/deal_detail.html', 
                             upload_success=False, 
                             user_id=user_id)
        
    if 'img' not in request.files or not request.files['img'].filename:
        error = "ファイルが選択されていません"
        return render_template('deal/deal_detail.html', 
                             upload_success=False, 
                             error=error, 
                             user_id=user_id)
    
    #ここから    
    file = request.files['img']
    
    # 驗證文件類型
    ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'webp'}
    if not ('.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS):
        error = "許可されていないファイル形式です"
        return render_template('deal/deal_detail.html', 
                             upload_success=False, 
                             error=error, 
                             user_id=user_id)
    
    try:
        # システム用的画像名を生成
        filename = secure_filename(file.filename)
        savedata = datetime.now().strftime("%Y%m%d%H%M%S_")
        filename = savedata + filename
        
        # 保存パス生成
        # current_filepath = os.path.abspath(__file__)
        # current_dictionary = os.path.dirname(current_filepath)
        save_path = os.path.join(current_app.root_path, "static", "img", filename)
      
        # folder存在確保
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # 画像保存
        image = Image.open(file)
        image.save(save_path, quality=90)
        image_url = "/static/img/" + filename
        
        # Upload成功
        return render_template('deal/deal_detail.html', 
                             upload_success=True, 
                             image_url=image_url,
                             user_id=user_id)
    
    except Exception as e:
        error = f"ファイルの保存に失敗しました: {str(e)}"
        return render_template('deal/deal_detail.html', 
                             upload_success=False, 
                             error=error, 
                             user_id=user_id)    


