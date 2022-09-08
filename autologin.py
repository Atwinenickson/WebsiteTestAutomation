from selenium import webdriver
from getpass import getpass

from selenium.webdriver.support.ui import Select
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from os import environ

from dotenv import load_dotenv
load_dotenv()




def phonelogin():
    phone = input("Enter in your phone: ")

    driver = webdriver.Chrome("D:\Work\Others\EPORTAL\WEBDRIVERS\chromedriver.exe")
    driver.maximize_window()

    driver.implicitly_wait(120)

    url = environ.get('baseurl')
    driver.get(url)

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/header/div[2]/div[3]/div/div/div[2]/div/div/div[2]/button"))
    )
    element.click()
    # driver.implicitly_wait(100)

    element1 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[1]"))
    )
    element1.click()
    time.sleep(10)

    # driver.implicitly_wait(80)
    # driver.find_element('xpath', '/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/button').click()

    # username_textbox = driver.find_element('xpath','//*[@id="username"]')
    # username_textbox.send_keys(phone)


    # login_button = driver.find_element('xpath', '//*[@id="checkUser"]').click()
    # login_button.submit()

    time.sleep(10)


def userlogin():
    username = input("Enter in your username: ")
    password = getpass("Enter your password: ")
    driver = webdriver.Chrome("D:\Work\Others\EPORTAL\WEBDRIVERS\chromedriver.exe")
    driver.maximize_window()

    driver.implicitly_wait(120)
    url = environ.get('baseurl')
    driver.get(url)


    print('trying to select')
    driver.find_element('xpath', '/html/body/div[1]/div/section/header/div[2]/div[3]/div/div/div[2]/div/div/div[2]/button/span').click()

    driver.implicitly_wait(100)

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div"))
    )
    element.click()

    driver.implicitly_wait(80)


    
    element2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="usernameUserInput"]'))
    )
    element2.send_keys(username)

    element3 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    element3.send_keys(password)

    login_button = driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div/div[3]/form/div[7]/div/button').click()
    login_button.submit()
    time.sleep(5)





def signup():
    driver = webdriver.Chrome("D:\Work\Others\EPORTAL\WEBDRIVERS\chromedriver.exe")
    driver.maximize_window()

    driver.implicitly_wait(120)
    url = environ.get('baseurl')
    driver.get(url)

    register = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/header/div[2]/div[3]/div/div/div[2]/div/div/div[1]/button/span"))
    )
    register.click()

    fName = 'Testing'
    lName = 'Testing'
    oName = 'Testing'
    pNumber = '700988455'
    uName = 'Shamlka2022'
    uEmail = 'test@test.com'
    cPassword = 'Test@2022An'
    Password = 'Test@2022An'
    

    firstName = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_firstName"]'))
    )
    firstName.send_keys(fName)


    lastName = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_lastName"]'))
    )
    lastName.send_keys(lName)

    driver.implicitly_wait(80)


    
    otherName = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_middleName"]'))
    )
    otherName.send_keys(oName)


    phone = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_phoneNum"]'))
    )
    phone.send_keys(pNumber)




    userName = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_username"]'))
    )
    userName.send_keys(uName)


    email = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_email"]'))
    )
    email.send_keys(uEmail)

    driver.implicitly_wait(80)


    
    otherName = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_middleName"]'))
    )
    otherName.send_keys(oName)

    password = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_password"]'))
    )
    password.send_keys(Password)

    ConfirmPassword = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_confirm"]'))
    )
    ConfirmPassword.send_keys(cPassword)

    terms = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_isTermsAndConditionsAccepted"]'))
    )
    terms.click()

    time.sleep(2)

    gender = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/section/main/div[1]/div/div[2]/form/div[1]/div[6]/div/div[1]/div/div[2]/div/div/div/label[1]/span[1]/input'))
    )
    gender.click()

    nation = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_userType"]'))
    )
    nation.click()

    Snation = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div'))
    )
    Snation.click()



    


    date = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-profile-data_dob"]'))
    )
    date.click()

    selectdate = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div/div[1]/div[2]/table/tbody/tr[2]/td[4]/div'))
    )
    selectdate.click()




    register = driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div/div[3]/form/div[7]/div/button').click()
    register.submit()
    time.sleep(5)



phonelogin()
# userlogin()
# signup()