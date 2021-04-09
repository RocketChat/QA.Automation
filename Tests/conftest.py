import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as ff_Options
from selenium.webdriver.chrome.options import Options as chrome_Options
import os

global driver
@pytest.fixture(params=[os.environ['BROWSER']], scope="session")
#@pytest.fixture(params=["Chrome", "Firefox", "Safari", "RemoteIE", "RemoteSafari"], scope="class")
def init_driver(request):
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

    """This is BrowserStack Testing"""
    USERNAME = os.environ['BROWSERSTACK_USERNAME']
    ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']
    LOCAL_IDENTIFIER = os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
    BUILD_NAME = os.environ['BROWSERSTACK_BUILD_NAME']
    PROJECT_NAME = os.environ['BROWSERSTACK_PROJECT_NAME']

    BROWSERSTACK_URL = 'http://'+USERNAME+':'+ACCESS_KEY+'@hub-cloud.browserstack.com/wd/hub'

    # if request.param == "RemoteIE":
    #     desired_cap = {
    #         'os': 'Windows',
    #         'os_version': '10',
    #         'browser': 'IE',
    #         'browser_version': '11.0',
    #         'name': "IETesting",
    #         'browserstack.local': 'true',
    #         'browserstack.localIdentifier': LOCAL_IDENTIFIER,
    #         'project': PROJECT_NAME,
    #         'build': BUILD_NAME
    #     }
    #     driver = webdriver.Remote(
    #         command_executor=BROWSERSTACK_URL,
    #         desired_capabilities=desired_cap
    #     )
    #
    # """BrowserStack Safari"""
    # if request.param == "RemoteSafari":
    #     desired_cap = {
    #         'os': 'OS X',
    #         'os_version': 'Catalina',
    #         'resolution': '1920x1080',
    #         'browser': 'Safari',
    #         'browser_version': '13.1',
    #         'name': "SafariTesting",
    #         'browserstack.local': 'true',
    #         'browserstack.localIdentifier': LOCAL_IDENTIFIER,
    #         'project': PROJECT_NAME,
    #         'build': BUILD_NAME
    #     }
    #     driver = webdriver.Remote(
    #         command_executor=BROWSERSTACK_URL,
    #         desired_capabilities=desired_cap
    #     )

    """BrowserStack Chrome"""
    if request.param == "RemoteChrome":
        desired_cap = {
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'name': "ChromeTesting",
            'browserstack.local': 'true',
            'browserstack.localIdentifier': LOCAL_IDENTIFIER,
            'project': PROJECT_NAME,
            'build': BUILD_NAME
        }
        driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            desired_capabilities=desired_cap
        )
    yield
    print("------Teardown------")
    driver.quit()


@pytest.fixture(scope="class")
def init_driver_class(request):
    request.cls.driver = driver
