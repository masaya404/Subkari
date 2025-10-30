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
#アカウントの口座情報を取得する ------------------------------------------------------------------------------
def getAccountInfo():
    accountNumbers=[]                 #口座番号下位三桁を格納
    id=session["user_id"]
    editmode=session["editmode"]
    con=connect_db()
    cur=con.cursor(dictionary=True)
    sql="select bankName,accountNumber,branchCode from t_transfer  where account_id=%s limit 3"
    cur.execute(sql,(id,))
    bank_info=cur.fetchall()
    cur.close()
    con.close()
    count=0
    #口座がいくつ登録されているかを数える
    for i in bank_info:
        count+=1

    #口座番号マスク処理のために口座番号の桁数と下位三桁を抽出し配列に入れる
    for i in range(count):
        num=int(bank_info[i]['accountNumber'])

        tmp=num
        length=0
        mask=""
        #口座番号の桁数を取得
        while tmp>0:
            tmp=tmp//10
            length+=1
        for i in range(length-3):
        
            mask+="*"

        num=str(num%1000)
        num=mask+num                #マスク処理を施した口座番号
        accountNumbers.append(num)
    return bank_info,accountNumbers,count

#ユーザー情報を取得する ------------------------------------------------------------------------------------
#引数として受け取ったidを持つユーザーの情報を取得
def get_user_info(id):
    sql = "SELECT * FROM m_account WHERE id = %s"
    con = connect_db()
    cur = con.cursor(dictionary=True)
    cur.execute(sql, (id,))  # ← タプルで渡す！
    user_info = cur.fetchone()
    return user_info

#mypageこういう名前のモジュール
mypage_bp = Blueprint('mypage', __name__, url_prefix='/mypage')



#マイページトップ表示-----------------------------------------------------------------------------
@mypage_bp.route("/mypage")
def mypage():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')

    
    
    #アカウントテーブルからユーザー情報を取得
    user_info=get_user_info(user_id)

    #アカウントテーブルからは取れない情報を取得
    con = connect_db()
    cur = con.cursor(dictionary=True)
      
    #フォロワー数、フォロー数、評価、総評価件数、出品数を取得
    #フォロー数
    sql="select count(*) from t_connection where execution_id=%s and type='フォロー' group by execution_id"
    cur.execute(sql, (user_id,))
    follows=cur.fetchone()
    #フォロワー数
    sql="select count(*) from t_connection where target_id=%s and type='フォロー' group by target_id"
    cur.execute(sql, (user_id,))
    followers=cur.fetchone()
    #評価
    sql="select avg(score) from t_evaluation where recipient_id=%s group by recipient_id"
    cur.execute(sql, (user_id,))
    evaluation=cur.fetchone()
    #総評価件数
    sql="select count(*) from t_evaluation where recipient_id=%s group by recipient_id"
    cur.execute(sql, (user_id,))
    evaluationCount=cur.fetchone()
    #出品数
    sql="select count(*) from m_product where account_id=%s"
    cur.execute(sql, (user_id,))
    products=cur.fetchone()

    #評価を変形
    evaluation=round(float(evaluation))     #小数点型にしてから四捨五入
    


    return render_template("mypage/mypage.html",image_path=user_info['identifyImg'],evaluation=evaluation,evaluationCount=evaluationCount,follows=follows,followers=followers,products=products,user_info=user_info)
    
    
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
    
    #user情報を取得
    user_info=get_user_info(user_id)

    return render_template("mypage/editProfile.html",smoker=user_info['smoker'],username=user_info['username'],introduction=user_info['introduction'])

#updateProfile プロフィール更新--------------------------------------------------------------
@mypage_bp.route("/updateProfile",methods=['POST'])
def updateProfile():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
    #更新内容を取得
    new_profile=request.form   #username,smoker,introduction
    print(new_profile)
    id=session['user_id']

    #dbに更新をかける 
    con = connect_db()
    cur = con.cursor(dictionary=True)
    sql="update m_account set username=%s,smoker=%s,introduction=%s where id=%s"
    cur.execute(sql,(new_profile['username'],new_profile['smoker'],new_profile['introduction'],id))
    con.commit()
    cur.close()
    con.close()

    #更新後のユーザー情報を取得 
    user_info=get_user_info(id)

    return render_template("mypage/editProfile.html",smoker=user_info['smoker'],username=user_info['username'],introduction=user_info['introduction'])

    


#--------------------------------------------------------------------------------------------------

#edit プロフィール編集-------------------------------------------------------------------------------
@mypage_bp.route("/edit")
def edit():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')

    #ユーザー情報を取得
    user_info=get_user_info(user_id)

    
    # image_path = result["identifyImg"] if result else None
    # smoker = result["smoking"] if result and "smoking" in result else 0

    return render_template("mypage/edit.html", username=user_info['username'],  smoker=user_info['smoker'],introduction=user_info['introduction'])
    

#---------------------------------------------------------------------------------------------------


#bankRegistration　振込口座登録ページ表示--------------------------------------------------------------
@mypage_bp.route("/bankRegistration")
def bankRegistration():

    #登録されている口座数を取得
    bank_count=0
    id=session["user_id"]
    con=connect_db()
    cur=con.cursor(dictionary=True)

    sql="select count(*) as 登録数 from t_transfer t inner join m_account a on t.account_id=a.id where a.id=%s group by a.id"
    cur.execute(sql,(id,))
    
    bank_count=cur.fetchone()
    if bank_count==None:
        bank_count=0
    else:
        bank_count=int(bank_count["登録数"])
    
    
    cur.close()
    con.close()
    #3件すでに登録済みなら拒否する
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
    #空欄確認
    for key,value in bank_info.items():
        if not value:
            ecnt+=1
    #空欄あり、登録できない      
    if ecnt !=0:
        return render_template('mypage/bankRegistration.html')
    
    #既に登録されていないか調べる 
    id=session["user_id"]
    sql="select * from t_transfer  where (account_id=%s) and (branchCode=%s) and (accountNumber=%s)"
    con=connect_db()
    cur=con.cursor(dictionary=True)
    cur.execute(sql,(id,bank_info['branchCode'],bank_info['accountNumber']))
    bankSame=cur.fetchone()

    #登録されているのでエラー
    if bankSame is not None:
        return render_template('mypage/bankRegistration.html')
    
    accountHolder=bank_info['famillyName']+bank_info['firstName']
    #登録処理

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
    session["editmode"]=False
    bank_info,accountNumbers,count=getAccountInfo()
    editmode=session["editmode"]
    return render_template("mypage/transferApplication.html",bank_info=bank_info,accountNumbers=accountNumbers,count=count,editmode=editmode)
#---------------------------------------------------------------------------------------------------
#transferApplication 削除ボタン表示 -----------------------------------------------------------------
@mypage_bp.route("/transferApplication")
def editActivate():
    editmode=session["editmode"]
    if not editmode:
        session["editmode"]=True
    else:
        session["editmode"]=False
    editmode=session["editmode"]
    bank_info,accountNumbers,count=getAccountInfo()
   
    
    return render_template("mypage/transferApplication.html",bank_info=bank_info,accountNumbers=accountNumbers,count=count,editmode=editmode)

#transferApplication 登録口座削除 -------------------------------------------------------------------
@mypage_bp.route("/transferApplication/removeBank",methods=['POST'])
def removeBank():
    #何番目が選択されたかを取得
    bank_id = request.form.get("bank_id") 

    id=session["user_id"]
    sql="select * from t_transfer  where account_id=%s"
    con=connect_db()
    cur=con.cursor(dictionary=True)
    cur.execute(sql,(id,))
    target=cur.fetchall()
    #選択された口座のidを取得
    target_id=target[int(bank_id)]["id"]

    #削除
    sql="delete from t_transfer where id=%s"
    cur.execute(sql,(target_id,))
    con.commit()
    cur.close()
    con.close()
    bank_info,accountNumbers,count=getAccountInfo()
    editmode=session["editmode"]
    
    return render_template("mypage/transferApplication.html",bank_info=bank_info,accountNumbers=accountNumbers,count=count,editmode=editmode)


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

#振込履歴-----------------------------------------------------------------------------------------
@mypage_bp.route("/transferHistory")
def transferHistory():
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
    return render_template("mypage/transferHistory.html" ,  user_id=user_id)
#------------------------------------------------------------------------------------------------

# htmlの画面遷移url_for
# {{ url_for('モジュール名.関数名') }}
# {{ url_for('seller.seller_format') }}
# {{ url_for('mypage.mypage') }}
# {{ url_for('mypage.userprf') }}
# >>>>>>> 3380b182aa575165ef27f84ca612b9c047078a8d
