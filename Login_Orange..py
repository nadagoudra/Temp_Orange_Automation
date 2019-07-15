from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome(executable_path='D:\\Softwares\\Selenium\\chromedriver_win32\\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)

def login_orange():
    global driver
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
    driver.find_element_by_id("txtUsername").send_keys('Admin')
    driver.find_element_by_id("txtPassword").send_keys('admin123')
    driver.find_element_by_id("btnLogin").click()

def add_user():
    driver.find_element_by_xpath('//a[@class="firstLevelMenu"]//b[contains(text(),"Admin")]').click()
    time.sleep(3)
    UseName = 'Krishna'+str(random.randint(1,1000))
    driver.find_element_by_xpath('//input[@name="searchSystemUser[userName]"]').send_keys(UseName)
    driver.find_element_by_css_selector('select[id="searchSystemUser_userType"]').send_keys('ESS')
    driver.find_element_by_id("searchSystemUser_employeeName_empName").send_keys('Krishna Nadagoudra')
    driver.find_element_by_css_selector('select[id="searchSystemUser_status"]').send_keys('Enabled')
    driver.find_element_by_id("searchBtn").click()
    NoRecords = driver.find_element_by_xpath('//table[@id="resultTable"]//tr//td').text
    print(NoRecords)
    if NoRecords.find('No Records Found') > 0:
        driver.find_element_by_xpath('//input[@name="btnAdd"]').click()

def logout_orange():
    driver.find_element_by_id("welcome").click()
    #driver.find_element_by_xpath('//a[contains(text(),"Logout")]').click()


login_orange()
add_user()
logout_orange()
