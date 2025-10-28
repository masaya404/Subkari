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
    bank_count=0
    #三件すでに登録済みなら拒否する
    user_id=session["user_id"]
    con=connect_db()
    cur=con.cursor(dictionary=True)

    sql="select count(*) as 登録数 from t_transfer t inner join m_account a on t.account_id=a.id where a.mail=%s group by a.mail"
    cur.execute(sql,(user_id,))
    
    bank_count=cur.fetchone()
    bank_count=int(bank_count["登録数"])
    if bank_count>=3:
        return render_template("mypage/mypage.html")

    return render_template("mypage/bankRegistration.html")
#----------------------------------------------------------------------------------------------------

#bankComplete' 振込口座登録完了ページ------------------------------------------------------------------
@mypage_bp.route("/bankComplete",methods=['POST'])
def bankComplete():
    #エラーチェック
    #error回数とメッセージ
    ecnt = 0
    error_message={}
    bank_info=request.form    #name,accountType,branchCode,accountNumber,firstName,famillyName
    print(bank_info)
    #空欄確認
    for key,value in bank_info.items():
        if not value:
            ecnt+=1
    #空欄あり、登録できない      
    if ecnt !=0:
        return render_template('mypage/bankRegistration.html')
    
    #既に登録されていないか調べる 
    user_id=session["user_id"]
    sql="select * from t_transfer t inner join m_account a on t.account_id=a.id where (a.mail=%s) and (t.branchCode=%s) and (t.accountNumber=%s)"
    con=connect_db()
    cur=con.cursor(dictionary=True)
    cur.execute(sql,(user_id,bank_info['branchCode'],bank_info['accountNumber']))
    userSame=cur.fetchone()

    #登録されているのでエラー
    if userSame is not None:
        return render_template('mypage/bankRegistration.html')
    
    accountHolder=bank_info['famillyName']+bank_info['firstName']
    #登録処理
    #account_idを取得
    sql="select id from m_account where mail=%s limit 1"
    cur.execute(sql,(user_id,))
    user_info=cur.fetchone()
    id=user_info["id"]

    #データを追加
    sql="INSERT INTO t_transfer (account_id,bankName,accountType,branchCode,accountNumber,accountHolder) VALUES(%s,%s,%s,%s,%s,%s)"
    cur.execute(sql, (id,bank_info['name'],bank_info['accountType'],bank_info['branchCode'],bank_info['accountNumber'],accountHolder))          #アカウントidがわからない
    con.commit()
    cur.close()
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



@mypage_bp.route("/mypage/amountComp")
def amountComp():
    return render_template("mypage/amountComp.html")



# htmlの画面遷移url_for
# {{ url_for('モジュール名.関数名') }}
# {{ url_for('seller.seller_format') }}
# {{ url_for('mypage.mypage') }}
# {{ url_for('mypage.userprf') }}
# >>>>>>> 3380b182aa575165ef27f84ca612b9c047078a8d
