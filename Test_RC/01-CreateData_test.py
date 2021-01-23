import pytest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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
# Test Case 1: Add a new user
def test_CreateNewUser():
    automation.delay()
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[6]").click()
    automation.delay(2)
    browser.find_element_by_xpath("//span[contains(text(),'Administration')]").click()
    automation.delay(2)
    browser.find_element_by_xpath("//div[contains(text(), 'Users')]").click()
    browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/section/div[1]/div/div/button[1]").click()
    automation.delay()
    # Enter Name
    name_input = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[1]/span/input")
    name_input.click()
    name_input.send_keys(data.new_user)
    name_input.send_keys(Keys.ENTER)
    # Enter Username
    username_input = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[2]/span/label/input")
    username_input.click()
    username_input.send_keys(data.new_username)
    username_input.send_keys(Keys.ENTER)
    # Enter Email
    email_input = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[3]/span[1]/label/input")
    email_input.click()
    email_input.send_keys(data.new_email)
    email_input.send_keys(Keys.ENTER)
    # Status Message
    status_input = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[4]/span/label/input")
    status_input.click()
    status_input.send_keys(data.new_status)
    status_input.send_keys(Keys.ENTER)
    # Bio
    bio_input = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[5]/span/label/textarea")
    bio_input.click()
    bio_input.send_keys(data.new_bio)
    bio_input.send_keys(Keys.ENTER)
    # Nickname
    nickname_input = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[6]/span/label/input")
    nickname_input.click()
    nickname_input.send_keys(data.new_nickname)
    nickname_input.send_keys(Keys.ENTER)
    # Password
    password_input = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[7]/span/label/input")
    password_input.click()
    password_input.send_keys(data.new_password)
    password_input.send_keys(Keys.ENTER)
    # Roles
    roles_input = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[10]/span/div/div[1]/div/input")
    roles_input.click()
    option_user = browser.find_element_by_css_selector("body > div:nth-child(23) > div > div > ol > li:nth-child(5) > div > div")
    option_user.click()
    # there is issue in the cross button, so clicking somewhere else to close the dropdown
    password_input.click()

    # Save button
    save_button = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[13]/span/div/button[2]")
    save_button.click()
    automation.delay(3)
    browser.refresh()
    # Assert below
    if browser.find_element_by_xpath("//*[contains(text(),'" + data.new_user + "')]").is_displayed():
        print("User is added and displayed successfully")
    else:
        print("Test failed: user added is not getting displayed")
# Test Case 2: Add the new user in DM
def test_DMNewUser():
    automation.delay(2)
    browser.find_element_by_xpath("//*[contains(text(),'" + data.new_user + "')]").click()
    browser.find_element_by_xpath("//button[contains(text(),'Direct Message')]").click()
    textarea = browser.find_element_by_xpath("//*[@name='msg']")
    textarea.click()
    textarea.send_keys(data.new_message)
    textarea.send_keys(Keys.ENTER)
    automation.delay()
# Test Case 3: Create a new Channel
def test_Channel():
    add_button = browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]")
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
# Test Case 4: Add a user to the channel
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


