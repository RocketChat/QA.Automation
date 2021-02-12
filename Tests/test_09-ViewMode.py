from Pages.Loginpage import LoginPage
from Pages.ViewModePage import ViewModePage
from Tests.test_base import BaseTest
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class Test_ViewMode(BaseTest):

    def test_extended_mode(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        self.driver.maximize_window()
        self.viewMode = ViewModePage(self.driver)
        self.viewMode.select_Extended_Mode()
        self.viewMode.double_click_home()

    def test_medium_mode(self):
        self.viewMode = ViewModePage(self.driver)
        self.viewMode.select_Medium_Mode()
        self.viewMode.double_click_home()

    def test_condensed_mode(self):
        self.viewMode = ViewModePage(self.driver)
        self.viewMode.select_Condensed_Mode()
        self.viewMode.double_click_home()
