import time
from selenium.webdriver.common.keys import Keys
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
value = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)").text
print(value)
source = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)")
actions.move_to_element(source).perform()
time.sleep(3)
# Hide user
browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(18)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button").click()
browser.find_element_by_xpath("//*[contains(text(),'Hide')]").click()
browser.find_element_by_xpath("//button[contains(text(),'Yes, hide it!')]").click()
time.sleep(5)

# Search user
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[2]").click()
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").click()
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").send_keys(value)
time.sleep(5)
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input").send_keys(Keys.ENTER)
time.sleep(5)

browser.close()
