import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
from automation_init import AutomationInit

def test_withRocketChat():
    automation = AutomationInit()
    browser = automation.getBrowser()
    automation.login()
    browser.save_screenshot("/Users/ishratmanzoor/Desktop/QA.Automation/Screenshots/Login.png")
    automation.delay()
    browser.close()

def test_withGoogle():
    automation = AutomationInit()
    user_name = "meherishrat@gmail.com"
    password = "Welcome@123"
    browser = automation.getBrowser()

    automation.delay()
    browser.find_element_by_xpath("//*[@id='login-card']/div[1]/button[3]").click()
    automation.delay(3)
    browser.switch_to.window(browser.window_handles[1])
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='identifierId']").click()
    browser.find_element_by_xpath("//*[@id='identifierId']").send_keys(user_name)
    browser.find_element_by_css_selector("#identifierNext > div > button").click()
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").click()
    browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(password)
    browser.find_element_by_css_selector("#passwordNext > div > button").click()
    automation.delay()
    browser.quit()





