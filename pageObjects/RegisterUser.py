import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterUser:
    register_xpath = '/html/body/div[1]/div/section/header/div[2]/div[3]/div/div/div[2]/div/div/div[1]/button/span'
    
    firstName_xpath = '//*[@id="user-profile-data_firstName"]'

    lastName_xpath = '//*[@id="user-profile-data_lastName"]'

    otherName_xpath = '//*[@id="user-profile-data_middleName"]'

    phone_xpath = '//*[@id="user-profile-data_phoneNum"]'

    userName_path = '//*[@id="user-profile-data_username"]'

    email_path = '//*[@id="user-profile-data_email"]'
    

    password_xpath = '//*[@id="user-profile-data_password"]'

    confirmPassword_xpath = '//*[@id="user-profile-data_confirm"]'

    terms_xpath = '//*[@id="user-profile-data_isTermsAndConditionsAccepted"]'
 
    gender_xpath = '/html/body/div[1]/div/section/main/div[1]/div/div[2]/form/div[1]/div[6]/div/div[1]/div/div[2]/div/div/div/label[1]/span[1]/input'
   
    nation_xpath = '//*[@id="user-profile-data_userType"]'

    sNation_xpath = '/html/body/div[2]/div/div/div/div[2]/div[1]/div/div/div[1]/div'
    
    date_xpath = '//*[@id="user-profile-data_dob"]'

    selectdate_xpath = '/html/body/div[3]/div/div/div/div/div[1]/div[2]/table/tbody/tr[2]/td[4]/div'

    addregister_xpath = '/html/body/div[2]/div[2]/div/div/div[3]/form/div[7]/div/button'



    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def Register(self):
        register = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.register_xpath))
        )
        register.click()
    
    
    def setFirstName(self, fName):
        firstName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.firstName_xpath))
        )
        firstName.send_keys(fName)

    def setLastName(self, lName):
        lastName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.lastName_xpath))
        )
        lastName.send_keys(lName)


    def setOtherName(self, oName):
        otherName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.otherName_xpath))
        )
        otherName.send_keys(oName)

    def setPhone(self, pNumber):
        phone = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.phone_xpath))
        )
        phone.send_keys(pNumber)



    def setUsername(self, uName):
        userName = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.userName_path))
        )
        userName.send_keys(uName)


    def setEmail(self, uEmail):
        email = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.email_path))
        )
        email.send_keys(uEmail)

    def setPassword(self, Password):
        password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.password_xpath))
        )
        password.send_keys(Password)

    def setConfirmPassword(self, cPassword):
        ConfirmPassword = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.confirmPassword_xpath))
        )
        ConfirmPassword.send_keys(cPassword)


    def setTerms(self):
        terms = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.terms_xpath))
        )
        terms.click()

    def setGender(self):
        gender = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.gender_xpath))
        )
        gender.click()

    def setNation(self):
        nation = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.nation_xpath))
        )
        nation.click()

    def setSNation(self):
        Snation = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.sNation_xpath))
        )
        Snation.click()



    

    def setDate(self):
        date = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.date_xpath))
        )
        date.click()

        selectdate = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.selectdate_xpath))
        )
        selectdate.click()
        



    def AddRegisteredUser(self):
        register = self.driver.find_element('xpath', self.addregister_xpath).click()
        register.submit()
        time.sleep(5)