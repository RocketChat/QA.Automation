import allure
from Pages.DirectorySearchPage import DirectorySearchPage
from Pages.LoginLogoutPage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class Test_Directory(BaseTest):
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_channel(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(data.user_name, data.password)
        # self.driver.maximize_window()
        self.search = DirectorySearchPage(self.driver)
        self.search.search_channel(data.channel_name)
        assert self.search.is_channel_name_visible()

    @allure.severity(allure.severity_level.NORMAL)
    def test_search_user(self):
        self.search = DirectorySearchPage(self.driver)
        self.search.search_user(data.user)
        assert self.search.is_user_visible()

    @allure.severity(allure.severity_level.NORMAL)
    def test_search_team(self):
        self.search = DirectorySearchPage(self.driver)
        self.search.search_team(data.team_name)
        assert self.search.is_team_name_visible()

