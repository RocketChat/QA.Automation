import sys, os
from selenium.common.exceptions import NoSuchElementException
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from messageOperations import MessageOperations

automation = AutomationInit()
browser = automation.getBrowser()
operation = MessageOperations(browser)
automation.login()

value = browser.find_element_by_css_selector(
        "#rocket-chat > aside > div.rooms-list.sidebar--custom-colors > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > a:nth-child(2) > div > div.rc-box.rcx-box--full.rcx-sidebar-item__container.rcx-sidebar-item__content.undefined > div.rc-box.rcx-box--full.rcx-sidebar-item__title").text
print(value)

def goToOption():
    # on open RC consider nth-child(13)
    source1 = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(2)")
    browser.execute_script("arguments[0].scrollIntoView(true);", source1)
    automation.delay()
    actions = ActionChains(browser)
    actions.move_to_element(source1).perform()
    automation.delay(3)
    button = browser.find_element_by_css_selector(
        ".rcx-sidebar-item:nth-child(2)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button")
    button.click()

def test_FavoriteUnfavorite():
    goToOption()
    # Favorite a channel
    browser.find_element_by_xpath("//*[contains(text(),'Favorite')]").click()
    automation.delay(3)

    # Un-favorite a Channel
    # on open RC consider nth-child(3) for un-favorite action
    source2 = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(2)")
    actions = ActionChains(browser)
    actions.move_to_element(source2).perform()
    automation.delay(3)
    browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(2)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button").click()
    browser.find_element_by_xpath("//*[contains(text(),'Unfavorite')]").click()
    automation.delay(3)

def test_HideShow():
    goToOption()

    # Hide channel
    browser.find_element_by_xpath("//*[contains(text(),'Hide')]").click()
    browser.find_element_by_xpath("//button[contains(text(),'Yes, hide it!')]").click()
    automation.delay(3)
    # Assert below
    try:
        channel = browser.find_element_by_xpath("//*[contains(text(),'" + value + "')]")
        if channel.is_displayed():
            print("test case failed, channel is still displayed")
            sys.exit()
    except NoSuchElementException:
        print("channel is hidden successfully")

    # Show a channel
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
    browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").click()
    browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").send_keys(value)
    automation.delay()
    browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").send_keys(Keys.ENTER)
    # Assert below
    browser.find_element_by_xpath("//*[contains(text(),'" + value + "')]").is_displayed()
    print("channel retrieved successfully")
    automation.delay()

def test_ReadUnread():
    goToOption()
    button_label = browser.find_element_by_css_selector("body > div:nth-child(23) > div > div > ol > li:nth-child(2)").text
    operation.performReadUnread()
    # Assert below
    goToOption()
    new_label = browser.find_element_by_css_selector("body > div:nth-child(23) > div > div > ol > li:nth-child(2)").text
    if button_label == new_label:
        print("Test Failed: Button label is not changed")
    else:
        print("Test Passed: Button label changed successfully")
    browser.close()
