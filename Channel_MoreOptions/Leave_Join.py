from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
automation = AutomationInit()
automation.chrome()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

action = ActionChains(browser)
value = browser.find_element_by_css_selector("#rocket-chat > aside > div.rooms-list.sidebar--custom-colors > div > div > div > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > a:nth-child(13) > div > div.rc-box.rcx-box--full.rcx-sidebar-item__container.rcx-sidebar-item__content.undefined > div.rc-box.rcx-box--full.rcx-sidebar-item__title").text
print(value)
source = browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(13)")
action.move_to_element(source).perform()
automation.delay()

# Leave channel
browser.find_element_by_css_selector(".rcx-sidebar-item:nth-child(13)>div.rcx-sidebar-item__wrapper>div.rcx-sidebar-item__content>div.rcx-sidebar-item__menu-wraper>button").click()
browser.find_element_by_xpath("//*[contains(text(),'Leave')]").click()
browser.find_element_by_xpath("//button[contains(text(),'Leave')]").click()
automation.delay()
# Search Channel
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[3]").click()
browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div[3]/form/label/input").click()
browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div[3]/form/label/input").send_keys(value)
browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div[3]/form/label/input").send_keys(Keys.ENTER)
automation.delay()

browser.find_element_by_xpath("//*[@id='rocket-chat']/div[2]/section/div[3]/div/div/div[1]/div[2]/div/div/div/div/table/tbody/tr").click()
automation.delay()
browser.find_element_by_css_selector(".js-join").click()
automation.delay()
browser.close()