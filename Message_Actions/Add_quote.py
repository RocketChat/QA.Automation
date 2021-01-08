from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from automation_init import AutomationInit
automation = AutomationInit()
automation.chrome()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)

action = ActionChains(browser)
browser.find_element_by_xpath("//*[contains(text(),'Meher')]").click()
automation.delay()
source = browser.find_element_by_css_selector(".wrapper>ul>li:last-child")
action.move_to_element(source).perform()
browser.find_element_by_css_selector(".wrapper>ul>li:last-child> div.message-actions > div.message-actions__buttons > button:nth-child(1)").click()
browser.find_element_by_xpath("//textarea[@name='msg']").click()
browser.find_element_by_xpath("//textarea[@name='msg']").send_keys("Testing quote")
browser.find_element_by_xpath("//textarea[@name='msg']").send_keys(Keys.ENTER)
automation.delay()
browser.close()
