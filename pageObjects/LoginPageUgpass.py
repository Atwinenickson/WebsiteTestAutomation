import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageUgpas:
    # Login Page
    login_button_xpath = '/html/body/div[1]/div/section/header/div[2]/div[3]/div/div/div[2]/div/div/div[2]/button/span'
    ugpass_button_xpath = '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/h5'
    ugpass_accept_terms_xpath = '/html/body/div[2]/div[1]/div/div/div/div/div/div[2]/button'
    id_xpath = '//*[@id="username"]'
    login_xpath = '//*[@id="checkUser"]'



    def __init__(self,driver):
        self.driver=driver
        self.driver.maximize_window()

    
    def clickLoginButton(self):
        login = WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, self.login_button_xpath))
    )
        login.click()
    


    def clickUgpass(self):
        ugpass = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.ugpass_button_xpath))
        )
        ugpass.click()

    def clickTerms(self):
        self.driver.find_element('xpath', self.ugpass_accept_terms_xpath).click()


    def setID(self, id):
        id = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.id_xpath))
        )
        id.send_keys(id)


    def clickLogin(self):
        self.driver.find_element('xpath', self.login_button_xpath).click()
        time.sleep(10)

    # def clickLogout(self):
    #     self.driver.find_element_by_link_text(self.link_logout_linktext).click()