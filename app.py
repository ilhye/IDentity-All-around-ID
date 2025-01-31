from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import auth, exceptions
from firebase_config import *

app = Flask(__name__)
\

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
