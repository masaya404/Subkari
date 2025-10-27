from flask import Flask
from flask import render_template,Blueprint
import mysql.connector


#DB設定------------------------------------------------------------------------------------------------------------------------------------------------------------------
def connect_db():
    con=mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '',
        db ='db_subkari'
    )
    return con


app=Flask(__name__)        #アプリケーションの大枠を生成

#ここわからない
account_manage_detail_bp = Blueprint('account', __name__, url_prefix='/account')




#アカウント詳細情報表示ページ ------------------------------------------------
@account_manage_detail_bp.route("/account/id:<id>_detail")
def account_manage_detail(id):
    sql=f'''
    select  
    ac.username as アカウント名 ,
    ac.fullname as 本名,
    ac.birthday as 生年月日,
    ac.mail as メールアドレス,
    ac.tel as 電話番号,
    concat(ac.pref,ad.address1+ad.address2,ad.address3) as 住所
    ac.created_at as  作成日時,
    max(l.logoutDatetime) as 最終ログイン時刻,
    ac.status as 状況                                      

    from m_account ac
    inner join t_login l  on ac.id=l.account_id
    inner join m_address ad on ac.id=ad.account_id

    where ac.id = {id} 
    ;
    '''
    con=connect_db()
    cur=con.cursor(dictionary=False)

    #アカウントの詳細情報取得 
    cur.execute(sql)
    user_info=cur.fetchall()
    return render_template("account_detail.html",user_info=user_info)


