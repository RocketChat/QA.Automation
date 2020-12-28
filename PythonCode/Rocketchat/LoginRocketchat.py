from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://open.rocket.chat/")
driver.maximize_window()

driver.find_element_by_xpath("//input[@id='emailOrUsername']").send_keys("ishrat.manzoor@rocket.chat")
driver.find_element_by_xpath("//input[@id='pass']").send_keys("I0s1h2u3##@")
driver.find_element_by_xpath("//*[contains(text(),'Login')]").click()

time.sleep(15)
driver.close()