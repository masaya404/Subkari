from flask import Blueprint,render_template,request,make_response,session, redirect, url_for
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

products_bp = Blueprint('products',__name__,url_prefix='/products')

# 検索結果についての表示 (商品一覧) ------------------------------------------------------------------------------------------------------------------------------------------
@products_bp.route('/search_result', methods=['GET'])
def search_result():
    user_id = session.get('user_id')
    products = [] 
    
    # DBに接続し、商品取得
    con = None
    try:
        con = connect_db()
        cur = con.cursor(dictionary=True) # 辞書形式で取得
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
        user_id = user_id, 
        products=products 
    ))
    return resp
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 商品詳細の表示 (product_details) ---------------------------------------------------------------------------------------------------------------------------------------
# 💡 修正点1: URLルーティングに商品IDのプレースホルダーを追加
@products_bp.route('/<int:product_id>', methods=['GET']) # ルートを /products/<int:product_id> に修正
def product_details_stub(product_id): # product_idを引数として受け取る
    # sessionからuser_idを取得
    user = session.get('user_id')
    
    result = None
    comments = [] # コメントリストを初期化
    con = None
    
    try:
        con = connect_db()
        cur = con.cursor(dictionary=True) 
        
        # 1. 商品情報の取得 (result)
        sql = "SELECT name, rentalPrice, purchasePrice, explanation FROM m_product WHERE id = %s;"
        cur.execute(sql, (product_id,))
        result = cur.fetchone() 

        # 2. コメント情報のダミーデータ生成 (実際はDBから取得)
        comments = [
            {'user_name': '中村 輝', 'text': 'コメント失礼します。購入を検討しているのですが、こちらの商品の使用期間はどれくらいでしょうか？', 'is_seller': False},
            {'user_name': '谷口 昌哉', 'text': '商品の使用期間ですね。約○年間（または○か月間）使用しました。', 'is_seller': True},
        ]
        
    except mysql.connector.Error as err:
        print(f"データベースエラー: {err}")

    finally:
        if con and con.is_connected():
            cur.close()
            con.close()
            
    # 商品が見つからなかった場合のデフォルト処理 (エラー回避のため)
    if not result:
        result = {
            'name': '商品が見つかりません', 
            'rentalPrice': '¥0', 
            'purchasePrice': '¥0', 
            'explanation': '該当する商品IDのデータは存在しませんでした。'
        }
    
    # 💡 修正点: 取得した商品情報 (result) とコメント (comments) をテンプレートに渡す
    resp = make_response(render_template(
        'products/product_details.html', 
        user=user, 
        result=result, 
        comments=comments
    ))
    return resp

#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con