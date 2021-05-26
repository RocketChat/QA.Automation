from Pages.AddTeamPage import AddTeamPage
from Pages.LoginLogoutPage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
import allure
import time
import pytest
from allure_commons.types import AttachmentType
data_env = Data()
data = data_env.get_data()


class Test_Team(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_new_team(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        self.team = AddTeamPage(self.driver)
        self.team.add_team(data.team_name, data.team_topic)
        allure.attach(self.driver.get_screenshot_as_png(), name="CreateTeam", attachment_type=AttachmentType.PNG)
        assert self.team.is_team_visible()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_users_to_team(self):
        self.team = AddTeamPage(self.driver)
        self.team.add_members_to_team(data.new_user)
        allure.attach(self.driver.get_screenshot_as_png(), name="AddMember", attachment_type=AttachmentType.PNG)
        assert self.team.is_message_visible()

