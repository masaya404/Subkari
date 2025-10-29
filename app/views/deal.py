from flask import Blueprint, render_template, request, make_response, redirect, url_for, session
from PIL import Image
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import mysql.connector
import json
import os

deal_bp = Blueprint('deal', __name__, url_prefix='/deal')


# Login画面表示 ----------------------------------------------------------------------------------------------------------------------------------------------------------
@deal_bp.route('/deal', methods=['GET'])
def deal():
    # errorメッセージ
    if 'user_id' not in session:
        user_id = None
        return redirect(url_for('login.login'))
    else:
        user_id = session.get('user_id')
        
    return render_template('deal/deal_index.html', user_id = user_id)
