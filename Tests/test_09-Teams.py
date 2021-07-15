from Pages.TeamsPage import TeamsPage
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
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(data.user_name, data.password)
        # self.driver.maximize_window()
        self.team = TeamsPage(self.driver)
        self.team.add_team(data.team_name, data.team_topic)
        allure.attach(self.driver.get_screenshot_as_png(), name="CreateTeam", attachment_type=AttachmentType.PNG)
        assert self.team.is_team_visible()
        self.team.go_to_Home()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_users_to_team(self):
        self.team = TeamsPage(self.driver)
        self.team.add_members_to_team(data.new_user)
        allure.attach(self.driver.get_screenshot_as_png(), name="AddMember", attachment_type=AttachmentType.PNG)
        assert self.team.is_message_visible()
        self.team.go_to_Home()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_existing_channel_to_team(self):
        self.team = TeamsPage(self.driver)
        self.team.add_existing_channel_to_team(data.channel_name)
        assert self.team.is_channel_visible()
        self.team.go_to_Home()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_new_channel_to_team(self):
        self.team = TeamsPage(self.driver)
        self.team.add_new_channel_to_team(data.new_channel)
        assert self.team.is_new_channel_visible()
        self.team.go_to_Home()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_channel_from_team(self):
        self.team = TeamsPage(self.driver)
        self.team.remove_channel_from_team()
        self.team.go_to_Home()

    @allure.severity(allure.severity_level.NORMAL)
    def test_convert_channel_to_team(self):
        self.team = TeamsPage(self.driver)
        self.team.convert_channel_to_team(data.channel2team)
        time.sleep(3)
        self.team.go_to_Home()

    @allure.severity(allure.severity_level.NORMAL)
    def test_move_to_team(self):
        self.team = TeamsPage(self.driver)
        self.team.move_channel_to_team(data.channel, data.team_name)
        assert self.team.is_channel_moved()
        time.sleep(3)
        self.team.go_to_Home()

    @allure.severity(allure.severity_level.NORMAL)
    def test_edit_team(self):
        self.team = TeamsPage(self.driver)
        self.team.edit_team(data.new_name)
        assert self.team.is_change_visible()
        self.team.go_to_Home()




