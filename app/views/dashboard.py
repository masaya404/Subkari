from flask import Flask
from flask import render_template,Blueprint
import mysql.connector
#テストデータを入れての検証はまだ
#passの概念理解してない
#まだ未完成許して


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
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')



@admin_bp.route("/dashboard")
def dashboard():
    con=connect_db()
    cur=con.cursor(dictionary=True)

    #今週の新規ユーザー数を取得
    cur.execute("select * from v_weekly_new_users;")
    new_users=cur.fetchall()
    #新規ユーザーの先週比を取得
    cur.execute("select * from v_compare_1_week_ago_new_users;")
    users_compare=cur.fetchall()

    #今週の出品数を取得
    cur.execute("select * from v_weekly_listing;")
    weekly_listing=cur.fetchall()

    #出品数の先週比を取得
    cur.execute("select * from v_compare_1_week_ago_listing;")
    listing_compare=cur.fetchall()

    #WAUを取得
    cur.execute("select * from v_weekly_active_users;")
    WAU=cur.fetchall()

    #MAUを取得
    cur.execute("select * from v_monthly_active_users;")
    MAU=cur.fetchall()

    #通報の未対応件数を取
    cur.execute("select * from v_alert_unchecked;")
    alert_unchecked=cur.fetchall()

    #問い合わせの未対応件数を取得
    cur.execute("select * from v_inquiry_unchecked;")
    inquiry_unchecked=cur.fetchall()

    #本人確認依頼の件数を取得
    cur.execute("select * from v_identify_offer;")
    identify_offer=cur.fetchall()

    #6か月分の地域別新規ユーザー数
    cur.execute("select * from v_region_new_users;")
    region_new_users=cur.fetchone()

    #6か月分の年代別新規ユーザー数
    cur.execute("select * from v_age_group_new_users;")
    age_new_users=cur.fetchall()

    return render_template("dashboard.html",
                           new_users=new_users,
                           users_compare=users_compare,
                           weekly_listing=weekly_listing,
                           listing_compare=listing_compare,
                           WAU=WAU,
                           MAU=MAU,
                           alert_unchecked=alert_unchecked,
                           inquiry_unchecked=inquiry_unchecked,
                           identify_offer=identify_offer,
                           region_new_users=region_new_users,
                           age_new_users=age_new_users
                           )
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)       #デバッグモードの切り替え

