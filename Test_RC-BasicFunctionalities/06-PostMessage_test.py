from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
sys.path.append(os.path.abspath('../Data'))
from automation_init import AutomationInit
from main import TestData
test_data = TestData()
data = test_data.get_data()

automation = AutomationInit()
browser = automation.getBrowser()
automation.login()

def test_InPrivateChannel():
    browser.find_element_by_xpath("//*[contains(text(),'" + data.channel_name + "')]").click()
    automation.delay(2)
    browser.find_element_by_xpath("//*[@name='msg']").click()
    browser.find_element_by_xpath("//*[@name='msg']").send_keys(data.message)
    browser.find_element_by_xpath("//*[@name='msg']").send_keys(Keys.ENTER)
    automation.delay()
    # Assert below
    message_sent = browser.find_element_by_xpath("//*[text()[contains(.,'" + data.message + "')]]")
    assert message_sent
    print("Test Passed: Message sent successfully")

def test_InPublicChannel():
    automation.delay()
    browser.find_element_by_xpath("//*[contains(text(),'general')]").click()
    automation.delay(2)
    browser.find_element_by_xpath("//*[@name='msg']").click()
    browser.find_element_by_xpath("//*[@name='msg']").send_keys(data.message)
    browser.find_element_by_xpath("//*[@name='msg']").send_keys(Keys.ENTER)
    automation.delay()
    # Assert below
    message_sent = browser.find_element_by_xpath("//*[text()[contains(.,'" + data.message + "')]]")
    assert message_sent
    print("Test Passed: Message sent successfully")
    browser.close()




