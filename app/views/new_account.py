from flask import Blueprint , render_template ,request,make_response,redirect,url_for,session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime , timedelta
import mysql.connector
import json
import os

login_bp = Blueprint('login', __name__, url_prefix='/login')


#Login画面表示----------------------------------------------------------------------------------------------------------------------------------------------------------
@login_bp.route('/password-reset', methods=['GET'])
def password_reset():
    # 初期表示用に空の辞書を渡す
    error = None
    success = None
    return render_template('login/password_reset.html', error=error, success=success)

