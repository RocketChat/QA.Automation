from selenium import webdriver
import time

class AutomationInit:
    def __init__(self, values=None):
        if values is None:
            values = {"username": "ishrat.manzoor@rocket.chat",
                      "password": "I0s1h2u3##@",
                      "url": "https://open.rocket.chat/"}
        self.user_name = values["username"]
        self.password = values["password"]
        self.url = values["url"]

    def chrome(self):
        chrome_options=webdriver.ChromeOptions()
        prefs={"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('--headless')
        driver=webdriver.Chrome(options=chrome_options)
        driver.get(self.url)
        self.driver = driver

    def firefox(self):
        driver= webdriver.Firefox()
        driver.get(self.url)
        self.driver=driver

    def safari(self):
        driver = webdriver.Safari()
        driver.get(self.url)
        self.driver=driver


    def getBrowser(self):
        return self.driver
    def closeBrowser(self):
        self.driver.close()

    def login(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@id='emailOrUsername']").send_keys(self.user_name)
        self.driver.find_element_by_xpath("//input[@id='pass']").send_keys(self.password)
        self.driver.find_element_by_xpath("//*[contains(text(),'Login')]").click()

    def logout(self):
        self.driver.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[1]").click()
        self.driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='My Account'])[1]/following::span[2]").click()

    def delay(self, timeinsec = 5):
        time.sleep(timeinsec)

