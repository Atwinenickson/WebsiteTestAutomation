import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageUghub:
    # Login Page
    login_button_xpath = '/html/body/div[1]/div/section/header/div[2]/div[3]/div/div/div[2]/div/div/div[2]/button/span'
    ughub_button_xpath = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/div'
    username_xpath = '//*[@id="usernameUserInput"]'
    password_xpath = '//*[@id="password"]'
    login_xpath = '/html/body/div[2]/div[2]/div/div/div[3]/form/div[7]/div/button'



    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    
    def clickLoginButton(self):
        login = WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, self.login_button_xpath))
    )
        login.click()
    


    def clickUghub(self):
        ughub = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.ughub_button_xpath))
        )
        ughub.click()


    def setUserName(self, username):
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.username_xpath))
        )
        username.send_keys(username)

    def setPassword(self, password):
        password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.password_xpath))
        )
        password.send_keys(password)


    def clickLogin(self):
        self.driver.find_element('xpath', self.login_button_xpath).click()
        time.sleep(10)

    # def clickLogout(self):
    #     self.driver.find_element_by_link_text(self.link_logout_linktext).click()