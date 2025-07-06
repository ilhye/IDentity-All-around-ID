from flask import Blueprint

layout_bp = Blueprint('layout', __name__, template_folder='templates', static_folder='static')

from . import routes