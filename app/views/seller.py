from flask import Blueprint,render_template,request,make_response,redirect,url_for,jsonify,flash,current_app,session
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
@seller_bp.route('/seller/format',methods=['GET','POST'])
def seller_format():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
        
    # POST ：保存
    if request.method == 'POST':
        save_form_data_to_session(request.form)
    
    # 取得
    form_data = get_form_data_from_session()
    
    return render_template('seller/seller_format.html', 
                         user_id=user_id, 
                         form_data=form_data)    
    # return render_template('seller/seller_format.html', user_id = user_id)

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
    
    # 使用 current_app.root_path
    save_dir = os.path.join(current_app.root_path, "static", "img")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, filename)
    
    #画像path生成 absolute_path
    # current_filepath = os.path.abspath(__file__)
    # current_dictionary = os.path.dirname(current_filepath)
    # save_path = current_dictionary + "\\static\\img\\" + filename
    
    #画像保存
    try:
        image = Image.open(file)
        image.save(save_path,quality = 90)
        image_url = "/static/img/" + filename      
        return jsonify({'success': True, 'image_url': image_url})
     
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
#画像アップロード----------------------------------------------------------------------------------------------------------------------------------------------------------
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
            base64_str = img_data['src'].split(',')[1]
            image_bytes = base64.b64decode(base64_str)
            image = Image.open(io.BytesIO(image_bytes))
            
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{img_data['id']}.jpg"
            
            save_dir = os.path.join(current_app.root_path, "static", "img")
            os.makedirs(save_dir, exist_ok=True)
            save_path = os.path.join(save_dir, filename)
            
            image.save(save_path, quality=90)
            saved_urls.append(f"/static/img/{filename}")
        
        session['uploaded_images'] = saved_urls
        session.modified = True
        
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

#size選択を記録----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/size/success',methods=['POST'])
def seller_size_success():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
    
    size_field = ['shoulderWidth', 'bodyWidth', 'sleeveLength', 'bodyLength','notes']
    # size_list = [request.form.get(s, '') for s in size_field]
    
    # size_list.append(request.form.get('shoulderWidth'))
    # size_list.append(request.form.get('bodyWidth'))
    # size_list.append(request.form.get('sleeveLength'))
    # size_list.append(request.form.get('bodyLength'))
    size_data = {s: request.form.get(s, '') for s in size_field}
    session['size_selected'] = size_data 
    # session['shoulderWidth'] = request.form.get('shoulderWidth')
    # session['bodyWidth'] = request.form.get('bodyWidth')
    # session['sleeveLength'] = request.form.get('sleeveLength')
    # session['bodyLength'] = request.form.get('bodyLength')
    
    # #flashはerror message , 自動的にsessionに保存され、get_flashed_messages()で内容を取得できる
    # if not size:
    #     flash("sizeの選択が必要です。")
    #     return redirect(url_for('seller.seller_size'))
    #  format 画面遷移
    return redirect(url_for('seller.seller_format'))
               
    # return render_template('seller/seller_format.html', user_id = user_id )
    
#サイズ記録----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/get_size_selected')
def get_size_selected():
    return jsonify(session.get('size_selected', {}))
#洗濯表示----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/clean',methods=['GET'])
def seller_clean():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
    #cleanの辞書型データを確認し、なければ{}
    selected = session.get('clean_selected', {})
    
    return render_template('seller/seller_clean.html', selected=selected, user_id=user_id)           
    # return render_template('seller/seller_clean.html', user_id = user_id)

#洗濯表示記録----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/clean/success',methods=['POST'])
def seller_clean_success():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
     
    #  保存セッション
    save_form_data_to_session(request.form)
    
    #取ってきたデータを辞書型で保存
    session['clean_selected'] = request.form.to_dict()
    session.modified = True
    return redirect(url_for('seller.seller_format'))          
    # return render_template('seller/seller_format.html', user_id = user_id)

#洗濯表示記録----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/get_clean_selected')
def get_clean_selected():
    return jsonify(session.get('clean_selected', {}))

#セラーフォマットの内容をDB登録----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/format/submit',methods=['POST'])
def format_submit():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
    #メイｎ処理
    # return render_template('seller/seller_products.html', user_id=user_id)
    try:
            # フォームデータ取得
            product_name = request.form.get('productName', '').strip()
            rental = request.form.get('rental') == 'true'
            purchase = request.form.get('purchase') == 'true'
            rentalPrice = request.form.get('rentalPrice', 0) if rental else 0
            purchasePrice = request.form.get('purchasePrice', 0) if purchase else 0
            smoking = request.form.get('smoking', 'no')
            color = request.form.get('color', '').strip()
            category = request.form.get('category', '').strip()
            brand = request.form.get('brand', '').strip()
            item_description = request.form.get('itemDescription', '').strip()
            product_description = request.form.get('productDescription', '').strip()
            return_location = request.form.get('returnLocation', '').strip()
            
            # sessionのサイズ取得
            shoulder_width = session.get('shoulderWidth', '')
            body_width = session.get('bodyWidth', '')
            sleeve_length = session.get('sleeveLength', '')
            body_length = session.get('bodyLength', '')
            size_notes = session.get('notes', '')
            
           # サイズをDBに保存
            sql = """
            INSERT INTO sizes (shoulderWidth, bodyWidth, sleeveLength, bodyLength, notes)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (shoulder_width, body_width, sleeve_length, body_length, size_notes))
            db.commit()
        
            #sessionの洗濯表示取得
            clean_selected = session.get('clean_selected', {})
            #column名
            columns = ['wash','bleach','tumble','dry','iron','dryclean','wet']
            #value名
            values = [clean_selected.get(col) for col in columns]

            # 洗濯表示のSQL
            sql_clean = f"""
            INSERT INTO cleaning (user_id, {', '.join(columns)})
            VALUES (%s, {', '.join(['%s']*len(columns))})
            """
            cursor.execute(sql_clean, [user_id] + values)
            db.commit()
            
            # # session から取得
            # size = session.get('size')
            # washing = session.get('clean')
            
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

#出品一覧画面----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/products',methods=['GET'])
def seller_products():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')

            
    return render_template('seller/seller_products.html', user_id = user_id)

#下書き一覧画面----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/seller/draft',methods=['GET'])
def seller_draft():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
      
            
    return render_template('seller/seller_draft.html', user_id = user_id)  
 
#データセンター覧画面----------------------------------------------------------------------------------------------------------------------------------------------------------
@seller_bp.route('/datacenter',methods=['GET'])
def datacenter():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
      
            
    return render_template('seller/seller_datacenter.html', user_id = user_id)

#セッション記録----------------------------------------------------------------------------------------------------------------------------------------------------------
def save_form_data_to_session(form_data):
    """保存session"""
    session['productName'] = form_data.get('productName', '')
    session['rental'] = form_data.get('rental') == 'true'  # checkbox  'true'
    session['purchase'] = form_data.get('purchase') == 'true'
    session['rentalPrice'] = form_data.get('rentalPrice','')
    session['purchasePrice'] = form_data.get('purchasePrice','')
    session['smoking'] = form_data.get('smoking', 'no')
    session['color'] = form_data.get('color', '')
    session['category'] = form_data.get('category', '')
    session['brand'] = form_data.get('brand', '')
    session['itemDescription'] = form_data.get('itemDescription', '')
    session['productDescription'] = form_data.get('productDescription', '')
    session['returnLocation'] = form_data.get('returnLocation', '')
    session.modified = True

def get_form_data_from_session():
    """ session 取得"""
    return {
        'productName': session.get('productName', ''),
        'rental': session.get('rental', False),
        'purchase': session.get('purchase', False),
        'rentalPrice':session.get('rentalPrice',''),
        'purchasePrice':session.get('purchasePrice',''),
        'smoking': session.get('smoking', 'no'),
        'color': session.get('color', ''),
        'category': session.get('category', ''),
        'brand': session.get('brand', ''),
        'itemDescription': session.get('itemDescription', ''),
        'productDescription': session.get('productDescription', ''),
        'returnLocation': session.get('returnLocation', '')
    }
   
#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con