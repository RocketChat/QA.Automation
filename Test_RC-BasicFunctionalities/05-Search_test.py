import pytest
from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
sys.path.append(os.path.abspath('../Data'))
from automation_init import AutomationInit
from main import Data
data_env = Data()
data = data_env.get_data()

automation = AutomationInit()
browser = automation.getBrowser()
automation.login()

def test_SearchPrivateChannel():
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
    search_input = browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input")

    automation.delay(2)
    search_input.click()
    search_input.send_keys(data.channel_name)
    automation.delay()
    search_input.send_keys(Keys.ENTER)
    automation.delay()
    # Assert below verify chat textarea is present
    status = browser.find_element_by_xpath("//textarea[@name='msg']").is_displayed()
    if status == True:
        print("Test Passed: Channel searched successfully")
    else:
        print("Test Failed: Channel search failed")

def test_SearchPublicChannel():
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
    search_input = browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input")

    automation.delay(2)
    search_input.click()
    search_input.send_keys("general")
    automation.delay()
    search_input.send_keys(Keys.ENTER)
    automation.delay()
    # Assert below verify chat textarea is present
    status = browser.find_element_by_xpath("//textarea[@name='msg']").is_displayed()
    if status == True:
        print("Test Passed: Public Channel searched successfully")
    else:
        print("Test Failed: Public Channel search failed")

def test_SearchUser():
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
    search_input = browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input")

    automation.delay(2)
    search_input.click()
    search_input.send_keys(data.new_user)
    automation.delay()
    search_input.send_keys(Keys.ENTER)
    automation.delay()
    # Assert below verify chat textarea is present
    status = browser.find_element_by_xpath("//textarea[@name='msg']").is_displayed()
    if status == True:
        print("Test Passed: User searched successfully")
    else:
        print("Test Failed: User search failed")
    browser.close()

