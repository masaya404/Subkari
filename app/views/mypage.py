from flask import Blueprint , render_template ,request,make_response,redirect,url_for,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

#mypageこういう名前のモジュール
mypage_bp = Blueprint('mypage', __name__, url_prefix='/mypage')

# <<<<<<< HEAD
# =======
#@mypage_bp.route("mypage/ページまたは処理の名前")このようにかく　mypageはこのモジュールの名前
#render_template("mypage/ページのhtml名前")このようにかく　mypageはこのモジュールの名前

#userprfのページはmypageのモジュールにかくので、ここには不要
# mypage_bp = Blueprint('userprf', __name__, url_prefix='/userprf')
# >>>>>>> 3380b182aa575165ef27f84ca612b9c047078a8d


#マイページトップ表示-----------------------------------------------------------------------------
@mypage_bp.route("/mypage")
def mypage():

    
    return render_template("mypage/mypage.html")
# <<<<<<< HEAD
#------------------------------------------------------------------------------------------------

#userprf表示--------------------------------------------------------------------------------------
@mypage_bp.route("mypage/userprf")
def userprf():
    return render_template("mypage/mypage.html")
#-------------------------------------------------------------------------------------------------

#editProfile プロフィール編集ページ表示--------------------------------------------------------------
@mypage_bp.route("mypage/editProfile")
def editProfile():
    return render_template("mypage/editProfile.html")

#--------------------------------------------------------------------------------------------------

#edit プロフィール編集-------------------------------------------------------------------------------
@mypage_bp.route("mypage/edit")
def edit():
    return render_template("mypage/edit.html")
#---------------------------------------------------------------------------------------------------


#bankRegistration　振込口座登録ページ表示--------------------------------------------------------------
@mypage_bp.route("/bankRegistration")
def bankRegistration():
    return render_template("mypage/bankRegistration.html")
#----------------------------------------------------------------------------------------------------

#bankComplete' 振込口座登録完了ページ------------------------------------------------------------------
@mypage_bp.route("/bankComplete")
def bankComplete():
    return render_template("mypage/bankComplete.html")
#----------------------------------------------------------------------------------------------------


#bank_transfer 振込申請ページ表示---------------------------------------------------------------------
@mypage_bp.route("mypage/transferApplication")
def transferApplication():
    return render_template("mypage/transferApplication.html")
#---------------------------------------------------------------------------------------------------

#transferAmount 金額選択ページ表示--------------------------------------------------------------------
@mypage_bp.route("mypage/transferAmount")
def transferAmount():
    return render_template("mypage/transferAmount.html")
#---------------------------------------------------------------------------------------------------



# htmlの画面遷移url_for
# {{ url_for('モジュール名.関数名') }}
# {{ url_for('seller.seller_format') }}
# {{ url_for('mypage.mypage') }}
# {{ url_for('mypage.userprf') }}
# >>>>>>> 3380b182aa575165ef27f84ca612b9c047078a8d
