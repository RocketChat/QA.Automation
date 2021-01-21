from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
sys.path.append(os.path.abspath('../Data'))
from automation_init import AutomationInit
from Data import main
data = main.main()

automation = AutomationInit()
browser = automation.getBrowser()
automation.login()

def test_AddQuote():
    browser.find_element_by_xpath("//*[contains(text(),'" + data.new_username + "')]").click()
    automation.delay()
    browser.find_element_by_xpath("//*[@name='msg']").click()
    browser.find_element_by_xpath("//*[@name='msg']").send_keys(data.message)
    browser.find_element_by_xpath("//*[@name='msg']").send_keys(Keys.ENTER)
    action = ActionChains(browser)
    source = browser.find_element_by_css_selector(".wrapper>ul>li:last-child")
    action.move_to_element(source).perform()
    browser.find_element_by_css_selector(".wrapper>ul>li:last-child> div.message-actions > div.message-actions__buttons > button:nth-child(1)").click()
    browser.find_element_by_xpath("//textarea[@name='msg']").click()
    browser.find_element_by_xpath("//textarea[@name='msg']").send_keys("Testing quote")
    browser.find_element_by_xpath("//textarea[@name='msg']").send_keys(Keys.ENTER)
    automation.delay()
    assert browser.find_element_by_xpath("//*[text()[contains(.,'Testing quote')]]")

def test_AddReaction():

    action = ActionChains(browser)
    browser.find_element_by_xpath("//*[contains(text(),'" + data.new_username + "')]").click()
    automation.delay()
    source = browser.find_element_by_css_selector(".wrapper>ul>li:last-child")
    action.move_to_element(source).perform()
    browser.find_element_by_css_selector(
        ".wrapper>ul>li:last-child> div.message-actions > div.message-actions__buttons > button:nth-child(2)").click()
    browser.find_element_by_xpath("//input[@name='name']").click()
    browser.find_element_by_xpath("//input[@name='name']").send_keys("Smiley")
    automation.delay()
    browser.find_element_by_xpath("//*[@data-emoji='smiley']").click()
    automation.delay()
    emoji_reply = browser.find_element_by_css_selector(".wrapper>ul>li:last-child>.reactions")
    assert emoji_reply

def test_ReplyInThread():

    action = ActionChains(browser)
    browser.find_element_by_xpath("//*[contains(text(),'" + data.new_username + "')]").click()
    automation.delay()
    source = browser.find_element_by_css_selector(".wrapper>ul>li:last-child")
    action.move_to_element(source).perform()
    browser.find_element_by_css_selector(
        ".wrapper>ul>li:last-child> div.message-actions > div.message-actions__buttons > button:nth-child(3)").click()
    browser.find_element_by_css_selector("section > div.rc-message-box.rc-new > label >textarea").click()
    automation.delay()
    browser.find_element_by_css_selector("section > div.rc-message-box.rc-new > label >textarea").send_keys(
        "Testing reply in thread")
    browser.find_element_by_css_selector("section > div.rc-message-box.rc-new > label >textarea").send_keys(Keys.ENTER)
    browser.find_element_by_css_selector(".rcx-box >div>h3>div>div> button:nth-child(2)").click()
    automation.delay()
    # Assert below
    reply_message = browser.find_element_by_css_selector(".wrapper>ul>li:last-child>.thread-replied>span>span")
    if reply_message.is_displayed():
        print("Test Passed")
    else:
        print("Test Failed")
    browser.close()
