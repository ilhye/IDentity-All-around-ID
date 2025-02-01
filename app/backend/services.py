from firebase_admin import credentials, initialize_app, auth
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
  
def check_account_exists(username, password):
    users = db.order_by_child('username').get()
    if users:
        for key, value in users.items():
            if value['username'] == username and value['password'] == password:
                return True
    return False
    
def update(username,password):
    users = db.order_by_child('username').get()
    for key, value in users.items():
        if value['username'] == username:
            db.child(key).update({'password': password})
            return True
    return False

def create_user_with_username_and_password(username, password):
    user = auth.create_user(username=username, password=password)
    return user

def verify_user_with_username_and_password(username, password):
    users = db.order_by_child('username').get()
    if users:
        for key, value in users.items():
            if value['username'] == username and value['password'] == password:
                return True
    return False