from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
from messageOperations import MessageOperations
automation = AutomationInit()
browser = automation.getBrowser()
operation = MessageOperations(browser)
automation.login()
value = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(8)").text
print(value)

def goToOption():
    source1 = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(8)")
    browser.execute_script("arguments[0].scrollIntoView(true);", source1)
    automation.delay()
    actions = ActionChains(browser)
    actions.move_to_element(source1).perform()
    automation.delay(3)
    button = browser.find_element_by_css_selector(
        ".rcx-sidebar-item:nth-child(8)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button")
    button.click()

def test_FavoriteUnfavorite():
    goToOption()
    # Favorite a user
    browser.find_element_by_xpath("//*[contains(text(),'Favorite')]").click()
    automation.delay(3)
    # Un-favorite a user
    source2 = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(2)")
    actions = ActionChains(browser)
    actions.move_to_element(source2).perform()
    automation.delay()
    browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(2)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button").click()
    browser.find_element_by_xpath("//*[contains(text(),'Unfavorite')]").click()
    automation.delay(3)

def test_HideShow():
    goToOption()
    automation.delay(3)
    # Hide user
    browser.find_element_by_xpath("//*[contains(text(),'Hide')]").click()
    browser.find_element_by_xpath("//button[contains(text(),'Yes, hide it!')]").click()
    automation.delay(3)

    # Show user
    browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
    browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").click()
    automation.delay(2)
    browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").send_keys(value)
    automation.delay()
    browser.find_element_by_xpath(
        "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").send_keys(Keys.ENTER)
    automation.delay()

def test_ReadUnread():
    goToOption()
    automation.delay(2)
    operation.performReadUnread()
    browser.close()

