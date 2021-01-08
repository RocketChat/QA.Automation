import time
from selenium.webdriver.common.keys import Keys
from automation_init import AutomationInit
automation = AutomationInit()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").click()
time.sleep(2)
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").send_keys("Meher")
time.sleep(5)
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").send_keys(Keys.ENTER)
time.sleep(5)
browser.find_element_by_xpath("//*[@name='msg']").click()
browser.find_element_by_xpath("//span[@class='rc-message-box__icon emoji-picker-icon js-emoji-picker']").click()
browser.find_element_by_xpath("//input[@name='name']").click()
browser.find_element_by_xpath("//input[@name='name']").send_keys("Smiley")
time.sleep(5)
browser.find_element_by_xpath("//*[@data-emoji='smiley']").click()
time.sleep(5)
browser.find_element_by_xpath("//*[@name='msg']").send_keys(Keys.ENTER)
time.sleep(5)

automation.logout()
time.sleep(5)
browser.close()

