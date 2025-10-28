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
    
    session['size1'] = request.form.get('size1')
    session['size2'] = request.form.get('size2')
    session['size3'] = request.form.get('size3')
    session['size4'] = request.form.get('size4')
    # #flashはerror message , 自動的にsessionに保存され、get_flashed_messages()で内容を取得できる
    # if not size:
    #     flash("sizeの選択が必要です。")
    #     return redirect(url_for('seller.seller_size'))
               
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

#セラーフォマットの内容をDB登録----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/format/submit',methods=['POST'])
def format_submit():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
    #メイｎ処理
    try:
            # フォームデータ取得
            product_name = request.form.get('productName', '').strip()
            rental = request.form.get('rental') == 'true'
            purchase = request.form.get('purchase') == 'true'
            rental_price = request.form.get('rentalPrice', 0) if rental else 0
            purchase_price = request.form.get('purchasePrice', 0) if purchase else 0
            smoking = request.form.get('smoking', 'no')
            color = request.form.get('color', '').strip()
            category = request.form.get('category', '').strip()
            brand = request.form.get('brand', '').strip()
            item_description = request.form.get('itemDescription', '').strip()
            product_description = request.form.get('productDescription', '').strip()
            return_location = request.form.get('returnLocation', '').strip()
            
            # session から取得
            size = session.get('size')
            washing = session.get('clean')
            
            # 画像データ取得
            images_json = request.form.get('images_data', '[]')
            images = json.loads(images_json)
            
            # バリデーション
            if not all([product_name, color, category, brand, size, washing, return_location]):
                flash('必須項目を入力してください', 'error')
                return render_template('seller/seller_format.html', user_id=user_id)
            
            if not (rental or purchase):
                flash('レンタル可能または購入可能を選択してください', 'error')
                return render_template('seller/seller_format.html', user_id=user_id)
            
            if not images:
                flash('最低1つの画像をアップロードしてください', 'error')
                return render_template('seller/seller_format.html', user_id=user_id)
            
            # DB に登録
            con = connect_db()
            cursor = con.cursor()
            
            try:
                # products テーブルに挿入
                query = """
                    INSERT INTO m_products 
                    (account_id, name, rentalPrice, purchasePrice, smokingFlg, color, 
                    category, brand, explanation , brand_id, 
                    size, cleanNotes, return_location, created_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
                """
                
                cursor.execute(query, (
                    user_id,
                    product_name,
                    rental,
                    purchase,
                    smoking,
                    color,
                    category,
                    brand,
                    item_description,
                    product_description,
                    size,
                    washing,
                    return_location
                ))
                
                product_id = cursor.lastrowid
                
                # 画像を保存
                for idx, img_data in enumerate(images):
                    try:
                        # Base64 データを画像ファイルに変換
                        src = img_data.get('src', '')
                        if ',' in src:
                            base64_str = src.split(',')[1]
                        else:
                            base64_str = src
                        
                        image_bytes = base64.b64decode(base64_str)
                        image = Image.open(io.BytesIO(image_bytes))
                        
                        # ファイル名: product_id.order (例: 1.1, 1.2, 1.3)
                        filename = f"{product_id}.{idx + 1}.jpg"
                        
                        # パス生成と保存
                        current_filepath = os.path.abspath(__file__)
                        current_directory = os.path.dirname(current_filepath)
                        save_dir = os.path.join(current_directory, "static", "img")
                        os.makedirs(save_dir, exist_ok=True)
                        
                        save_path = os.path.join(save_dir, filename)
                        image.save(save_path, quality=90)
                        
                        image_url = f"/static/img/{filename}"
                        
                        # product_images テーブルに挿入
                        query_img = """
                            INSERT INTO product_images (product_id, image_url, order_index)
                            VALUES (%s, %s, %s)
                        """
                        cursor.execute(query_img, (product_id, image_url, idx + 1))
                        
                    except Exception as e:
                        print(f"画像保存エラー: {e}")
                        continue
                
                con.commit()
                
                # session をクリア
                session.pop('uploadedImages', None)
                session.pop('size', None)
                session.pop('clean', None)
                
                return render_template('seller/seller_products.html', user_id=user_id)
                
            except Exception as e:
                con.rollback()
                print(f"DB エラー: {e}")
                flash('データベースへの登録に失敗しました', 'error')
                return render_template('seller/seller_format.html', user_id=user_id)
            
            finally:
                cursor.close()
                con.close()
        
    except Exception as e:
        print(f"エラー: {e}")
        flash('エラーが発生しました', 'error')
        return render_template('seller/seller_format.html', user_id=user_id)

    
#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con