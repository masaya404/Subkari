from flask import Blueprint , render_template ,request,make_response,redirect,url_for,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os


mypage_bp = Blueprint('mypage', __name__, url_prefix='/mypage')
mypage_bp = Blueprint('userprf', __name__, url_prefix='/userprf')


#マイページトップ表示--------------------------------------------------
@mypage_bp.route("/mypage.mypage")
def mypage():

    
    return render_template("mypage/mypage.html")
#--------------------------------------------------------------------


この辺に書く？