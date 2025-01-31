from firebase_admin import credentials, initialize_app
from firebase_admin import db as firebase_db

cred = credentials.Certificate('credentials.json')
initialize_app(cred, {'databaseURL': 'https://identity-all-around-id-default-rtdb.firebaseio.com/'})

db = firebase_db.reference()

def add_user(user):
    db.push(user)