from flask import Blueprint, render_template, request, make_response, redirect, url_for, session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import mysql.connector
import json
import os

deal_bp = Blueprint('deal', __name__, url_prefix='/deal')


# 取引TOP画面表示 ----------------------------------------------------------------------------------------------------------------------------------------------------------
@deal_bp.route('/deal', methods=['GET'])
def deal():
    # user検証成功
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
        
    return render_template('deal/deal_index.html', user_id = user_id)
# 取引一覧画面表示 ----------------------------------------------------------------------------------------------------------------------------------------------------------
@deal_bp.route('/deal/list', methods=['GET'])
def deal_list():
    # euser検証成功
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
        
    return render_template('deal/deal_detail.html', user_id = user_id)

# 取引詳細の画像添付 ----------------------------------------------------------------------------------------------------------------------------------------------------------
@deal_bp.route('/deal/list/imageUpload', methods=['POST'])
def deal_list_imageUpload():
    # euser検証成功
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
        
    return render_template('deal/deal_detail.html', user_id = user_id)

