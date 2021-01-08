from automation_init import AutomationInit
from selenium.webdriver import ActionChains
automation = AutomationInit()
automation.chrome()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

# Extended mode
automation.delay(3)
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[4]").click()
browser.find_element_by_css_selector("body > div.rc-popover.rc-popover-- > div > div > div > ul:nth-child(2) > li:nth-child(1) > label > label").click()
automation.delay(3)
source = browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[1]")
action = ActionChains(browser)
action.double_click(source).perform()

# Medium Mode
automation.delay()
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[4]").click()
browser.find_element_by_css_selector("body > div.rc-popover.rc-popover-- > div > div > div > ul:nth-child(2) > li:nth-child(2) > label > label").click()
automation.delay()
source = browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[1]")
action.double_click(source).perform()

# Condensed Mode
browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[4]").click()
browser.find_element_by_css_selector("body > div.rc-popover.rc-popover-- > div > div > div > ul:nth-child(2) > li:nth-child(3) > label > label").click()
automation.delay(3)
source = browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[1]")
action.double_click(source).perform()
automation.delay()
browser.close()