from flask import Blueprint, render_template, request, make_response, session, redirect, url_for
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import mysql.connector
import json
import os

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
        sql_product = "SELECT name,account_id, rentalPrice, purchasePrice, explanation, image_path, thumbnail1, thumbnail2, thumbnail3 FROM m_product WHERE id = %s;"
        cur.execute(sql_product, (product_id,))
        product = cur.fetchone()

        #商品が見つからない場合の処理
        # 商品が見つからなかった場合のデフォルト処理
        if not product:
            product = {
                'name': '商品が見つかりません',
                'rentalPrice': '¥0',
                'purchasePrice': '¥0',
                'explanation': '該当する商品IDのデータは存在しませんでした。',
                'image_path': 'default.jpg',  # 画像がない場合のデフォルト画像を設定
                'thumbnail1': 'default_thumbnail1.jpg',
                'thumbnail2': 'default_thumbnail2.jpg',
                'thumbnail3': 'default_thumbnail3.jpg'
            }


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

    

    # 取得した商品情報 (product) とコメント (comments) をテンプレートに渡す
    resp = make_response(render_template(
        'products/product_details.html',
        user_id=user_id,
        product=product,
        comments=comments
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
