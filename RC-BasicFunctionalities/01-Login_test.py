import sys, os
sys.path.append(os.path.abspath('../AutomationModule'))
sys.path.append(os.path.abspath('../Data'))
from automation_init import AutomationInit
from Data import main
data = main.main()
path = os.getcwd()
print("current working directory is: {0}".format(path))
def test_withRocketChat():
    automation = AutomationInit()
    browser = automation.getBrowser()
    automation.delay(2)
    browser.save_screenshot(path + "/Screenshots/Login.png")
    automation.login()
    automation.delay()
    browser.close()

# test for open RC
def test_withGoogle():
    automation = AutomationInit()
    browser = automation.getBrowser()

    automation.delay()
    browser.find_element_by_xpath("//*[@id='login-card']/div[1]/button[3]").click()
    automation.delay(3)
    browser.switch_to.window(browser.window_handles[1])
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='identifierId']").click()
    browser.find_element_by_xpath("//*[@id='identifierId']").send_keys(data.user_name)
    browser.find_element_by_css_selector("#identifierNext > div > button").click()
    automation.delay(3)
    browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").click()
    browser.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(data.password)
    browser.find_element_by_css_selector("#passwordNext > div > button").click()
    automation.delay()
    browser.quit()




