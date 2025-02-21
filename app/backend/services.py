from firebase_admin import credentials, initialize_app
from firebase_admin import db as firebase_db
'''
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
'''
import time

cred = credentials.Certificate('credentials.json')
initialize_app(cred, {'databaseURL': 'https://identity-all-around-id-default-rtdb.firebaseio.com/'})

db = firebase_db.reference("Personal-Details")

def add_user(user):
    db.push(user)

def check_username(username):
    users = db.order_by_child('username').get()
    if users:
        for key, value in users.items():
            if value.get('username') == username:
                return True
        print(username)
    return False
  
def check_account_exists(username, password):
    users = db.order_by_child('username').get()
    if users:
        for key, value in users.items():
            if value.get('username') == username and value.get('password') == password:
                return True
    return False

def update(username, password):
    users = db.order_by_child('username').get()
    for key, value in users.items():
        if value['username'] == username:
            db.child(key).update({'password': password})
            return True
    return False
