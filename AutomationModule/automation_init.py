import pytest
import sys, os
sys.path.append(os.path.abspath('Data'))
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from main import Data
data_env = Data()
data = data_env.get_data()

class AutomationInit:
    def __init__(self, values=None):
        if values is None:
            values = {"username": data.user_name,
                      "password": data.password,
                      "url": data.url }
        self.user_name = values["username"]
        self.password = values["password"]
        self.url = values["url"]

    def Chrome(self):
        chrome_options=webdriver.ChromeOptions()
        prefs={"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        #chrome_options.add_argument('--headless')
        driver=webdriver.Chrome(options=chrome_options)
        driver.get(self.url)
        self.driver=driver

    def Firefox(self):
        path=os.getcwd()
        driver=webdriver.Firefox(log_path = path + "/Logs/geckodriver.log")
        driver.get(self.url)
        self.driver=driver

    def Safari(self):
        driver=webdriver.Safari()
        driver.get(self.url)
        self.driver=driver

    def getBrowser(self):
        self.Chrome()
        #self.Firefox()
        #self.Safari()
        return self.driver

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath("//input[@id='emailOrUsername']").send_keys(self.user_name)
        self.driver.find_element_by_xpath("//input[@id='pass']").send_keys(self.password)
        self.driver.find_element_by_xpath("//*[contains(text(),'Login')]").click()
        self.driver.implicitly_wait(30)


    def logout(self):
        self.driver.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[1]").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='My Account'])[1]/following::span[2]").click()

    def delay(self, timeinsec = 5):
        time.sleep(timeinsec)

