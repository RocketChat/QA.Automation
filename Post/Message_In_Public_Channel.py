from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
automation = AutomationInit()
automation.chrome()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

browser.find_element_by_xpath("//*[contains(text(),'sandbox')]").click()
automation.delay()
browser.find_element_by_xpath("//*[@name='msg']").click()
browser.find_element_by_xpath("//*[@name='msg']").send_keys("Hello testing")
browser.find_element_by_xpath("//*[@name='msg']").send_keys(Keys.ENTER)
automation.delay()
browser.close()

