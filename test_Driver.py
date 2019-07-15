import unittest
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

driver = webdriver.Chrome()#(executable_path='D:\\Softwares\\Selenium\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.google.com')

@pytest.yield_fixture(scope='module')
#def setUp():


