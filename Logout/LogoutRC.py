import time
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
automation = AutomationInit()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[1]").click()
browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='My Account'])[1]/following::span[2]").click()
time.sleep(3)
browser.close()