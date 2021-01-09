from selenium.webdriver.common.action_chains import ActionChains
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
automation = AutomationInit()
automation.chrome()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

element = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)")
browser.execute_script("arguments[0].scrollIntoView(true);", element)

automation.delay()
actions = ActionChains(browser)
source1 = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)")
actions.move_to_element(source1).perform()
automation.delay()
# Favorite a user
browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button").click()
browser.find_element_by_xpath("//*[contains(text(),'Favorite')]").click()
automation.delay()
# Unfavorite a user
source2 = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(3)")
actions.move_to_element(source2).perform()
automation.delay()
browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(3)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button").click()
browser.find_element_by_xpath("//*[contains(text(),'Unfavorite')]").click()
automation.delay(3)
browser.close()