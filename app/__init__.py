# Creates the Flask app and registers the blueprints.
from flask import Flask
from app.pages import pages_bp
from app.auth import auth_bp

def run_app():
    app = Flask(__name__)

    # Register the blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(pages_bp, url_prefix='/pages')

    return app