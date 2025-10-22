from flask import Blueprint,render_template,request,make_response,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

top_bp = Blueprint('top',__name__,url_prefix='/top')

#Products表示-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/top',methods=['GET'])
def show_list():   

    username = request.cookies.get('username')

    return render_template('products/products.html',products = products ,authority = session.get('authority'),username=username)

#Products詳細-----------------------------------------------------------------------------------------------------------------------------------------------------------
@top_bp.route('/products/<scode>',methods=['GET'])
def product_detail(scode):
    username = request.cookies.get('username')
    #user確認
    if 'ID' in session:
    #商品資料を取得    
        sql = "SELECT * FROM lunch WHERE scode= %s;"
        con = connect_db()
        cur = con.cursor(dictionary=True)
        cur.execute(sql,(scode,))
        result = cur.fetchone()
        cur.close()
        con.close()
        
        return render_template('products/product_detail.html',result = result,username=username)
    
    else:
        return render_template('index.html',username=username)


#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='py23db'
    )
    return con