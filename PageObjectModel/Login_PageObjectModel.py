import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sys
import unittest
sys.path.append('D:\\Workspace\\Python_Work\\Temp_Orange_Automation')
from Driver.DriverScript import driver
from Application_Functions.ReportLog import report_log
from Application_Functions.ReportLog import capturescreenshot


class Elements(unittest.TestCase):
    try:
        TextBox_UserName_xpath = '//input[@name="txtUsernam"]'
        TextBox_Password_id = 'txtPassword'
        Button_Login_id = 'btnLogin'
        Button_Admin_xpath = '//a[@class="firstLevelMenu"]//b[contains(text(),"Admin")]'
        TextBox_UName_xpath = '//input[@name="searchSystemUser[userName]"]'
        TextBox_UserType_css_selector = 'select[id="searchSystemUser_userType"]'
        TextBox_EmpName_id = 'searchSystemUser_employeeName_empName'
        TextBox_UserStatus_css_selector = 'select[id="searchSystemUser_status"]'
        Button_Search_id = 'searchBtn'
        Read_NoRecordsFound_xpath = '//table[@id="resultTable"]//tr//td'
        Button_Add_xpath = '//input[@name="btnAdd"]'
        Link_WelCome_xpath = '//a[contains(text(),"Welcome Admin")]'
        Link_Logout_xpath = '//a[contains(text(),"Logout")]'

        def set_user_name(self,username):
            try:
                driver.find_element_by_xpath(self.TextBox_UserName_xpath).send_keys(username)
            except NoSuchElementException as er:
                report_log('', 'Error occured', er, 'Fail')
                print('Error message',er)
            ele = driver.find_element_by_xpath('(//span[contains(text(),"Username")])[2]')
            if ele.is_enabled():
                report_log('User Name TextBox','Value must be entered','Value entered:'+username,'Pass')
            else:
                report_log('User Name TextBox', 'Value must be entered','Value not entered:'+username,'Fail')

        def set_password(self,password):
            driver.find_element_by_id(self.TextBox_Password_id).send_keys(password)
            ele = driver.find_element_by_xpath('(//span[contains(text(),"Password")])[2]')
            if ele.is_enabled():
                report_log('Password TextBox','Value must be entered','Password entered:'+password,'Pass')
            else:
                report_log('Password TextBox', 'Value must be entered','Password not entered:'+password,'Fail')

        def click_login_button(self):
            ele = driver.find_element_by_xpath('//input[@id="btnLogin"]')
            if ele.is_displayed():
                report_log('click Login button','Button must be clicked','Clicked','Pass')
            else:
                report_log('click Login button','Button must be clicked','Clicked','Fail')
            driver.find_element_by_id(self.Button_Login_id).click()

        def click_logout(self):
            driver.find_element_by_xpath(self.Link_WelCome_xpath).click()
            ele = driver.find_element_by_xpath(self.Link_Logout_xpath)

            if ele.is_displayed():
                report_log('click Logout found', 'Button must be clicked', 'Clicked', 'Pass')
            else:
                report_log('click Logout button', 'Button must be clicked', 'not Clicked', 'Fail')

            capturescreenshot()
            driver.find_element_by_xpath(self.Link_Logout_xpath).click()

    except selenium.common.exceptions.NoSuchElementException as er:
        report_log('', 'Error occured', er, 'Fail')
        print('Error Message is : ',er)

