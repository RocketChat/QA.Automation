import time
from selenium.webdriver.common.keys import Keys
from automation_init import AutomationInit
automation = AutomationInit()
browser = automation.getBrowser()
automation.login()
browser.implicitly_wait(10)
channelName = "TesttChannel"

browser.find_element_by_xpath("//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]").click()
browser.find_element_by_xpath("//span[contains(text(),'Channel')]").click()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[1]/label/div[2]/input").click()
browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[1]/label/div[2]/input").send_keys(channelName)
browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input").click()
browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input").send_keys("meherishrat")
time.sleep(5)
browser.find_element_by_xpath("//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input").send_keys(Keys.ENTER)
browser.find_element_by_xpath("//*[@id='create-channel']/div[3]/input").click()
time.sleep(5)
browser.close()