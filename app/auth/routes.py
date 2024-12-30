from flask import render_template
from . import auth_bp

@auth_bp.route('/get-started')
def get_started():
    return render_template('get-started.html')