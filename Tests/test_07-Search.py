import allure
import pytest
from allure_commons.types import AttachmentType
from Pages.SearchPage import SearchPage
from Pages.LoginLogoutPage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class Test_Home(BaseTest):
    @allure.severity(allure.severity_level.NORMAL)
    def test_homepage_title(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(data.user_name, data.password)
        # self.driver.maximize_window()
        pytest.skip("test")
        self.search = SearchPage(self.driver)
        self.search.save_screenshot("/Screenshots/Homepage.png")
        header = self.search.get_header_value()
        print(header)
        allure.attach(self.driver.get_screenshot_as_png(), name="Homepage", attachment_type=AttachmentType.PNG)
        assert header == data.HOMEPAGE_HEADER

    @allure.severity(allure.severity_level.NORMAL)
    def test_home_icon(self):
        self.search = SearchPage(self.driver)
        assert self.search.is_home_icon_displayed()

    @allure.severity(allure.severity_level.NORMAL)
    def test_search_icon(self):
        self.search = SearchPage(self.driver)
        assert self.search.is_search_icon_displayed()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_user(self):
        self.search = SearchPage(self.driver)
        self.search.perform_search_user(data.user)
        assert self.search.is_textarea_visible()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_private_channel(self):
        self.search = SearchPage(self.driver)
        self.search.perform_search_private_channel(data.channel_name)
        assert self.search.is_textarea_visible()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_public_channel(self):
        self.search = SearchPage(self.driver)
        self.search.perform_search_public_channel(data.PUBLIC_CHANNEL)
        assert self.search.is_textarea_visible()
