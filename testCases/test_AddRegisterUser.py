import pytest
import time
from pageObjects.RegisterUser import RegisterUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_001_RegisterUser:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger


    # DATA
    fName = 'Testing'
    lName = 'Testing'
    oName = 'Testing'
    pNumber = '700988455'
    uName = 'Shamlka2022'
    uEmail = 'test@test.com'
    cPassword = 'Test@2022An'
    uPassword = 'Test@2022An'
    uNin = 'CM12WER432WERa'

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_001_RegisterUser **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("******* Starting Register Test **********")

        self.adduser = RegisterUser(self.driver)

        self.logger.info("************* Providing user info **********")
        self.adduser.Register()
        self.adduser.setFirstName(self.fName)
        self.adduser.setLastName(self.lName)
        self.adduser.setOtherName(self.oName)
        self.adduser.setPhone(self.pNumber)
        self.adduser.setUsername(self.uName)

        self.email = random_generator() + "@gmail.com"
        self.adduser.setEmail(self.email)


        self.adduser.setPassword(self.uPassword)
        self.adduser.setConfirmPassword(self.cPassword)
        self.adduser.setTerms()

        self.adduser.setGender()
        self.adduser.setNation()
        self.adduser.setSNation()


        self.adduser.setDate()

        self.adduser.setNin(self.uNin)

        self.adduser.AddRegisteredUser()
        




        self.logger.info("************* Saving user info **********")

        self.logger.info("********* Add user validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Register User Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_registerUser_scr.png")  # Screenshot
            self.logger.error("********* Register User Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Register test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))