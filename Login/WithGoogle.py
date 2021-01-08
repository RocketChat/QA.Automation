from selenium import webdriver
import time
user_name = "meherishrat@gmail.com"
password = "Welcome@123"

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
#chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://open.rocket.chat/")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='login-card']/div[1]/button[3]").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
driver.find_element_by_xpath("//*[@id='identifierId']").click()
driver.find_element_by_xpath("//*[@id='identifierId']").send_keys(user_name)
driver.find_element_by_css_selector("#identifierNext > div > button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").click()
driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys(password)
driver.find_element_by_css_selector("#passwordNext > div > button").click()
time.sleep(3)
driver.quit()


