import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as ff_Options
from selenium.webdriver.chrome.options import Options as chrome_Options
import os


@pytest.fixture(params=["RemoteChrome", "RemoteIE", "RemoteSafari"], scope="class")
#@pytest.fixture(params=["Chrome", "Firefox", "Safari"], scope="class")
def init_driver(request):
    global driver
    """This checks chrome browser"""
    print("------Setup------")
    # if request.param == "Chrome":
    #     options = chrome_Options()
    #     options.headless = False
    #     prefs = {"profile.default_content_setting_values.notifications": 2}
    #     options.add_experimental_option("prefs", prefs)
    #     driver = webdriver.Chrome(options=options)
    #
    # """This checks Firefox browser"""
    # if request.param == "Firefox":
    #     path = os.getcwd()
    #     options = ff_Options()
    #     options.headless = True
    #     driver = webdriver.Firefox(options=options, service_log_path=path + "/Logs/geckodriver.log")
    #
    # """This checks Safari browser"""
    # if request.param == "Safari":
    #     driver = webdriver.Safari()

    """This is for BrowserStack IE """
    if request.param == "RemoteIE":
        BROWSERSTACK_URL = 'http://rocketchattester1:3qKpZ3j75MbhWztWU1R9@hub-cloud.browserstack.com/wd/hub'
        desired_cap = {
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'IE',
            'browser_version': '11.0',
            'name': "IETesting",
            'build': 'BStack Build Number 1',
            'browserstack.local': 'true'
        }
        driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            desired_capabilities=desired_cap
        )
    """BrowserStack Chrome"""
    if request.param == "RemoteChrome":
        BROWSERSTACK_URL = 'http://rocketchattester1:3qKpZ3j75MbhWztWU1R9@hub-cloud.browserstack.com/wd/hub'
        desired_cap = {
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'Windows',
            'name': 'Chrome Testing',  # test name
            'build': 'BStack Build Number 1',  # CI/CD job or build name
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
                'build': 'BStack Build Number 1',
                'browserstack.local': 'true'
            }
        driver = webdriver.Remote(
                command_executor=BROWSERSTACK_URL,
                desired_capabilities=desired_cap
            )

    request.cls.driver = driver
    yield
    print("------Teardown------")
    driver.quit()
