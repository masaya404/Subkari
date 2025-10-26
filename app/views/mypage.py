from flask import Blueprint , render_template ,request,make_response,redirect,url_for,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

#mypageこういう名前のモジュール
mypage_bp = Blueprint('mypage', __name__, url_prefix='/mypage')

#@mypage_bp.route("mypage/ページまたは処理の名前")このようにかく　mypageはこのモジュールの名前
#render_template("mypage/ページのhtml名前")このようにかく　mypageはこのモジュールの名前

#userprfのページはmypageのモジュールにかくので、ここには不要
# mypage_bp = Blueprint('userprf', __name__, url_prefix='/userprf')


#マイページトップ表示--------------------------------------------------
@mypage_bp.route("mypage/mypage")
def mypage():

    
    return render_template("mypage/mypage.html")
#userprf表示--------------------------------------------------------------------
@mypage_bp.route("mypage/userprf")
def userprf():
    return render_template("mypage/mypage.html")

#editProfile表示--------------------------------------------------------------------
@mypage_bp.route("mypage/editProfile")
def editProfile():
    return render_template("mypage/editProfile.html")




この辺に書く？
# htmlの画面遷移url_for
# {{ url_for('モジュール名.関数名') }}
# {{ url_for('seller.seller_format') }}
# {{ url_for('mypage.mypage') }}
# {{ url_for('mypage.userprf') }}
