import time
from selenium.webdriver.common.action_chains import ActionChains
from automation_init import AutomationInit
from messageOperations import MessageOperations

automation = AutomationInit()
browser = automation.getBrowser()
operation = MessageOperations(browser)

automation.login()
browser.implicitly_wait(10)

action = ActionChains(browser)
source = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(13)")
action.move_to_element(source).perform()
time.sleep(3)
browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(13)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button").click()


operation.performReadUnread()
browser.close()
