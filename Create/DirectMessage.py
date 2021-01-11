from selenium.webdriver.common.keys import Keys
import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit
automation = AutomationInit()
automation.safari()
#automation.chrome()
#automation.safari()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)
user = "meherishrat"

browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]").click()
browser.find_element_by_xpath("//*[contains(text(),'Direct Messages')]").click()
browser.find_element_by_xpath("//*[@id='directMessageUsers']").click()
browser.find_element_by_xpath("//*[@id='directMessageUsers']").send_keys(user)
automation.delay(3)
browser.find_element_by_xpath("//*[@id='directMessageUsers']").send_keys(Keys.ENTER)
automation.delay(2)
browser.save_screenshot("/Users/ishratmanzoor/Desktop/QA.Automation/Screenshots/DMscreen.png")
#browser.get_screenshot_as_file("screenDm.png")
browser.find_element_by_xpath("//button[@form='create-dm']").click()
status = browser.find_element_by_xpath("//textarea[@name='msg']").is_displayed()
print(status)
automation.delay()
browser.close()