# ==========================================================
# Filename      : app/__init__.py
# Descriptions  : Application Factory
# ==========================================================
from flask import Flask,make_response, render_template,request,session
from config import Config

def create_app():
    # Flaskアプリケーションのインスタンスを作成
    # __name__をappパッケージのパスに設定
    app = Flask(__name__)
    
    # config.pyから設定を読み込む
    app.config.from_object(Config)

    # --- Blueprintの登録 ---
    # viewsパッケージからproductsとauthのBlueprintをインポート
    from .views import top,login,products,seller,dashboard,mypage
    
    app.register_blueprint(top.top_bp)
    app.register_blueprint(login.login_bp)
    app.register_blueprint(products.products_bp)
    app.register_blueprint(seller.seller_bp)
    app.register_blueprint(dashboard.dashboard_bp)
    # app.register_blueprint(account_management.account_management_bp)
    # app.register_blueprint(account_management_detail.account_management_detail_bp)
    app.register_blueprint(mypage.mypage_bp)
    
    return app