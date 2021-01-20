import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from messageOperations import MessageOperations
from selenium.common.exceptions import NoSuchElementException

automation = AutomationInit()
browser = automation.getBrowser()
operation = MessageOperations(browser)
automation.login()
def test_LeaveJoin():
    source1 = browser.find_element_by_xpath("//*[contains(text(), 'general')]")
    browser.execute_script("arguments[0].scrollIntoView(true);", source1)
    automation.delay()
    actions = ActionChains(browser)
    actions.move_to_element(source1).perform()
    automation.delay(3)
    button = browser.find_element_by_css_selector(
        ".rcx-sidebar-item:nth-child(6)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button")
    button.click()
    # Leave channel
    browser.find_element_by_xpath("//*[contains(text(),'Leave')]").click()
    browser.find_element_by_xpath("//button[contains(text(),'Leave')]").click()
    automation.delay()
    # Assert below
    try:
        channel = browser.find_element_by_xpath("//*[contains(text(),'general')]")
        if channel.is_displayed():
            print("test case failed, channel is still displayed")
            sys.exit()
    except NoSuchElementException:
        print("user left the channel successfully")

    # Join Channel
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[3]").click()
    browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div[3]/form/label/input").click()
    browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div[3]/form/label/input").send_keys("general")
    browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div[3]/form/label/input").send_keys(Keys.ENTER)
    automation.delay()

    browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/div[2]/section/div[3]/div/div/div[1]/div[2]/div/div/div/div/table/tbody/tr").click()
    automation.delay()
    browser.find_element_by_css_selector(".js-join").click()
    automation.delay()
    # Assert below
    browser.find_element_by_xpath("//*[contains(text(),'general')]").is_displayed()
    print("user joined back successfully")
    automation.delay()
    browser.close()