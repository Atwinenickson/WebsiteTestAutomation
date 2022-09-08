import pytest
from selenium import webdriver
from pageObjects.LoginPageUghub import LoginPageUghub
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_LoginUghub:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("****Started Ughub Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPageUghub(self.driver)
        self.lp.clickLoginButton()
        self.lp.clickUghub()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="EPORTAL APPLICATION":
            self.logger.info("****Login ughub test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login ughub test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False
