# Creates the Flask app and registers the blueprints.
from flask import Flask, redirect, url_for
from app.pages import pages_bp
from app.auth import auth_bp
from app.layout import layout_bp

def run_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "SecretKey"

    # Register the blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(pages_bp, url_prefix='/pages')
    app.register_blueprint(layout_bp, url_prefix='/layout')

    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))

    return app