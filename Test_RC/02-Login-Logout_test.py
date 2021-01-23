import pytest
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
sys.path.append(os.path.abspath('../Data'))
from automation_init import AutomationInit
from main import Data
data_env = Data()
data = data_env.get_data()

path = os.getcwd()
print("current working directory is: {0}".format(path))

def test_withRocketChat():
    automation = AutomationInit()
    browser = automation.getBrowser()
    automation.delay(2)
    print(path)
    browser.save_screenshot(path + "/Screenshots/Login.png")
    automation.login()
    automation.delay()
    # Assert below
    rc = browser.find_element_by_id('rocket-chat')
    if rc.is_displayed():
        print("user is successfully navigated to the homepage")
    else:
        print("Test failed: Homepage is not displayed in the given time")
    automation.delay(2)
    avatar = browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[1]")
    avatar.click()
    logout_button = browser.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='My Account'])[1]/following::span[2]")
    logout_button.click()
    automation.delay(2)
    # Assert below
    if browser.find_element_by_xpath("//input[@id='emailOrUsername']").is_displayed():
        print("Test Passed: Logout is successful")
    else:
        print("Test Failed")
    automation.delay()
    browser.close()


# test for open RC
def withGoogle():
    automation = AutomationInit()
    browser = automation.getBrowser()

    automation.delay()
    browser.find_element_by_xpath("//*[@id='login-card']/div[1]/button[3]").click()
    automation.delay(3)
    browser.switch_to.window(browser.window_handles[1])
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='identifierId']").click()
    browser.find_element_by_xpath("//*[@id='identifierId']").send_keys(data.user_name)
    browser.find_element_by_css_selector("#identifierNext > div > button").click()
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").click()
    browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(data.password)
    browser.find_element_by_css_selector("#passwordNext > div > button").click()
    automation.delay()
    browser.quit()
