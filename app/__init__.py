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
    from .views import top,auth,products
    
    app.register_blueprint(top.top_bp)
    app.register_blueprint(auth.auth_bp)
    app.register_blueprint(products.products_bp)
        
    return app