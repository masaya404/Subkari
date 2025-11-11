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
    
    #取引資料の取得-------------------------------------------------------------
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
    
    session['transaction'] = transaction
    
    # commentsの取得
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
        
    # print(transaction)
    
    return render_template('deal/deal_detail.html', transaction = transaction,comments = comments, user_id = user_id)

# 出品者資料の取得--------------------------------------------------------------------------------------------------------------------------------------------------------------
@deal_bp.route('/seller_data/get',methods=['GET'])
def get_seller_data():
    id = session.get('transaction', {}).get('account_id')
    try:
        seller_data = get_seller_info(id)
    
        return jsonify({'success':True,
                    'data':seller_data})

    except Exception as e:
        print(f'Error: {str(e)}')
        return jsonify({'success': False, 'message': str(e)}), 500

#商品の出品者資料--------------------------------------------------
def get_seller_info(id):
    con = connect_db()
    cur = con.cursor(dictionary=True)

    #firstName identifyImg status smoker evaluation total
    sql = """
            SELECT 
                a.firstName,
                a.identifyImg,
                a.status,
                a.smoker,
                COUNT(e.id) as evaluation_count,
                ROUND(AVG(e.score),1) as average_score
            FROM m_account a
            LEFT JOIN t_evaluation e
            ON a.id = e.recipient_id
            WHERE a.id=%s
            GROUP BY a.id           
        """
    cur.execute(sql,(id,))
    result = cur.fetchone()
    cur.close()
    con.close()
    
    return result    
     
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
    
    transaction = session.get('transaction')
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
                             user_id=user_id,
                             transaction = transaction)
    
    except Exception as e:
        error = f"ファイルの保存に失敗しました: {str(e)}"
        return render_template('deal/deal_detail.html', 
                             upload_success=False, 
                             error=error, 
                             user_id=user_id)    

# comment ----------------------------------------------------------------------------------------------------------------------------------------------------------
# 既に存在するcommentsの取り処理
@deal_bp.route('/get-comments', methods=['GET'])
def get_comments():
    # transaction_id = request.args.get('transaction_id')
    # user検証
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
        
    product_id = request.args.get('product_id')
    
    if not product_id:
        return jsonify({'success': False, 'message': 'transaction_id が必要です'}), 400
    
    try:
        con = connect_db()
        cur = con.cursor(dictionary=True)
        
        # t_commentsにいるコメント
        sql = """
            SELECT 
                t.account_id,
                t.content,
                t.createdDate,
                t.product_id,
                a.firstName
            FROM t_comments t
            LEFT JOIN m_account a
            ON t.account_id = a.id
            WHERE t.product_id = %s
            ORDER BY t.createdDate DESC
        """
        cur.execute(sql, (product_id,))
        comments = cur.fetchall()
       
        cur.close()
        con.close()
        
        # datetimeを文字列に変換しないとjsonが読めない
        comments_list = []
        for comment in comments:
            comments_list.append({
                'account_id': comment['account_id'],
                'firstName': comment['firstName'] or '匿名',  # 名前がなければ
                'content': comment['content'],
                'createdDate': comment['createdDate'].isoformat() if comment['createdDate'] else None  #date型→str
            })
        return jsonify(comments_list), 200
    
    except Exception as e:
        print(f'Error getting comments: {str(e)}')
        return jsonify({'success': False, 'message': str(e)}), 500


# 新しい comment　提出
@deal_bp.route('/add-comment', methods=['POST'])
def add_comment():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'ログインが必要です'}), 401
    
    user_id = session.get('user_id')
    data = request.get_json()
    
    product_id = data.get('product_id')
    content = data.get('content', '').strip()
    
    if not content:
        return jsonify({'success': False, 'message': 'コメントを入力してください'}), 400
    
    try:
        con = connect_db()
        cur = con.cursor()
        
        #  comment　→　DB
        sql = """
            INSERT INTO t_comments ( product_id, account_id, content, createdDate)
            VALUES ( %s, %s, %s, %s)
        """
        
        cur.execute(sql, (
            product_id,
            user_id,
            content,
            datetime.now()
        ))
        
        con.commit()
        comment_id = cur.lastrowid    #AUTO INCREMENTの値を取得
        
        cur.close()
        con.close()
        
        return jsonify({
            'success': True,
            'message': 'コメントを送信しました',
            'comment_id': comment_id
        }), 200
    
    except Exception as e:
        print(f'Error adding comment: {str(e)}')
        return jsonify({'success': False, 'message': str(e)}), 500


# @deal_bp.route('/comment', methods=['POST'])
# def deal_comment():
#     comment = request.form.get('comment')
#     product_id = request.form.get('product_id')
#     transaction = session.get('transaction')
#     print(product_id)
#     if 'user_id' not in session:
#         return jsonify({'success': False, 'message': 'ログインが必要です'}), 401
    
#     user_id = session.get('user_id')
    
#     if not comment and not product_id:
#         return jsonify({'success': False, 'message': 'コメントと商品IDが必要です'}), 400
    
#     try:
#         con = connect_db()
#         cursor = con.cursor()
        
#         # DBに登録
#         sql = """
#             INSERT INTO t_comments (product_id, account_id, content, createdDate)
#             VALUES (%s, %s, %s, NOW())
#         """
#         cursor.execute(sql, (product_id, user_id, comment))
#         con.commit()
        
#         cursor.close()
#         con.close()
        
#         return jsonify({
#             'success': True,
#             'message': 'メッセージを送信しました',
#             'transactin':transaction
#         }), 200
    
#     except Exception as e:
#         print(f'エラー: {str(e)}')
#         return jsonify({
#             'success': False,
#             'message': f'エラー: {str(e)}'
#         }), 500
#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con
