import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
import sys
import time
sys.path.append('D:\\Workspace\\Python_Work\\Temp_Orange_Automation')
from Driver.DriverScript import driver
from PageObjectModel.Login_PageObjectModel import Elements
from Application_Functions.ReportLog import report_log
from Application_Functions.ReportLog import inserttestcase
from Application_Functions.ReportLog import startreport
from Application_Functions.ReportLog import endreport
from Application_Functions.ReportLog import capturescreenshot


class LoginTest(unittest.TestCase):
    baseURL = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
    username = 'Admin'
    password = 'admin123'
    ScreenShotPath = "D:\\Workspace\\Python_Work\\Temp_Orange_Automation\\HTML_Report\\UserName.jpg"
    driver.implicitly_wait(10)

    global lp
    lp = Elements()

    @classmethod
    def setUpClass(cls):
        driver.get(cls.baseURL)
        driver.maximize_window()
        startreport()

    def test_login(self):
        inserttestcase('test_login')
        driver.implicitly_wait(10)
        lp.set_user_name(self.username)
        lp.set_password(self.password)
        capturescreenshot()
        lp.click_login_button()
        self.assertEqual('OrangeHRM', driver.title, 'Title not matched, Fail')

    def test_logout(self):
        inserttestcase('test_logout')
        lp.click_logout()

    @classmethod
    def tearDownClass(cls):
        driver.close()
        endreport()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\\Workspace\\Python_Work\\Temp_Orange_Automation\\HTML_Report'))

