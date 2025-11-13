from flask import Flask, render_template, Blueprint
import mysql.connector

app = Flask(__name__)

brand_serach_bp = Blueprint('brand_serach', __name__, url_prefix='/brand')


# DB接続初期設定
def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        db='db_subkari'
    )
    return con


# TRAVASTOKYOのページ
@brand_serach_bp.route('/TRAVASTOKYO')
def TRAVASTOKYO():

    # DB接続
    con = connect_db()
    cur = con.cursor(dictionary=True)

    cur.execute("""
        select brand_id
        from m_products
        where brand_id = 1
    """)

    rows = cur.fetchall()

    cur.close()
    con.close()


    return render_template('brand/TRAVASTOKYO.html', rows=rows)

