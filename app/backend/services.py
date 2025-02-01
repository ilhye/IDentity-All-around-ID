from firebase_admin import credentials, initialize_app
from firebase_admin import db as firebase_db
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
            if value['username'] == username:
                return True
    return False

def update(username, password):
    users = db.order_by_child('username').get()
    for key, value in users.items():
        if value['username'] == username:
            db.child(key).update({'password': password})
            return True
    return False

def automaton(username, password):
    users = db.get()
    for key, value in users.items():
        if value['username'] == username and value['password'] == password:
            # Set up the Chrome options
            options = Options()
            options.add_argument("--start-maximized")

            # Set up the Chrome driver
            driver = webdriver.Chrome(options=options)

            # Open the URL
            driver.get("https://passport.gov.ph/appointment")

            # Wait for the page to load
            time.sleep(5)

            # Fill out the form
            driver.find_element(By.ID, "agree").click()
            driver.find_element(By.XPATH, "//input[@value='Individual']").click()
            driver.find_element(By.XPATH, "//a[contains(text(),'Next')]").click()
            driver.find_element(By.ID, "SiteID").click()
            driver.find_element(By.ID, "co-notif-checkbox").click()
            driver.find_element(By.ID, "next-available-date").click()
            driver.find_element(By.ID, "TimeSlotID").click()
            driver.find_element(By.ID, "NextButton").click()
            driver.find_element(By.ID, "PhoneNumber").send_keys(value['phone'])
            driver.find_element(By.ID, "MobileNumber").send_keys(value['phone'])
            driver.find_element(By.ID, "EmailAddress").send_keys(value['email'])
            driver.find_element(By.ID, "ConfirmEmailAddress").send_keys(value['email'])
            driver.find_element(By.ID, "LastName").send_keys(value['lname'])
            driver.find_element(By.ID, "FirstName").send_keys(value['fname'])
            driver.find_element(By.ID, "MiddleName").send_keys(value['mname'])
            driver.find_element(By.ID, "Birthday_Month").click()
            driver.find_element(By.ID, "Birthday_Day").click()
            driver.find_element(By.ID, "Birthday_Year").click()
            
            # Click gender based on user data
            if value['gender'] == 'Male':
                driver.find_element(By.XPATH, "//*[@value='M']").click()
            elif value['gender'] == 'Female':
                driver.find_element(By.XPATH, "//*[@value='F']").click()
                
            driver.find_element(By.ID, "CivilStatus").click()
            driver.find_element(By.XPATH, "//*[@id='BirthRight']/option[2]").click()
            driver.find_element(By.ID, "FatherLastName").send_keys(value['fatherName'])
            driver.find_element(By.ID, "FatherFirstName").send_keys(value['fatherFirstName'])
            driver.find_element(By.ID, "FatherMiddleName").send_keys(value['fatherMiddleName'])
            driver.find_element(By.XPATH, "//*[@id='FatherCitizenship']/option[1]").click()
            driver.find_element(By.ID, "MotherLastName").send_keys(value['motherName'])
            driver.find_element(By.ID, "MotherFirstName").send_keys(value['motherFirstName'])
            driver.find_element(By.ID, "MotherMiddleName").send_keys(value['motherMiddleName'])
            driver.find_element(By.XPATH, "//*[@id='MotherCitizenship']/option[1]").click()
            driver.find_element(By.ID, "SpouseLastName").send_keys(value['spouseLastName'])
            driver.find_element(By.ID, "SpouseFirstName").send_keys(value['spouseFirstName'])
            driver.find_element(By.ID, "SpouseMiddleName").send_keys(value['spouseMiddleName'])
            driver.find_element(By.XPATH, "//*[@id='SpouseCitizenship']/option[1]").click()
            driver.find_element(By.XPATH, "//*[@id='ApplicationType']/option[2]").click()
            driver.find_element(By.XPATH, "//*[@id='Citizenship']/option[2]").click()
            driver.find_element(By.ID, "HasForeignPassport").click()
            driver.find_element(By.ID, "EmergencyContactPerson").send_keys(value['emergencyContactPerson'])
            driver.find_element(By.ID, "EmergencyContactNumber").send_keys(value['emergencyContactNumber'])
            driver.find_element(By.XPATH, "//*[@id='container']/div/div[2]/div/form/div[7]/div[2]/div/div[2]/button").click()
            driver.find_element(By.ID, "CompleteAddress").send_keys(value['completeAddress'])
            driver.find_element(By.ID, "City").send_keys(value['city'])
            driver.find_element(By.ID, "Province").send_keys(value['province'])
            driver.find_element(By.ID, "Occupation").send_keys(value['occupation'])
            driver.find_element(By.ID, "OfficeNumber").send_keys(value['officeNumber'])
            driver.find_element(By.ID, "OfficeAddress").send_keys(value['officeAddress'])
            time.sleep(1000)

            return True
    return False