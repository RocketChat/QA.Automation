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
    add_button = browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/div/div/main/div/aside/footer/button")
    add_button.click()
    # add assert here that the user is already added
    home = browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[1]")
    home.click()
    automation.delay(3)
    browser.close()


