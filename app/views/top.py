from flask import Blueprint,render_template,request,make_response,redirect,url_for,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os
# /app/views/top.py のファイルの先頭に追加
top_bp = Blueprint('top',__name__)

#sessionの中にuserの登録状態を確認し、ゲストまたはメンバーのtop pageに遷移する
#訪客のtop page表示--------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/')
def guest_index():
    #sessionの登録資料確認
    if 'user_id' in session:
        user_id = session.get('user_id')
        resp = make_response(redirect(url_for('top.member_index')))
    else :
        user_id = None
    
    resp = make_response(render_template('top/guest_index.html', user_id = user_id))
    return resp
    
#会員のtop page表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/top',methods=['GET'])
def member_index():
    #sessionの登録資料確認   
    if 'user_id' not in session:
        resp = make_response(url_for('login.login'))
        user_id = None
    else:
        user_id = session.get('user_id')
        
    resp = make_response(render_template('top/member_index.html', user_id = user_id))
    return resp

#subkariについての表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/about_subkari', methods=['GET'])
def about_subkari():
    # sessionからuser_idを取得
    if 'user_id' in session:
        user_id = session.get('user_id')
    else :
        user_id = None
    
    # 'top/welcome_subkari.html' テンプレートをレンダリング
    resp = make_response(render_template('top/welcome_subkari.html', user_id = user_id))
    return resp
#検索結果についての表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
from flask import Blueprint,render_template,request,make_response,redirect,url_for,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os
# /app/views/top.py のファイルの先頭に追加
top_bp = Blueprint('top',__name__)

#sessionの中にuserの登録状態を確認し、ゲストまたはメンバーのtop pageに遷移する
#訪客のtop page表示--------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/')
def guest_index():
    #sessionの登録資料確認
    if 'user_id' in session:
        user_id = session.get('user_id')
        resp = make_response(redirect(url_for('top.member_index')))
    else :
        user_id = None
    
    resp = make_response(render_template('top/guest_index.html', user_id = user_id))
    return resp
    
#会員のtop page表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/top',methods=['GET'])
def member_index():
    #sessionの登録資料確認   
    if 'user_id' not in session:
        resp = make_response(url_for('login.login'))
        user_id = None
    else:
        user_id = session.get('user_id')
        
    resp = make_response(render_template('top/member_index.html', user_id = user_id))
    return resp

#subkariについての表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/about_subkari', methods=['GET'])
def about_subkari():
    # sessionからuser_idを取得
    if 'user_id' in session:
        user_id = session.get('user_id')
    else :
        user_id = None
    
    # 'top/welcome_subkari.html' テンプレートをレンダリング
    resp = make_response(render_template('top/welcome_subkari.html', user_id = user_id))
    return resp

#商品についての表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/coordinate', methods=['GET'])
def coordinate():
    # 商品の検索処理やデータベースのクエリを追加する
    return render_template('top/search_product.html')

@top_bp.route('/tops', methods=['GET'])
def tops():
    # 商品の検索処理やデータベースのクエリを追加する
    return render_template('top/search_product.html')

@top_bp.route('/bottoms', methods=['GET'])
def bottoms():
    # 商品の検索処理やデータベースのクエリを追加する
    return render_template('top/search_product.html')

@top_bp.route('/accessories', methods=['GET'])
def accessories():
    # 商品の検索処理やデータベースのクエリを追加する
    return render_template('top/search_product.html')



#検索結果についての表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/search', methods=['GET'])
def search():
    search_query: str = request.args.get('keyword', '') # 型ヒントを追加
    
    # -------------------------------------------------------------------
    # NameErrorを回避するための修正: データベース検索処理をコメントアウトし、ダミーデータを使用
    # -------------------------------------------------------------------
    
    # products = Product.query.filter(Product.name.ilike(f'%{search_query}%')).all()
    
    # エラー回避のため、代わりにダミーのリストを作成
    # 実際には、Productモデルを正しくインポートする必要があります
    
    # 💡 修正点: DummyProductの定義を関数のスコープ内に移動し、正しくインデント
    class DummyProduct:
        def __init__(self, name):
            self.name = name
            self.id = 1
            self.price = 1000
            # --- テンプレートで必要な属性を追加 ---
            self.image_path = 'dummy_product.jpg'  
            # ------------------------------------
            # テンプレートに必要な他の属性をここに追加できます

    # 検索クエリに基づいたダミーの結果を生成
    if search_query:
        products = [
            DummyProduct(f"検索された商品: {search_query} A"),
            DummyProduct(f"検索された商品: {search_query} B")
        ]
    else:
        products = [
            DummyProduct("全ての商品 1"),
            DummyProduct("全ての商品 2")
        ]
        
    # -------------------------------------------------------------------

    # 結果をHTMLに渡す
    return render_template('top/search_product.html', search_query=search_query, products=products)




#検索結果についての表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/product_details', methods=['GET'])
def product_details():
    # sessionからuser_idを取得
    if 'user_id' in session:
        user_id = session.get('user_id')
    else:
        user_id = None

    # 'top/search_product.html' テンプレートをレンダリング
    resp = make_response(render_template('products/search_product.html', user_id=user_id))
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