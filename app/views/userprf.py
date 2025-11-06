from flask import Blueprint , render_template ,request,make_response,redirect,url_for,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con
#------------------------------------------------------------------------------------------------------------------------------------------------------


# Blueprintの設定
userprf_bp = Blueprint('userprf', __name__, url_prefix='/userprf')


#userprf ユーザープロフィールを表示------------------------------------------------------
@userprf_bp.route("/<int:userprf_id>" )
def userprf(userprf_id):

    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('userprf_id')
    
    #user情報を取得
    user_info=get_user_info(user_id)
    evaluation,evaluationCount,follows,followers,products=get_transaction_info(user_id)
    #商品情報を取得
    productName,productImg=get_product_info(user_id)

    return render_template("userprf/userprf.html",evaluation=evaluation,evaluationCount=evaluationCount['評価件数'],follows=follows['フォロー数'],followers=followers['フォロワー数'],products=products['出品数'],productName=productName,productImg=productImg,user_info=user_info)


#--------------------------------------------------------------------------------------