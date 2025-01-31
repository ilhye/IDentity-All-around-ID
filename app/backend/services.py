from firebase_admin import credentials, initialize_app
from firebase_admin import db as firebase_db

cred = credentials.Certificate('credentials.json')
initialize_app(cred, {'databaseURL': 'https://identity-all-around-id-default-rtdb.firebaseio.com/'})

db = firebase_db.reference("Personal-Details")

def add_user(user):
    db.push(user)

def check_username(username):
    users = db.order_by_child('username').get()
    if users:
        for key, value in users.items():
            if value['username'] == username:
                return True
    return False

def update(username,password):
    users = db.order_by_child('username').get()
    for key, value in users.items():
        if value['username'] == username:
            db.child(key).update({'password': password})
            return True
    return False