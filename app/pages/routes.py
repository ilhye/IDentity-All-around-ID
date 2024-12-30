from flask import render_template
from . import pages_bp

@pages_bp.route('/page-one')
def page_one():
    return "Page One"