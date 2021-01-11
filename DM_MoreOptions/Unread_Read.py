from selenium.webdriver.common.action_chains import ActionChains
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
from messageOperations import MessageOperations
automation = AutomationInit()
automation.chrome()
browser = automation.getBrowser()
operation = MessageOperations(browser)
automation.login()
browser.implicitly_wait(10)

element = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)")
browser.execute_script("arguments[0].scrollIntoView(true);", element)

automation.delay()
actions = ActionChains(browser)
source = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)")
actions.move_to_element(source).perform()
automation.delay()

browser.find_element_by_css_selector(
            ".rcx-sidebar-item:nth-child(18)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button").click()

operation.performReadUnread()
browser.close()