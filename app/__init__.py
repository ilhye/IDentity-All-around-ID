# Creates the Flask app and registers the blueprints.
from flask import Flask
from app.home import home_bp

def run_app():
    app = Flask(__name__)

    # Register the blueprint
    app.register_blueprint(home_bp, url_prefix='/home')

    return app