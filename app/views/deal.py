from flask import Blueprint, render_template, request, make_response, redirect, url_for, current_app, session,jsonify
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
    
     
        # DB接続
        con = connect_db()
        cur = con.cursor(dictionary=True)
        
        #  SQL 文章用意bought
        sql = """
            SELECT 
                p.*, 
                m.img,
                t.id,
                t.status,
                t.situation
            FROM 
                m_product AS p
            LEFT JOIN 
                m_productimg AS m 
            ON 
                p.id = m.product_id
            LEFT JOIN 
                t_transaction AS t 
            ON 
                p.id = t.product_id
            WHERE 
                t.customer_id = %s
            ORDER BY p.id ASC
            ;
            """   
        cur.execute(sql, (user_id,))
        bought_products = cur.fetchall()
       
        #  SQL 文章用意sell
        sql = """
            SELECT 
                p.*, 
                m.img,
                t.id,
                t.status,t.situation
            FROM 
                m_product AS p
            LEFT JOIN 
                m_productimg AS m 
            ON 
                p.id = m.product_id
            LEFT JOIN 
                t_transaction AS t 
            ON 
                p.id = t.product_id
            WHERE 
                p.account_id = %s
            AND
                p.draft = 0
            AND
                t.status IS NOT NULL
            GROUP BY p.id
            ;
            """   
        cur.execute(sql, (user_id,))
        products = cur.fetchall()
        cur.close()
        con.close()
        #出品商品の表示 products={product_id:2, customer_id:1, status:2, ...}
        
        
    return render_template('deal/deal_index.html', bought_products = bought_products, products = products, user_id = user_id)
# 取引一覧画面表示 ----------------------------------------------------------------------------------------------------------------------------------------------------------
@deal_bp.route('/deal/<int:transaction_id>', methods=['GET','POST'])
def deal_list(transaction_id):
    # euser検証成功
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
    #comment表示
    # DB接続
    con = connect_db()
    cur = con.cursor(dictionary=True)
    
    #  SQL 文章用意
    sql = """
        SELECT 
            t.*,
            p.*,
            m.img
        FROM 
            t_transaction AS t
        LEFT JOIN 
            m_product AS p
        ON
            t.product_id = p.id
        LEFT JOIN 
            m_productimg AS m
        ON
            t.product_id = m.product_id
        WHERE 
            t.id = %s
        LIMIT 1
        ;
        """
    cur.execute(sql, (transaction_id,))
    transaction = cur.fetchone()
    
    if not transaction:
        return redirect(url_for('deal.deal'))
    # comments
    product_id = transaction['product_id']
    sql = """
        SELECT content, createdDate, account_id
        FROM t_comments
        WHERE product_id = %s
        ORDER BY createdDate DESC
    """
    cur.execute(sql, (product_id,))
    comments = cur.fetchall()
    
    cur.close()
    con.close()   
    
    if transaction['status'] == '購入':
        charge = int(transaction['purchasePrice'])*0.1
        benefit = int(transaction['purchasePrice']) - charge
        transaction['charge'] = charge
        transaction['benefit'] = benefit
        
    else:
        charge = int(transaction['rentalPrice'])*0.1
        benefit = int(transaction['rentalPrice']) - charge
        transaction['charge'] = charge
        transaction['benefit'] = benefit
        
    print(transaction)
    
    return render_template('deal/deal_detail.html', transaction = transaction,comments = comments, user_id = user_id)

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
    
    # 画像検証
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

# comment ----------------------------------------------------------------------------------------------------------------------------------------------------------
@deal_bp.route('/comment', methods=['POST'])
def deal_comment():
    comment = request.form.get('comment')
    product_id = request.form.get('product_id')
    transaction_id = request.form.get('transaction_id')
    
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'ログインが必要です'}), 401
    
    user_id = session.get('user_id')
    
    if not comment or not product_id:
        return jsonify({'success': False, 'message': 'コメントと商品IDが必要です'}), 400
    
    try:
        con = connect_db()
        cursor = con.cursor()
        
        # DBに登録
        sql = """
            INSERT INTO t_comments (product_id, account_id, content, createdDate)
            VALUES (%s, %s, %s, NOW())
        """
        cursor.execute(sql, (product_id, user_id, comment))
        con.commit()
        
        cursor.close()
        con.close()
        
        return jsonify({
            'success': True,
            'message': 'メッセージを送信しました'
        }), 200
    
    except Exception as e:
        print(f'エラー: {str(e)}')
        return jsonify({
            'success': False,
            'message': f'エラー: {str(e)}'
        }), 500
#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con
