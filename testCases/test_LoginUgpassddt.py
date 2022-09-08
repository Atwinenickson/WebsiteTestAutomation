import pytest
from pageObjects.LoginPageUghub import LoginPageUghub
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_005_Ugpass_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("******* Starting Test_005_UGPASsS_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPageUghub(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet2')
        print('Number of rows...',self.rows)
        lst_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet2',r,1)
            self.exp = XLUtils.readData(self.path, 'Sheet2', r, 2)

            self.lp.clickLoginButton()
            self.lp.clickUghub()
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="EPORTAL APPLICATION"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info("**** passed ****")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp=='Fail':
                    self.logger.info("**** failed ****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("******* UGPASS DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* UGPASS DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login UGPASS DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");