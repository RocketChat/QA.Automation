import time
from selenium.webdriver.common.action_chains import ActionChains
from automation_init import AutomationInit
automation = AutomationInit()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

element = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)")
browser.execute_script("arguments[0].scrollIntoView(true);", element)

time.sleep(5)
actions = ActionChains(browser)
source1 = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)")
actions.move_to_element(source1).perform()
time.sleep(3)
# Favorite a user
browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button").click()
browser.find_element_by_xpath("//*[contains(text(),'Favorite')]").click()
time.sleep(5)
# Unfavorite a user
source2 = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(3)")
actions.move_to_element(source2).perform()
time.sleep(3)
browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(3)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button").click()
browser.find_element_by_xpath("//*[contains(text(),'Unfavorite')]").click()
time.sleep(3)
browser.close()