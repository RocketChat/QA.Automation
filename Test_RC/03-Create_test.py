import pytest
from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
sys.path.append(os.path.abspath('../Data'))
from automation_init import AutomationInit
from main import Data
data_env = Data()
data = data_env.get_data()
path = os.getcwd()

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
    browser.find_element_by_xpath("//*[@id='users']").send_keys(data.new_user)
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='users']").send_keys(Keys.ENTER)

    browser.find_element_by_xpath("//*[@id='discussion_message']").click()
    browser.find_element_by_xpath("//*[@id='discussion_message']").send_keys(data.discussion_message)
    browser.find_element_by_xpath("//button[@form='create-discussion']").click()
    automation.delay(3)
    # Assert below
    if browser.find_element_by_xpath("//*[contains(text(),'" + data.discussion_name + "')]").is_displayed():
        print("Test Passed: Discussion added and displayed successfully")
    else:
        print("Test Failed: Discussion is not getting displayed")

def test_DM():
    add_button.click()
    automation.delay(3)
    browser.find_element_by_xpath("//*[contains(text(),'Direct Messages')]").click()
    browser.find_element_by_xpath("//*[@id='directMessageUsers']").click()
    browser.find_element_by_xpath("//*[@id='directMessageUsers']").send_keys(data.new_user)
    # browser.find_element_by_xpath("//*[@id='directMessageUsers']").send_keys(data.user)
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='directMessageUsers']").send_keys(Keys.ENTER)
    automation.delay(2)
    browser.save_screenshot(path + "/Screenshots/DM.png")
    # browser.get_screenshot_as_file("screenDm.png")
    browser.find_element_by_xpath("//button[@form='create-dm']").click()
    # Assert below
    status = browser.find_element_by_xpath("//textarea[@name='msg']").is_displayed()
    if status:
        print("Test passed: DM created successfully")
    else:
        print("Test failed: DM not created")
        automation.delay()
    browser.close()
