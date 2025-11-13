from flask import Blueprint, render_template, request, make_response, session, redirect, url_for
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import mysql.connector
import json
import os



# Blueprintの設定
products_bp = Blueprint('products', __name__, url_prefix='/products')


#プロフィールに表示する取引情報を取得する ------------------------------------------------------------------------------------
#引数として受け取ったidを持つユーザーの情報を取得
def get_transaction_info(id):
    #アカウントテーブルからは取れない情報を取得
    con = connect_db()
    cur = con.cursor(dictionary=True)
      
    #フォロワー数、フォロー数、評価、総評価件数、出品数を取得
    #フォロー数
    sql="select count(*) as フォロー数 from t_connection where execution_id=%s and type='フォロー' group by execution_id"
    cur.execute(sql, (id,))
    follows=cur.fetchone()
    #フォロワー数
    sql="select count(*) as フォロワー数 from t_connection where target_id=%s and type='フォロー' group by target_id"
    cur.execute(sql, (id,))
    followers=cur.fetchone()
    #評価
    sql="select avg(score) as 評価 from t_evaluation where recipient_id=%s group by recipient_id"
    cur.execute(sql, (id,))
    evaluation=cur.fetchone()
    #総評価件数
    sql="select count(*) as 評価件数 from t_evaluation where recipient_id=%s group by recipient_id"
    cur.execute(sql, (id,))
    evaluationCount=cur.fetchone()
    #出品数
    sql="select count(*) as 出品数 from m_product where account_id=%s"
    cur.execute(sql, (id,))
    products=cur.fetchone()
    #評価を変形
    if evaluation is not None:
        evaluation=round(float(evaluation['評価']))     #小数点型にしてから四捨五入
    else:
        evaluation = 0
        evaluationCount = {"評価件数":0}
    return evaluation,evaluationCount


#引数として受け取ったidを持つユーザーの情報を取得
def get_user_info(id):
    sql = "SELECT * FROM m_account WHERE id = %s"
    con = connect_db()
    cur = con.cursor(dictionary=True)
    cur.execute(sql, (id,))  # ← タプルで渡す！
    user_info = cur.fetchone()
    return user_info



#アカウントの口座情報を取得する ------------------------------------------------------------------------------
def getAccountInfo():
    accountNumbers=[]                 #口座番号下位三桁を格納
    id=session["user_id"]
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

#商品情報を取得する ------------------------------------------------------------------------------------
def get_product_info(product_id):
    try:
        con = connect_db()
        cur = con.cursor(dictionary=True)

        # 商品情報を取得
        sql_product = """
        SELECT 
        pr.name as product_name,
        pr.account_id, 
        pr.rentalPrice, 
        pr.purchasePrice, 
        pr.explanation ,
        pr.color,
        pr.for,
        pr.category_id,
        pr.brand_id ,
        br.name as brand_name  , 
        ca.name as category_name
        

        FROM m_product pr
        INNER JOIN m_brand br ON br.id = pr.brand_id
        INNER JOIN m_category ca ON pr.category_id = ca.id
        WHERE pr.id = %s;
        """
        cur.execute(sql_product, (product_id,))
        product = cur.fetchone()
        return product
    except mysql.connector.Error as err:
        print(f"データベースエラー: {err}")
        return None
    finally:
        if con and con.is_connected():
            cur.close()
            con.close()


    

# 商品一覧の表示
@products_bp.route('/search_result', methods=['GET'])
def search_result():
    user_id = session.get('user_id')
    products = []

    # DBに接続して商品情報を取得
    con = None
    try:
        con = connect_db()
        cur = con.cursor(dictionary=True)  # 辞書形式で取得
        sql = "SELECT id, name, brand, price, image_path FROM m_product LIMIT 50;"
        cur.execute(sql)
        products = cur.fetchall()
        cur.close()
    except mysql.connector.Error as err:
        print(f"DB Error: {err}")
    finally:
        if con and con.is_connected():
            con.close()

    # 'top/search_product.html' テンプレートをレンダリングし、商品リストを渡す
    resp = make_response(render_template(
        'top/search_product.html',
        user_id=user_id,
        products=products
    ))
    return resp

# 商品詳細の表示
@products_bp.route('/<int:product_id>', methods=['GET'])
def product_details_stub(product_id):
    # sessionからuser_idを取得
    user_id = session.get('user_id')

    product = None
    comments = []  # コメントリストを初期化
    con = None
    cur = None

    try:
        con = connect_db()
        cur = con.cursor(dictionary=True)

        # 商品情報を取得
        sql_product = """
        SELECT pr.id ,pr.name as product_name,pr.account_id, pr.rentalPrice, pr.purchasePrice, pr.explanation ,pr.color,pr.for,pr.category_id,pr.brand_id ,br.name as brand_name  , ca.name as category_name
        FROM m_product pr
        INNER JOIN m_brand br ON br.id = pr.brand_id
        INNER JOIN m_category ca ON pr.category_id = ca.id
        WHERE pr.id = %s;
        """
        cur.execute(sql_product, (product_id,))
        product = cur.fetchone()
        print(product)

        #商品が見つからない場合の処理
        # 商品が見つからなかった場合のデフォルト処理
        # ... 省略 ...
        if not product:

            
            # 商品が見つからない場合は、エラーページや404を返すのが適切です
            return render_template('error.html'), 404 # **ここで関数を終了させる**

        #--レンタル期間情報を取得--
        sql_rentalPeriod = """
        SELECT rentalPeriod
        from t_rentalPeriod
        where product_id = %s;

        """

        cur.execute(sql_rentalPeriod, (product_id,))
        rentalPeriod = cur.fetchall()

        # 1. レンタル単価を取得（数値型に変換）
        try:
            # product.rentalPrice は文字列の可能性もあるため、int型に変換
            rental_price_per_day = int(product['rentalPrice'])
        except (TypeError, ValueError):
            # エラーハンドリング: 価格が不正な場合は0としておくなど
            rental_price_per_day = 0
            
        # 2. 期間ごとの合計金額を計算し、辞書として保存する
        calculated_prices = {}

        for period_data in rentalPeriod:
            # rentalPeriodから期間（日）を取得
            # キー名はSQLの SELECT rentalPeriod から 'rentalPeriod' になる
            try:
                #データを入れるperiod_stringに      
                period_string = period_data['rentalPeriod']
                # '日' という文字を空文字に置き換え（例: '4日' -> '4'）
                days_str = period_string.replace('日', '')

                days = int(days_str)
                
                # 計算
                total_price = rental_price_per_day * days
                
                # 結果を辞書に追加
                # 例: {'4日': 4000, '7日': 7000} のように格納
                calculated_prices[f'{days}日'] = total_price
                
            except (TypeError, ValueError):
                # 期間のデータが不正な場合はスキップ
                continue

        # コメント情報を取得
        # 2. コメントデータと投稿者名を取得
        # t_comments と m_account を結合し、投稿日時の降順で取得
        sql_comments = """
            SELECT 
                t.content AS text, 
                m.username AS user_name, 
                t.account_id AS comment_acouunt_id,
                t.createdDate

            FROM 
                t_comments t
            JOIN 
                m_account m ON t.account_id = m.id
            WHERE 
                t.product_id = %s
            ORDER BY 
                t.createdDate ASC;
        """

        cur.execute(sql_comments, (product_id,))
        fetched_comments = cur.fetchall()

        
        # 3. HTMLテンプレートに渡す形式にデータを整形
        # 商品の出品者IDと比較して、出品者かどうかを判定するフラグを追加
        seller_id = product['account_id'] # m_productから取得した出品者のaccount_id
        
        for comment in fetched_comments:
            is_seller = (comment['comment_acouunt_id'] == seller_id)
            
            # テンプレートに渡すコメントリストに追加
            comments.append({
                'user_name': comment['user_name'],
                'text': comment['text'],
                'is_seller': is_seller,
                # 日付も表示したい場合はここで整形して渡すことも可能
                'created_date': comment['createdDate'].strftime('%Y/%m/%d %H:%M') if comment['createdDate'] else ''
            })

        #トップサイズ情報を取得
        sql_topSize ="""
        SELECT
        shoulderWidth ,bodyWidth , sleeveLength , bodyLength , notes
        from
        m_topsSize
        where
        product_id = %s;
        """
        cur.execute(sql_topSize, (product_id,))
        topSize = cur.fetchone()


        #ボトムスサイズ情報を取得
        sql_bottomsSize = """
        SELECT
        hip 
        , totalLength 
        , rise 
        , inseam 
        , waist 
        , thighWidth 
        , hemWidth 
        , skirtLength
        , notes

        from
        m_bottomsSize

        where
        product_id = %s;
        """
        cur.execute(sql_bottomsSize, (product_id,))
        bottomsSize = cur.fetchone()


       
    except mysql.connector.Error as err:
        print(f"データベースエラー: {err}")

    finally:
        if con and con.is_connected():
            cur.close()
            con.close()



    # 評価情報を取得
    evaluation, evaluationCount = get_transaction_info(product['account_id'])

    #アカウント情報取得
    seller_info = get_user_info(product['account_id'])
    

    # 取得した商品情報 (product) とコメント (comments) をテンプレートに渡す
    resp = make_response(render_template(
        'products/product_details.html',
        evaluationCount=evaluationCount['評価件数'],
        user_id=user_id,
        seller_info=seller_info,
        product=product,
        comments=comments,
        calculated_prices = calculated_prices,
        evaluation=evaluation,
        topSize=topSize,
        bottomsSize=bottomsSize
    ))
    return resp
#purchase
@products_bp.route('/purchase/<int:product_id>', methods=['GET'])
def purchase(product_id):
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')

    #DBから情報を取得
    try:
        con = connect_db()
        cur = con.cursor(dictionary=True)

        # 商品情報を取得
        sql_product = """
        SELECT pr.id , pr.name as product_name,pr.account_id, pr.rentalPrice, pr.purchasePrice, pr.explanation ,pr.color,pr.for,pr.category_id,pr.brand_id ,br.name as brand_name  , ca.name as category_name
        FROM m_product pr
        INNER JOIN m_brand br ON br.id = pr.brand_id
        INNER JOIN m_category ca ON pr.category_id = ca.id
        WHERE pr.id = %s;
        """
        cur.execute(sql_product, (product_id,))
        product = cur.fetchone()
        #配送情報を取得

        sql_address="""
        SELECT id,zip,pref,address1,address2,address3
        FROM m_address
        WHERE account_id = %s;
        """
        cur.execute(sql_address, (user_id,))
        address_list = cur.fetchall()


        #カード情報を取得
        sql_card="""
        SELECT id,number,expiry,holderName
        FROM t_creditCard
        WHERE account_id = %s;
        """
        cur.execute(sql_card, (user_id,))
        card_info = cur.fetchall()

    except mysql.connector.Error as err:
        print(f"データベースエラー: {err}")

    finally:
        if con and con.is_connected():
            cur.close()
            con.close()
        
    #支払い情報を取得
    bank_info,accountNumbers,count=getAccountInfo()

    return render_template("purchase/purchase.html",user_id = user_id, product = product, address_list=address_list, card_info=card_info, accountNumbers=accountNumbers, count=count)

#レンタルができるようにする
@products_bp.route('/rental/<int:product_id>', methods=['GET'])
def rental(product_id):
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')

    return render_template("purchase/purchase.html",user_id = user_id )




#購入完了画面
@products_bp.route('/purchase_complete', methods=['POST'])
def purchase_complete():
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')

    product_id = request.form.get('product_id')
    payment_method = request.form.get('payment_method')
    addressId = request.form.get('address_index')
    delivery_location = request.form.get('delivery_location')
    creditcards_id = request.form.get('creditcards_id')

    #購入項目があるかチェック
    if not product_id or not payment_method or not addressId or not delivery_location:

            
        # 商品が見つからない場合は、エラーページや404を返すのが適切です
        return render_template('error.html'), 404 # **ここで関数を終了させる**

    #payment_methodがクレジットならpayment_methodを発送待ちにする
    if payment_method == "クレジット":
        status = "発送待ち"
        paymentDeadline = None
        creditcards_id = int(creditcards_id)
    else:
        status = "支払い待ち"
        #72時間後の日付を取得
        paymentDeadline = datetime.now() + timedelta(hours=72)
        creditcards_id = 'NULL'

    #商品情報を取得
    product = get_product_info(product_id)

    # get_product_info()で取得した商品の販売者ID
    seller_id = product['account_id']
    addressId = int(addressId)

    #預かり書と発送書のフラグ
    shipping_flg = False
    received_flg = False

    #取引状況・購入かレンタルか
    situation = "購入"
    
    # dbへの登録処理
    try:
        con = connect_db()
        cur = con.cursor(dictionary=True)

        #住所情報を取得
        sql_address="""
        SELECT
        pref,address1,address2,address3
        FROM m_address
        WHERE id = %s;
        """
        cur.execute(sql_address, (addressId,))
        address = cur.fetchone()
        shippingAddress = f"{address['pref']} {address['address1']} {address['address2']} {address['address3']}"

        

        #購入情報をt_purchaseテーブルに登録
        sql_purchase="""
        INSERT INTO t_transaction (
        customer_id,
        seller_id, 
        product_id, 
        status,
        situation,
        paymentMethod,
        paymentDeadline,
        shippingAddress,
        creditcard_id,
        shippingFlg,
        receivedFlg)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s);
        """
        #situation #取引状態・購入の場合は'購入'レンタルの場合は'レンタル'
        cur.execute(sql_purchase, (user_id, seller_id, product_id, status,situation,payment_method,paymentDeadline, shippingAddress, creditcards_id,shipping_flg,received_flg))
        con.commit()

        #商品テーブルを更新
        # sql_update_product="""
        # UPDATE m_product
        # SET availability = '取引中'
        # WHERE id = %s;
        # """
        # cur.execute(sql_update_product, (product_id,))
        # con.commit()

    except mysql.connector.Error as err:
        print(f"データベースエラー: {err}")

    finally:
        if con and con.is_connected():
            cur.close()
            con.close()

    return render_template("purchase/purchase_complete.html", user_id=user_id)


# DB接続設定
def connect_db():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        db='db_subkari'
    )
    return con

