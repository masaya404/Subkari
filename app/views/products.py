from flask import Blueprint, render_template, request, make_response, session, redirect, url_for
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import mysql.connector
import json
import os

#プロフィールに表示する取引情報を取得する ------------------------------------------------------------------------------------
#引数として受け取ったidを持つユーザーの情報を取得
def get_transaction_info(id):
    #アカウントテーブルからは取れない情報を取得
    con = connect_db()
    cur = con.cursor(dictionary=True)
      
    #フォロワー数、フォロー数、評価、総評価件数、出品数を取得
    #フォロー数
    sql="select count(*) as フォロー数 from t_connection where execution_id=%s and type='フォロー' group by execution_id"
    cur.execute(sql, (id,))
    follows=cur.fetchone()
    #フォロワー数
    sql="select count(*) as フォロワー数 from t_connection where target_id=%s and type='フォロー' group by target_id"
    cur.execute(sql, (id,))
    followers=cur.fetchone()
    #評価
    sql="select avg(score) as 評価 from t_evaluation where recipient_id=%s group by recipient_id"
    cur.execute(sql, (id,))
    evaluation=cur.fetchone()
    #総評価件数
    sql="select count(*) as 評価件数 from t_evaluation where recipient_id=%s group by recipient_id"
    cur.execute(sql, (id,))
    evaluationCount=cur.fetchone()
    #出品数
    sql="select count(*) as 出品数 from m_product where account_id=%s"
    cur.execute(sql, (id,))
    products=cur.fetchone()
    #評価を変形
    evaluation=round(float(evaluation['評価']))     #小数点型にしてから四捨五入
   
    return evaluation,evaluationCount


#引数として受け取ったidを持つユーザーの情報を取得
def get_user_info(id):
    sql = "SELECT * FROM m_account WHERE id = %s"
    con = connect_db()
    cur = con.cursor(dictionary=True)
    cur.execute(sql, (id,))  # ← タプルで渡す！
    user_info = cur.fetchone()
    return user_info




# Blueprintの設定
products_bp = Blueprint('products', __name__, url_prefix='/products')

# 商品一覧の表示
@products_bp.route('/search_result', methods=['GET'])
def search_result():
    user_id = session.get('user_id')
    products = []

    # DBに接続して商品情報を取得
    con = None
    try:
        con = connect_db()
        cur = con.cursor(dictionary=True)  # 辞書形式で取得
        sql = "SELECT id, name, brand, price, image_path FROM m_product LIMIT 50;"
        cur.execute(sql)
        products = cur.fetchall()
        cur.close()
    except mysql.connector.Error as err:
        print(f"DB Error: {err}")
    finally:
        if con and con.is_connected():
            con.close()

    # 'top/search_product.html' テンプレートをレンダリングし、商品リストを渡す
    resp = make_response(render_template(
        'top/search_product.html',
        user_id=user_id,
        products=products
    ))
    return resp

# 商品詳細の表示
@products_bp.route('/<int:product_id>', methods=['GET'])
def product_details_stub(product_id):
    # sessionからuser_idを取得
    user_id = session.get('user_id')

    product = None
    comments = []  # コメントリストを初期化
    con = None
    cur = None

    try:
        con = connect_db()
        cur = con.cursor(dictionary=True)

        # 商品情報を取得
        sql_product = "SELECT name,account_id, rentalPrice, purchasePrice, explanation FROM m_product WHERE id = %s;"
        cur.execute(sql_product, (product_id,))
        product = cur.fetchone()
        print(product)

        #商品が見つからない場合の処理
        # 商品が見つからなかった場合のデフォルト処理
        # ... 省略 ...
        if not product:

            
            # 商品が見つからない場合は、エラーページや404を返すのが適切です
            return render_template('error.html'), 404 # **ここで関数を終了させる**

        # if not product:
        #     product = {
        #         'name': '商品が見つかりません',
        #         'rentalPrice': '¥0',
        #         'purchasePrice': '¥0',
        #         'explanation': '該当する商品IDのデータは存在しませんでした。',
        #         'image_path': 'default.jpg',  # 画像がない場合のデフォルト画像を設定
        #         'thumbnail1': 'default_thumbnail1.jpg',
        #         'thumbnail2': 'default_thumbnail2.jpg',
        #         'thumbnail3': 'default_thumbnail3.jpg'
        #     }


        # コメント情報を取得
        # 2. コメントデータと投稿者名を取得
        # t_comments と m_account を結合し、投稿日時の降順で取得
        sql_comments = """
            SELECT 
                t.content AS text, 
                m.username AS user_name, 
                t.account_id AS comment_acouunt_id,
                t.createdDate

            FROM 
                t_comments t
            JOIN 
                m_account m ON t.account_id = m.id
            WHERE 
                t.product_id = %s
            ORDER BY 
                t.createdDate ASC;
        """

        cur.execute(sql_comments, (product_id,))
        fetched_comments = cur.fetchall()

        
        # 3. HTMLテンプレートに渡す形式にデータを整形
        # 商品の出品者IDと比較して、出品者かどうかを判定するフラグを追加
        seller_id = product['account_id'] # m_productから取得した出品者のaccount_id
        
        for comment in fetched_comments:
            is_seller = (comment['comment_acouunt_id'] == seller_id)
            
            # テンプレートに渡すコメントリストに追加
            comments.append({
                'user_name': comment['user_name'],
                'text': comment['text'],
                'is_seller': is_seller,
                # 日付も表示したい場合はここで整形して渡すことも可能
                'created_date': comment['createdDate'].strftime('%Y/%m/%d %H:%M') if comment['createdDate'] else ''
            })
        # comments = [
        #     {'user_name': '中村 輝', 'text': 'コメント失礼します。購入を検討しているのですが、こちらの商品の使用期間はどれくらいでしょうか？', 'is_seller': False},
        #     {'user_name': '谷口 昌哉', 'text': '商品の使用期間ですね。約○年間（または○か月間）使用しました。', 'is_seller': True},
        # ]

    except mysql.connector.Error as err:
        print(f"データベースエラー: {err}")

    finally:
        if con and con.is_connected():
            cur.close()
            con.close()



    # 評価情報を取得
    evaluation, evaluationCount = get_transaction_info(product['account_id'])

    #アカウント情報取得
    seller_info = get_user_info(product['account_id'])
    

    # 取得した商品情報 (product) とコメント (comments) をテンプレートに渡す
    resp = make_response(render_template(
        'products/product_details.html',
        evaluationCount=evaluationCount['評価件数'],
        user_id=user_id,
        seller_info=seller_info,
        product=product,
        comments=comments,
        evaluation=evaluation
    ))
    return resp
#purchase
@products_bp.route('/purchase', methods=['GET'])
def purchase():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    return render_template("purchase/purchase.html",user_id = user_id)

# DB接続設定
def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        db='db_subkari'
    )
    return con
