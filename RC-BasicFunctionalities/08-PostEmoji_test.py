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

def test_PostEmoji():
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
    search_input = browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input")

    automation.delay(2)
    search_input.click()
    automation.delay(2)
    search_input.send_keys(data.new_user)
    automation.delay()
    search_input.send_keys(Keys.ENTER)
    automation.delay()
    browser.find_element_by_xpath("//*[@name='msg']").click()
    browser.find_element_by_xpath("//span[@class='rc-message-box__icon emoji-picker-icon js-emoji-picker']").click()
    browser.find_element_by_xpath("//input[@name='name']").click()
    browser.find_element_by_xpath("//input[@name='name']").send_keys("Smiley")
    automation.delay()
    browser.find_element_by_xpath("//*[@data-emoji='smiley']").click()
    automation.delay()
    browser.find_element_by_xpath("//*[@name='msg']").send_keys(Keys.ENTER)
    automation.delay()
    # Assert below
    emoji = browser.find_element_by_css_selector(".wrapper>ul>li:last-child>div>div:last-child>span")
    assert emoji
    print("emoji posted successfully")
    automation.logout()
    automation.delay()
    browser.close()

