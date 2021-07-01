from Pages.DeleteDataPage import DeleteDataPage
from Pages.LoginLogoutPage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
import allure
import time
import pytest
from allure_commons.types import AttachmentType
data_env = Data()
data = data_env.get_data()


class Test_Delete(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(data.user_name, data.password)
        self.delete = DeleteDataPage(self.driver)
        self.delete.Delete_user()
        #assert self.delete.user_not_displayed()

    def test_delete_channel(self):
        self.delete = DeleteDataPage(self.driver)
        self.delete.Delete_channel()
        #assert self.delete.channel_not_displayed()

    def test_delete_team(self):
        self.delete = DeleteDataPage(self.driver)
        self.delete.Delete_team()
        #assert self.delete.team_not_displayed()
