from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
sys.path.append(os.path.abspath('../Data'))
from automation_init import AutomationInit
from Data import main
data = main.main()

automation = AutomationInit()
browser = automation.getBrowser()
automation.login()
add_button = browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]")

def test_Discussion():
    add_button.click()
    browser.find_element_by_xpath("//span[contains(text(),'Discussion')]").click()
    automation.delay()
    browser.find_element_by_xpath("//*[@id='parentChannel']").click()
    browser.find_element_by_xpath("//*[@id='parentChannel']").send_keys(data.channel_name)
    automation.delay()
    browser.find_element_by_xpath("//*[@id='parentChannel']").send_keys(Keys.ENTER)
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='discussion_name']").click()
    browser.find_element_by_xpath("//*[@id='discussion_name']").send_keys(data.discussion_name)
    browser.find_element_by_xpath("//*[@id='users']").click()
    browser.find_element_by_xpath("//*[@id='users']").send_keys(data.user)
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='users']").send_keys(Keys.ENTER)

    browser.find_element_by_xpath("//*[@id='discussion_message']").click()
    browser.find_element_by_xpath("//*[@id='discussion_message']").send_keys(data.discussion_message)
    browser.find_element_by_xpath("//button[@form='create-discussion']").click()
    automation.delay(3)
    assert browser.find_element_by_xpath("//*[contains(text(),'" + data.discussion_name + "')]")
    browser.close()
