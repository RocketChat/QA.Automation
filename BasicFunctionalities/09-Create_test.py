from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
automation = AutomationInit()
browser = automation.getBrowser()
automation.login()
channelName = "TesttChannell"
user = "meherishrat"
discussionName = "DiscussionTestt"
discussionMessage = "TestDiscussion"
add_button = browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]")

def test_Channel():
    add_button.click()
    browser.find_element_by_xpath("//span[contains(text(),'Channel')]").click()
    automation.delay()
    browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[1]/label/div[2]/input").click()
    browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[1]/label/div[2]/input").send_keys(channelName)
    browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input").click()
    browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input").send_keys(user)
    automation.delay()
    browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input").send_keys(Keys.ENTER)
    browser.find_element_by_xpath("//*[@id='create-channel']/div[3]/input").click()
    automation.delay()

def test_Discussion():

    add_button.click()
    browser.find_element_by_xpath("//span[contains(text(),'Discussion')]").click()
    automation.delay()
    browser.find_element_by_xpath("//*[@id='parentChannel']").click()
    browser.find_element_by_xpath("//*[@id='parentChannel']").send_keys(channelName)

    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='parentChannel']").send_keys(Keys.ENTER)
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='discussion_name']").click()
    browser.find_element_by_xpath("//*[@id='discussion_name']").send_keys(discussionName)
    browser.find_element_by_xpath("//*[@id='users']").click()
    browser.find_element_by_xpath("//*[@id='users']").send_keys(user)
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='users']").send_keys(Keys.ENTER)

    browser.find_element_by_xpath("//*[@id='discussion_message']").click()
    browser.find_element_by_xpath("//*[@id='discussion_message']").send_keys(discussionMessage)
    browser.find_element_by_xpath("//button[@form='create-discussion']").click()
    automation.delay(3)

def test_DM():
    add_button.click()
    automation.delay(3)
    browser.find_element_by_xpath("//*[contains(text(),'Direct Messages')]").click()
    browser.find_element_by_xpath("//*[@id='directMessageUsers']").click()
    browser.find_element_by_xpath("//*[@id='directMessageUsers']").send_keys(user)
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='directMessageUsers']").send_keys(Keys.ENTER)
    automation.delay(2)
    browser.save_screenshot("/Users/ishratmanzoor/Desktop/QA.Automation/Screenshots/DMscreen.png")
    # browser.get_screenshot_as_file("screenDm.png")
    browser.find_element_by_xpath("//button[@form='create-dm']").click()
    status=browser.find_element_by_xpath("//textarea[@name='msg']").is_displayed()
    print(status)
    automation.delay()
    browser.close()
