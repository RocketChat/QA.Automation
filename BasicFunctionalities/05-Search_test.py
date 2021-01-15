from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
automation = AutomationInit()
browser = automation.getBrowser()
automation.login()

def test_SearchPrivateChannel():
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
    search_input = browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input")

    automation.delay(2)
    search_input.click()
    search_input.send_keys("rocketchat-qa")
    automation.delay()
    search_input.send_keys(Keys.ENTER)
    automation.delay()
    # verify chat textarea is present
    status = browser.find_element_by_xpath("//textarea[@name='msg']").is_displayed()
    print(status)

def test_SearchPublicChannel():
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
    search_input = browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input")

    automation.delay(2)
    search_input.click()
    search_input.send_keys("sandbox")
    automation.delay()
    search_input.send_keys(Keys.ENTER)
    automation.delay()
    # verify chat textarea is present
    status = browser.find_element_by_xpath("//textarea[@name='msg']").is_displayed()
    print(status)

def test_SearchUser():
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
    search_input=browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input")

    automation.delay(2)
    search_input.click()
    search_input.send_keys("Meher")
    automation.delay()
    search_input.send_keys(Keys.ENTER)
    automation.delay()
    # verify chat textarea is present
    status = browser.find_element_by_xpath("//textarea[@name='msg']").is_displayed()
    print(status)
    browser.close()

