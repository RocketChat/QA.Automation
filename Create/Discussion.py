import time
from selenium.webdriver.common.keys import Keys
from automation_init import AutomationInit
automation = AutomationInit()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)
channelName = "sandbox"

browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]").click()
browser.find_element_by_xpath("//span[contains(text(),'Discussion')]").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='parentChannel']").click()
browser.find_element_by_xpath("//*[@id='parentChannel']").send_keys(channelName)

time.sleep(3)
browser.find_element_by_xpath("//*[@id='parentChannel']").send_keys(Keys.ENTER)
time.sleep(3)
browser.find_element_by_xpath("//*[@id='discussion_name']").click()
browser.find_element_by_xpath("//*[@id='discussion_name']").send_keys("DiscussionTestt")
browser.find_element_by_xpath("//*[@id='users']").click()
browser.find_element_by_xpath("//*[@id='users']").send_keys("meherishrat")
time.sleep(3)
browser.find_element_by_xpath("//*[@id='users']").send_keys(Keys.ENTER)

browser.find_element_by_xpath("//*[@id='discussion_message']").click()
browser.find_element_by_xpath("//*[@id='discussion_message']").send_keys("TestDiscussion")
browser.find_element_by_xpath("//button[@form='create-discussion']").click()
time.sleep(3)
browser.close()