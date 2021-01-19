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
# test cases specifically for local
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
    browser.refresh()
    # add assert here
    automation.delay()

def test_DMNewUser():
    automation.delay()
    browser.find_element_by_xpath("//*[contains(text(),'" + data.new_user + "')]").click()
    browser.find_element_by_xpath("//button[contains(text(),'Direct Message')]").click()
    textarea = browser.find_element_by_xpath("//*[@name='msg']")
    textarea.click()
    textarea.send_keys(data.new_message)
    textarea.send_keys(Keys.ENTER)
    automation.delay()
    browser.close()

