from selenium.webdriver.common.keys import Keys
from automation_init import AutomationInit
automation = AutomationInit()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)


browser.find_element_by_xpath("//*[contains(text(),'rocketchat-qa')]").click()

browser.find_element_by_xpath("//*[@name='msg']").click()
browser.find_element_by_xpath("//*[@name='msg']").send_keys("Hello testing")
browser.find_element_by_xpath("//*[@name='msg']").send_keys(Keys.ENTER)


browser.close()


