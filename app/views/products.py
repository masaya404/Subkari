from flask import Blueprint,render_template,request,make_response,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

products_bp = Blueprint('products',__name__,url_prefix='/products')

# 検索結果についての表示 (商品一覧) ------------------------------------------------------------------------------------------------------------------------------------------
@products_bp.route('/products.show_list', methods=['GET']) # ★ URLを /search_result に変更
def search_result(): # ★ 関数名を変更
    user_id = session.get('user_id')
    products = [] 
    
    # DBに接続し、商品取得
    sql = "SELECT id, name, brand, price, image_path FROM m_product LIMIT 50;" 
    con=connect_db()
    cur=con.cursor()
    cur.execute(sql)
    products=cur.fetchall() 
    cur.close()
    con.close()
    
    # 'top/search_product.html' テンプレートをレンダリングし、商品リストを渡す
    resp = make_response(render_template(
        'top/search_product.html', 
        user_id = user_id, 
        products=products 
    ))
    return resp


# 検索結果についての表示 (旧: product_details) --------------------------------------------------------------------------------------------------------------------------
# ★ 修正: search_resultと競合しないよう、product_details_stubとして残します
@products_bp.route('/products.product_details', methods=['GET'])
def product_details_stub():
    # sessionからuser_idを取得
    if 'user' in session:
        user = session.get('user_id')
    else :
        user = None
    
    resp = make_response(render_template('top/search_product.html', user = user))
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