import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from automation_init import AutomationInit
automation = AutomationInit()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

action = ActionChains(browser)
browser.find_element_by_xpath("//*[contains(text(),'Meher')]").click()
time.sleep(5)
source = browser.find_element_by_css_selector(".wrapper>ul>li:last-child")
action.move_to_element(source).perform()
browser.find_element_by_css_selector(".wrapper>ul>li:last-child> div.message-actions > div.message-actions__buttons > button:nth-child(3)").click()
browser.find_element_by_css_selector("section > div.rc-message-box.rc-new > label >textarea").click()
automation.delay()
browser.find_element_by_css_selector("section > div.rc-message-box.rc-new > label >textarea").send_keys("Testing reply in thread")
browser.find_element_by_css_selector("section > div.rc-message-box.rc-new > label >textarea").send_keys(Keys.ENTER)
browser.find_element_by_css_selector(".rcx-box >div>h3>div>div> button:nth-child(2)").click()
time.sleep(5)
browser.close()
