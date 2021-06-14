import allure
from allure_commons.types import AttachmentType
from Pages.LoginLogoutPage import LoginPage
from Pages.ViewModePage import ViewModePage
from Tests.test_base import BaseTest
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class Test_ViewMode(BaseTest):

    @allure.severity(allure.severity_level.NORMAL)
    def test_extended_mode(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(data.user_name, data.password)
        # self.driver.maximize_window()
        self.viewMode = ViewModePage(self.driver)
        self.viewMode.select_Extended_Mode()
        allure.attach(self.driver.get_screenshot_as_png(), name="ExtendedMode", attachment_type=AttachmentType.PNG)
        self.viewMode.double_click_home()

    @allure.severity(allure.severity_level.NORMAL)
    def test_medium_mode(self):
        self.viewMode = ViewModePage(self.driver)
        self.viewMode.select_Medium_Mode()
        allure.attach(self.driver.get_screenshot_as_png(), name="MediumMode", attachment_type=AttachmentType.PNG)
        self.viewMode.double_click_home()

    @allure.severity(allure.severity_level.NORMAL)
    def test_condensed_mode(self):
        self.viewMode = ViewModePage(self.driver)
        self.viewMode.select_Condensed_Mode()
        allure.attach(self.driver.get_screenshot_as_png(), name="CondensedMode", attachment_type=AttachmentType.PNG)
        self.viewMode.double_click_home()
