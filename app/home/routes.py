from flask import render_template
from . import home_bp

@home_bp.route('/get-started')
def get_started():
    return render_template('get-started.html')