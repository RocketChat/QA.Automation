import pytest
from allure_commons.types import AttachmentType


from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
import allure
data_env = Data()
data = data_env.get_data()


@allure.severity(allure.severity_level.CRITICAL)
class Test_Login(BaseTest):

    @allure.severity(allure.severity_level.NORMAL)
    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(data.LOGIN_PAGE_TITLE)
        self.loginPage.save_screenshot("/Screenshots/Login.png")
        assert title == data.LOGIN_PAGE_TITLE

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        self.driver.maximize_window()
        allure.attach(self.driver.get_screenshot_as_png(), name="Home", attachment_type=AttachmentType.PNG)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout(self):
        #pytest.skip("Skipping this just to check reports")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_logout()
        allure.attach(self.driver.get_screenshot_as_png(), name="LogInScreen", attachment_type=AttachmentType.PNG)
        assert self.loginPage.is_logout_successful()
