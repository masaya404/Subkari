from flask import Blueprint, render_template, request, make_response, redirect, url_for, session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
# import mysql.connector # データベース接続は使用しないためコメントアウト
import json
import os


# /app/views/top.py のファイルの先頭に追加
top_bp = Blueprint('top', __name__)



# =======================================================================
#  修正点: 50件のダミー商品データと画像パスを定義
# =======================================================================

# 50枚のダミー画像パスを定義 (static/img/product_01.jpg から product_50.jpg を想定)
IMAGE_PATHS = [f'product_{i:02d}.jpg' for i in range(1, 51)]

# 50件分のダミー商品データ (5列 x 10行 = 50件)
DUMMY_PRODUCTS = [
    {
        'id': i, 
        'brand': ['TRAVAS TOKYO', 'REFLEM', 'CIVARIZE', 'LIZ LISA', 'KINGLYMASK'][i % 5],
        'name': f'商品名サンプル {i:02d}',
        'price': 1500 + (i * 100) % 5000, 
        # 50個の異なる画像パスを使用
        'image_path': IMAGE_PATHS[i] 
    } 
    for i in range(40) 
]

# =======================================================================
# 訪客のtop page表示
# =======================================================================
@top_bp.route('/')
def guest_index():
    if 'user_id' in session:
        user_id = session.get('user_id')
        # エンドポイントは 'top.member_index'
        resp = make_response(redirect(url_for('top.member_index')))
    else :
        user_id = None
    
    resp = make_response(render_template('top/guest_index.html', user_id = user_id))
    return resp
    
# 会員のtop page表示
@top_bp.route('/top',methods=['GET'])
def member_index():
    if 'user_id' not in session:
        # エンドポイントは 'login.login'
        resp = make_response(url_for('login.login'))
        user_id = None
    else:
        user_id = session.get('user_id')
        
    resp = make_response(render_template('top/member_index.html', user_id = user_id))
    return resp

# subkariについての表示
@top_bp.route('/about_subkari', methods=['GET'])
def about_subkari():
    if 'user_id' in session:
        user_id = session.get('user_id')
    else :
        user_id = None
    
    resp = make_response(render_template('top/welcome_subkari.html', user_id = user_id))
    return resp

# 商品についての表示 (トップス)
@top_bp.route('/tops', methods=['GET'])
def tops():
    # =======================================================================
    #  修正点: DUMMY_PRODUCTSをテンプレートに渡すように変更
    # search_query も None で渡すことで全商品一覧として表示
    # =======================================================================
    context = {
        'search_query': None,
        'products': DUMMY_PRODUCTS # 50件のダミー商品を渡す
    }
    return render_template('top/search_product.html', **context)

# 商品についての表示 (ボトムス)
@top_bp.route('/bottoms', methods=['GET'])
def bottoms():
    # 商品の検索処理やデータベースのクエリを追加する
    # ダミーデータを渡す場合は上記 tops() と同様の処理が必要です
    return render_template('top/search_product.html', search_query=None, products=DUMMY_PRODUCTS)

# 商品についての表示 (アクセサリー)
@top_bp.route('/accessories', methods=['GET'])
def accessories():
    # DUMMY_PRODUCTSから全ての商品を渡す（フィルタリングなし）
    return render_template('top/search_product.html', search_query=None, products=DUMMY_PRODUCTS)

# コーディネート
@top_bp.route('/coordinate', methods=['GET'])
def coordinate():
    # DUMMY_PRODUCTSから全ての商品を渡す（フィルタリングなし）
    return render_template('top/search_product.html', search_query=None, products=DUMMY_PRODUCTS)


# 検索結果についての表示
@top_bp.route('/search', methods=['GET'])
def search():
    search_query: str = request.args.get('keyword', '')
    
    # 検索結果が空にならないよう、クエリに関わらずダミーを返す
    context = {
        'search_query': search_query,
        # 検索結果としてDUMMY_PRODUCTSの最初の数件を返すことで、動作確認を容易にする
        'products': DUMMY_PRODUCTS[:5] 
    }

    # 結果をHTMLに渡す
    return render_template('top/search_product.html', **context)


# 商品詳細についての表示
@top_bp.route('/product_details', methods=['GET'])
def product_details():
    if 'user_id' in session:
        user_id = session.get('user_id')
    else:
        user_id = None

    # 'top/search_product.html' テンプレートをレンダリング
    resp = make_response(render_template('products/search_product.html', user_id=user_id))
    return resp

# DB設定 (使用しないが元のコードに残す)
# def connect_db():
#     con=mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         passwd = '',
#         db ='db_subkari'
#     )
#     return con
