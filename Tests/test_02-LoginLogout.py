from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class Test_Login(BaseTest):

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(data.LOGIN_PAGE_TITLE)
        self.loginPage.save_screenshot("/Screenshots/Login.png")
        assert title == data.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        self.driver.maximize_window()

    def test_logout(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_logout()
        assert self.loginPage.is_logout_successful()
