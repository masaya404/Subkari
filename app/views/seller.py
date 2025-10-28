from flask import Blueprint,render_template,request,make_response,redirect,url_for,jsonify,flash,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os
import base64
import io

seller_bp = Blueprint('seller',__name__,url_prefix='/seller')
# 処理方法：まず選択またはアップロードされたデータをsessionに保存され、最後にformatですべてのデータを一気にDBに登録 
#seller TOP画面表示----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller',methods=['GET'])
def seller():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
        
    resp = make_response(render_template('seller/seller_index.html', user_id = user_id))
    return resp

#seller フォーマット----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/format',methods=['GET'])
def seller_format():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')    
    return render_template('seller/seller_format.html', user_id = user_id)

#画像アップロード画面----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/uploadImg',methods=['GET'])
def seller_uploadImg():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
      
            
    return render_template('seller/seller_uploadImg.html', user_id = user_id)

#画像アップロード----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/upload',methods=['POST'])
def seller_upload():
    file = request.files.get('file')
    if not file:
        return render_template('seller/seller_format.html')
    
    filename = secure_filename(file.filename)
    savedata = datetime.now().strftime("%Y%m%d%H%M%S_")
    filename = savedata + filename
    
    #画像path生成 absolute_path
    current_filepath = os.path.abspath(__file__)
    current_dictionary = os.path.dirname(current_filepath)
    save_path = current_dictionary + "\\static\\img\\" + filename
    
    #画像保存
    image = Image.open(file)
    image.save(save_path,quality = 90)
    image_url = "/static/img/" + filename
    
    return jsonify({'success': True, 'image_url': image_url}) 

#画像アップロード----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/save-images', methods=['POST'])
def seller_save_images():
    if 'user_id' not in session:
        return jsonify({'success': False, 'error': 'ログインが必要です'}), 401
    
    data = request.get_json()
    images = data.get('images', [])
    
    if not images:
        return jsonify({'success': False, 'error': '画像がありません'}), 400
    
    saved_urls = []
    
    try:
        for img_data in images:
            # Base64 データを画像に変換
            base64_str = img_data['src'].split(',')[1]  # Data URL から Base64 部分を抽出
            image_bytes = base64.b64decode(base64_str)
            image = Image.open(io.BytesIO(image_bytes))
            
            # ファイル名生成
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{img_data['id']}.jpg"
            
            # パス生成と保存
            current_filepath = os.path.abspath(__file__)
            current_dictionary = os.path.dirname(current_filepath)
            save_path = os.path.join(current_dictionary, "static", "img", filename)
            
            image.save(save_path, quality=90)
            saved_urls.append(f"/static/img/{filename}")
        
        # session に保存
        session['uploaded_images'] = saved_urls
        
        return jsonify({'success': True, 'image_urls': saved_urls})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
#size選択----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/size',methods=['GET'])
def seller_size():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
               
    return render_template('seller/seller_size.html', user_id = user_id)

#size選択記録----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/size/success',methods=['POST'])
def seller_size_success():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
    size = request.form.get('size')
    # #flashはerror message , 自動的にsessionに保存され、get_flashed_messages()で内容を取得できる
    # if not size:
    #     flash("sizeの選択が必要です。")
    #     return redirect(url_for('seller.seller_size'))
    session['size'] = size
               
    return render_template('seller/seller_format.html', user_id = user_id)

#洗濯表示----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/clean',methods=['GET'])
def seller_clean():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
               
    return render_template('seller/seller_clean.html', user_id = user_id)

#洗濯表示記録----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/clean/success',methods=['POST'])
def seller_clean_success():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
    clean = request.form.get('clean')
    # #flashはerror message , 自動的にsessionに保存され、get_flashed_messages()で内容を取得できる
    # if not clean:
    #     flash("洗濯表示の選択が必要です。")
    #     return redirect(url_for('seller.seller_clean'))
    session['clean'] = clean
               
    return render_template('seller/seller_format.html', user_id = user_id)

#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con