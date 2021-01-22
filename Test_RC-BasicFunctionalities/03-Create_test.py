from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
sys.path.append(os.path.abspath('../Data'))
from automation_init import AutomationInit
from main import TestData
test_data = TestData()
data = test_data.get_data()
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

def test_DM():
    add_button.click()
    automation.delay(3)
    browser.find_element_by_xpath("//*[contains(text(),'Direct Messages')]").click()
    browser.find_element_by_xpath("//*[@id='directMessageUsers']").click()
    browser.find_element_by_xpath("//*[@id='directMessageUsers']").send_keys(data.new_user)
    #browser.find_element_by_xpath("//*[@id='directMessageUsers']").send_keys(data.user)
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='directMessageUsers']").send_keys(Keys.ENTER)
    automation.delay(2)
    browser.save_screenshot(path + "/Screenshots/DM.png")
    # browser.get_screenshot_as_file("screenDm.png")
    browser.find_element_by_xpath("//button[@form='create-dm']").click()
    # Assert below
    status = browser.find_element_by_xpath("//textarea[@name='msg']").is_displayed()
    if status==True:
        print("Test passed: DM created successfully")
    else:
        print("Test failed: DM not created")
    automation.delay()
    browser.close()







