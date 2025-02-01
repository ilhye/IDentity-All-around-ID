from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

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
def fill_out_form(user_data):
    driver.find_element(By.ID, "agree").click()
    driver.find_element(By.XPATH, "//input[@value='Individual']").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Next')]").click()
    driver.find_element(By.ID, "//*[@id='SiteID']").click()
    driver.find_element(By.ID, "//*[@id='co-notif-checkbox']").click()
    driver.find_element(By.ID, "//*[@id='next-available-date']").click()
    driver.find_element(By.ID, "//*[@id='TimeSlotID']").click()
    driver.find_element(By.ID, "//*[@id='NextButton']").click()
    driver.find_element(By.ID, "//*[@id='PhoneNumber']").click()
    driver.find_element(By.ID, "//*[@id='MobileNumber'']").click()
    driver.find_element(By.ID, "//*[@id='EmailAddress']").click()
    driver.find_element(By.ID, "//*[@id='ConfirmEmailAddress']").click()
    driver.find_element(By.ID, "//*[@id='LastName']").click()
    driver.find_element(By.ID, "//*[@id='FirstName']").click()
    driver.find_element(By.ID, "//*[@id='MiddleName']").click()
    driver.find_element(By.ID, "//*[@id='Birthday_Month']").click()
    driver.find_element(By.ID," //*[@id='Birthday_Day']").click()
    driver.find_element(By.ID, "//*[@id='Birthday_Year']").click()
    driver.find_element(By.ID, "//*[@value='M']").click()
    driver.find_element(By.ID, "//*[@value='F']").click()
    driver.find_element(By.ID, "//*[@id='CivilStatus']").click()
    driver.find_element(By.ID, "//*[@id='BirthRight']/option[2]").click()
    driver.find_element(By.ID, "//*[@id='FatherLastName']").click()
    driver.find_element(By.ID, "//*[@id='FatherFirstName']").click()
    driver.find_element(By.ID, "//*[@id='FatherMiddleName']").click()
    driver.find_element(By.ID,"//*[@id='FatherCitizenship']/option[1]").click()
    driver.find_element(By.ID, "//*[@id='MotherLastName']").click()
    driver.find_element(By.ID, "//*[@id='MotherFirstName']").click()
    driver.find_element(By.ID, "//*[@id='MotherMiddleName']").click()
    driver.find_element(By.ID, "//*[@id='MotherCitizenship']/option[1]").click()
    driver.find_element(By.ID, "//*[@id='SpouseLastName']").click()
    driver.find_element(By.ID, "//*[@id='SpouseFirstName']").click()
    driver.find_element(By.ID, "//*[@id='SpouseMiddleName']").click()
    driver.find_element(By.ID, "//*[@id='SpouseCitizenship']/option[1]").click()
    driver.find_element(By.ID, "//*[@id='ApplicationType']/option[2]").click()
    driver.find_element(By.ID, "//*[@id='Citizenship']/option[2]").click()
    driver.find_element(By.ID, "//*[@id='HasForeignPassport']").click()
    driver.find_element(By.ID, "//*[@id='EmergencyContactPerson']").click()
    driver.find_element(By.ID, "//*[@id='EmergencyContactNumber']").click()
    driver.find_element(By.ID, "//*[@id='container']/div/div[2]/div/form/div[7]/div[2]/div/div[2]/button").click()
    driver.find_element(By.ID, "//*[@id='CompleteAddress']").click()
    driver.find_element(By.ID, "//*[@id='City']").click()
    driver.find_element(By.ID, "//*[@id='Province']").click()
    driver.find_element(By.ID, "//*[@id='Occupation']").click()
    driver.find_element(By.ID, "//*[@id='OfficeNumber']").click()
    driver.find_element(By.ID, "//*[@id='OfficeAddress']").click()
# Keep the browser open for 30 seconds
time.sleep(1000)

# Close the browser
# driver.quit()