import imp
from lib2to3.pgen2 import driver
from selenium import webdriver
from getpass import getpass

from selenium.webdriver.support.ui import Select
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def phonelogin():
    phone = input("Enter in your phone: ")

    driver = webdriver.Chrome("D:\Work\Others\EPORTAL\WEBDRIVERS\chromedriver.exe")
    driver.maximize_window()

    driver.implicitly_wait(120)
    driver.get("https://eportal-uat.ughub.go.ug/e-portal/home/")


    print('trying to select')
    driver.find_element('xpath', '/html/body/div[1]/div/section/header/div[2]/div[3]/div/div/div[2]/div/div/div[2]/button/span').click()

    driver.implicitly_wait(100)

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div"))
    )
    # driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div').click()
    element.click()
    
    print('selected')

    driver.implicitly_wait(80)
    driver.find_element('xpath', '/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/button').click()

    username_textbox = driver.find_element('xpath','//*[@id="username"]')
    username_textbox.send_keys(phone)


    login_button = driver.find_element('xpath', '//*[@id="checkUser"]').click()
    login_button.submit()

    time.sleep(5)


def userlogin():
    username = input("Enter in your username: ")
    password = getpass("Enter your password: ")
    driver = webdriver.Chrome("D:\Work\Others\EPORTAL\WEBDRIVERS\chromedriver.exe")
    driver.maximize_window()

    driver.implicitly_wait(120)
    driver.get("https://eportal-uat.ughub.go.ug/e-portal/home/")

    print('trying to select')
    driver.find_element('xpath', '/html/body/div[1]/div/section/header/div[2]/div[3]/div/div/div[2]/div/div/div[2]/button/span').click()

    driver.implicitly_wait(100)

    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div"))
    )
    # driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div').click()
    element.click()
    
    print('selected')

    driver.implicitly_wait(80)



    # driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div').click()

    # print('selected')


    
    element2 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="usernameUserInput"]'))
    )
    element2.send_keys(username)

    # username_textbox = driver.find_element('xpath', '//*[@id="usernameUserInput"]')
    # username_textbox.send_keys(username)

    element3 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    element3.send_keys(password)

    # password_textbox = driver.find_element('xpath', '//*[@id="password"]')
    # password_textbox.send_keys(password)

    login_button = driver.find_element('xpath', '/html/body/div[2]/div[2]/div/div/div[3]/form/div[7]/div/button').click()
    login_button.submit()
    time.sleep(5)

phonelogin()
userlogin()
driver.quit()