import pytest
import os
from selenium import webdriver

@pytest.fixture(params=["Chrome", "Firefox"], scope="class")
def init_driver(request):
    if request.param == "Chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    if request.param == "Firefox":
        path = os.getcwd()
        driver = webdriver.Firefox(service_log_path=path + "/Logs/geckodriver.log")
    # if request.param == "Safari":
    #     driver = webdriver.Safari()
    request.cls.driver = driver
    yield
    driver.close()
