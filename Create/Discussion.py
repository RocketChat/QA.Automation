from selenium.webdriver.common.keys import Keys
from automation_init import AutomationInit
automation = AutomationInit()
automation.chrome()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)
channelName = "sandbox"
user = "meherishrat"
discussionName = "DiscussionTestt"
discussionMessage = "TestDiscussion"

browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]").click()
browser.find_element_by_xpath("//span[contains(text(),'Discussion')]").click()
automation.delay()
browser.find_element_by_xpath("//*[@id='parentChannel']").click()
browser.find_element_by_xpath("//*[@id='parentChannel']").send_keys(channelName)

automation.delay(3)
browser.find_element_by_xpath("//*[@id='parentChannel']").send_keys(Keys.ENTER)
automation.delay(3)
browser.find_element_by_xpath("//*[@id='discussion_name']").click()
browser.find_element_by_xpath("//*[@id='discussion_name']").send_keys(discussionName)
browser.find_element_by_xpath("//*[@id='users']").click()
browser.find_element_by_xpath("//*[@id='users']").send_keys(user)
automation.delay(3)
browser.find_element_by_xpath("//*[@id='users']").send_keys(Keys.ENTER)

browser.find_element_by_xpath("//*[@id='discussion_message']").click()
browser.find_element_by_xpath("//*[@id='discussion_message']").send_keys(discussionMessage)
browser.find_element_by_xpath("//button[@form='create-discussion']").click()
automation.delay(3)
browser.close()