import pytest
from selenium import webdriver
from browserstack.local import Local


@pytest.fixture(params=["Chrome", "RemoteIE"], scope="class")
def init_driver(request):
    if request.param == "Chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    # if request.param == "Firefox":
    #     path = os.getcwd()
    #     driver = webdriver.Firefox(service_log_path=path + "/Logs/geckodriver.log")
    # if request.param == "Safari":
    #     driver = webdriver.Safari()
    if request.param == "RemoteIE":
        BROWSERSTACK_URL = 'http://rocketchattester1:3qKpZ3j75MbhWztWU1R9@hub-cloud.browserstack.com/wd/hub'

        desired_cap = {

            'os': 'Windows',
            'os_version': '10',
            'browser': 'IE',
            'browser_version': '11.0',
            'name': "rocketchattester1's First Test",
            'browserstack.local': 'true'

        }

        driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            desired_capabilities=desired_cap
        )
    request.cls.driver = driver
    yield
    driver.close()
