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
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')

    
    return render_template("mypage/mypage.html" , user_id=user_id)
# <<<<<<< HEAD
#------------------------------------------------------------------------------------------------

#userprf表示--------------------------------------------------------------------------------------
@mypage_bp.route("mypage/userprf")
def userprf():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    return render_template("mypage/mypage.html" , user_id=user_id)
#-------------------------------------------------------------------------------------------------

#editProfile プロフィール編集ページ表示--------------------------------------------------------------
@mypage_bp.route("/editProfile")
def editProfile():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    
    return render_template("mypage/editProfile.html" , user_id=user_id)

#--------------------------------------------------------------------------------------------------

#edit プロフィール編集-------------------------------------------------------------------------------
@mypage_bp.route("mypage/edit")
def edit():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    return render_template("mypage/edit.html" , user_id=user_id)


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
@mypage_bp.route("/transferAmount", methods=["GET", "POST"])
def transferAmount():
    error_message = None

    if request.method == "POST":
        amount_str = request.form.get("amount")

        if not amount_str:
            error_message = "金額を入力してください。"
        else:
            try:
                amount = int(amount_str)
                if amount < 0:
                    error_message = "金額は0円以上を入力してください。"
                elif amount > 1000000:
                    error_message = "一度に振り込める限度額は1,000,000円までです。"
                elif amount < 201:
                    error_message = "振込手数料200円を含め、最低201円以上を入力してください。"
            except ValueError:
                error_message = "正しい金額を入力してください。"

        if error_message:
            # 入力エラーがあれば同じページにエラーメッセージ付きで再表示
            return render_template("mypage/transferAmount.html", error_message=error_message)

        # ✅ 正常処理時はマイページ完了画面へリダイレクト
        return redirect(url_for('mypage.amountComp'))

    # ✅ GETアクセス時（初回表示）
    return render_template("mypage/transferAmount.html")


#---------------------------------------------------------------------------------------------------



#金額確定ページ------------------------------------------------------------------------------------
@mypage_bp.route("/mypage/amountComp")
def amountComp():
    return render_template("mypage/amountComp.html")
#---------------------------------------------------------------------------------------------------


#salesHistory 売上履歴------------------------------------------------------------------------------
@mypage_bp.route("/salesHistory")
def salesHistory():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    

    
    # try:
    #     conn = mysql.connector.connect(
    #         host="localhost",
    #         user="root",
    #         password="あなたのパスワード",
    #         database="db_subkari",   # ←実際のDB名に変更
    #         charset="utf8mb4"
    #     )
    #     cursor = conn.cursor(dictionary=True)

    #     # ログイン中のユーザーIDを使用する場合（例）
    #     user_id = session.get("user_id", 1)  # 仮で1番ユーザー

    #     # 売上履歴を取得（新しい順）
    #     sql = """
    #         SELECT id, type, DATE_FORMAT(date, '%%Y/%%m/%%d %%H:%%i') AS date, amount
    #         FROM sales_history
    #         WHERE user_id = %s
    #         ORDER BY date DESC
    #     """
    #     cursor.execute(sql, (user_id,))
    #     sales_list = cursor.fetchall()

    # except mysql.connector.Error as err:
    #     print("DBエラー:", err)
    #     sales_list = []
    # finally:
    #     cursor.close()
    #     conn.close()

    # HTMLへ渡す
    # return render_template("mypage/salesHistory.html", sales_list=sales_list)
    return render_template("mypage/salesHistory.html" ,  user_id=user_id)
#-------------------------------------------------------------------------------------------------



# htmlの画面遷移url_for
# {{ url_for('モジュール名.関数名') }}
# {{ url_for('seller.seller_format') }}
# {{ url_for('mypage.mypage') }}
# {{ url_for('mypage.userprf') }}
# >>>>>>> 3380b182aa575165ef27f84ca612b9c047078a8d
