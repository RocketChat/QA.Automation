import pytest
from allure_commons.types import AttachmentType
from Pages.LoginLogoutPage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
import allure
data_env = Data()
data = data_env.get_data()


@allure.severity(allure.severity_level.CRITICAL)
class Test_Login(BaseTest):

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_page_title(self):
        pytest.skip("Skipping this test as title is not present in IE")
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(data.LOGIN_PAGE_TITLE)
        print(title)
        allure.attach(self.driver.get_screenshot_as_png(), name="LoginScreen", attachment_type=AttachmentType.PNG)
        assert title == data.LOGIN_PAGE_TITLE

    @allure.severity(allure.severity_level.NORMAL)
    def test_links(self):
        self.loginPage = LoginPage(self.driver)
        assert self.loginPage.is_forgot_password_link_present()
        assert self.loginPage.is_register_account_link_present()

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        allure.attach(self.driver.get_screenshot_as_png(), name="Home", attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_logout()
        assert self.loginPage.is_logout_successful()
