import pytest
from selenium import webdriver
import os


@pytest.fixture(params=["Chrome", "Firefox", "Safari", "RemoteIE", "RemoteSafari"], scope="class")
def init_driver(request):
    global driver
    """This checks chrome browser"""
    print("------Setup------")
    if request.param == "Chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)

    """This checks Firefox browser"""
    if request.param == "Firefox":
        path = os.getcwd()
        driver = webdriver.Firefox(service_log_path=path + "/Logs/geckodriver.log")

    """This checks Safari browser"""
    if request.param == "Safari":
        driver = webdriver.Safari()

    """This code is for BrowserStack IE """
    if request.param == "RemoteIE":
        BROWSERSTACK_URL = 'http://rocketchattester1:3qKpZ3j75MbhWztWU1R9@hub-cloud.browserstack.com/wd/hub'
        desired_cap = {
            'os': 'Windows',
            'os_version': '10',
            'browser': 'IE',
            'browser_version': '11.0',
            'name': "IETesting",
            'browserstack.local': 'true'
        }
        driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            desired_capabilities=desired_cap
        )
    """BrowserStack Safari"""
    if request.param == "RemoteSafari":
        BROWSERSTACK_URL = 'http://rocketchattester1:3qKpZ3j75MbhWztWU1R9@hub-cloud.browserstack.com/wd/hub'
        desired_cap = {
                'os': 'OS X',
                'os_version': 'Catalina',
                'resolution': '1920x1080',
                'browser': 'Safari',
                'browser_version': '13.1',
                'name': "SafariTesting",
                'browserstack.local': 'true',
            }
        driver = webdriver.Remote(
                command_executor=BROWSERSTACK_URL,
                desired_capabilities=desired_cap
            )

    request.cls.driver = driver
    yield
    print("------Teardown------")
    driver.quit()
