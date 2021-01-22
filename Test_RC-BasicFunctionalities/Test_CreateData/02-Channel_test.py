import pytest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import sys, os
sys.path.append(os.path.abspath('../../AutomationModule'))
sys.path.append(os.path.abspath('../../Data'))
from automation_init import AutomationInit
from main import Data
data_env = Data()
data = data_env.get_data()
path = os.getcwd()

automation = AutomationInit()
browser = automation.getBrowser()
automation.login()
add_button = browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]")

def test_Channel():
    add_button.click()
    browser.find_element_by_xpath("//span[contains(text(),'Channel')]").click()
    automation.delay()
    browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[1]/label/div[2]/input").click()
    browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[1]/label/div[2]/input").send_keys(data.channel_name)
    browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input").click()
    #browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input").send_keys(data.user)
    browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input").send_keys(data.new_user)
    automation.delay()
    browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input").send_keys(Keys.ENTER)
    browser.find_element_by_xpath("//*[@id='create-channel']/div[3]/input").click()
    automation.delay()
    # Assert below
    if browser.find_element_by_xpath("//*[contains(text(),'" + data.channel_name + "')]").is_displayed():
        print("channel added successfully")
    else:
        print("Test failed: channel added is not getting displayed")
    automation.delay()

def test_AddUsersToChannel():
    automation.delay(2)
    browser.find_element_by_xpath("//*[contains(text(),'" + data.channel_name + "')]").click()
    automation.delay(2)
    members = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/div/div/main/header/div/div[3]/button[4]")
    members.click()
    add_users = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/div/div/main/div/aside/footer/div/button[2]")
    add_users.click()
    input_field = browser.find_element_by_xpath("//input[@placeholder='Choose users']")
    input_field.click()
    input_field.send_keys(data.new_user)
    automation.delay(3)
    input_field.send_keys(Keys.ENTER)
    add_UsersButton = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/div/div/main/div/aside/footer/button")
    add_UsersButton.click()
    automation.delay()
    # Assert below that the user is already added, if initially created and added
    try:
        element = browser.find_element_by_css_selector(".wrapper>ul>li:last-child>div:nth-child(2)>div:nth-child(2)>span:nth-child(3)")
        assert element
        print("user is already added")
    except NoSuchElementException:
        print("User added successfully")
    home = browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[1]")
    home.click()
    automation.delay(3)
    browser.close()







