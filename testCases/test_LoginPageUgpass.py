import pytest
from selenium import webdriver
from pageObjects.LoginPageUgpass import LoginPageUgpas
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_LoginUgpass:
    baseURL = ReadConfig.getApplicationURL()
    id = ReadConfig.getUserID()
    logger=LogGen.loggen()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("****Started Ugpass Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPageUgpas(self.driver)
        self.lp.clickLoginButton()
        self.lp.clickUgpass()
        self.lp.clickTerms()
        self.lp.setID(self.id)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="EPORTAL APPLICATION":
            self.logger.info("****Login ugpas test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login ugpas test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False
