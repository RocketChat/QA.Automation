from Pages.CreateDataPage import CreateDataPage
from Pages.LoginLogoutPage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
import allure
import time
import pytest
from allure_commons.types import AttachmentType
data_env = Data()
data = data_env.get_data()


class Test_Create(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_new_user(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        self.create = CreateDataPage(self.driver)
        self.create.add_new_user(data.new_user, data.new_username, data.new_email, data.new_status, data.new_bio, data.new_nickname, data.new_password)
        allure.attach(self.driver.get_screenshot_as_png(), name="CreateUser", attachment_type=AttachmentType.PNG)
        assert self.create.is_user_visible()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_new_DM(self):
        self.create = CreateDataPage(self.driver)
        self.create.dm_new_user(data.new_message)
        assert self.create.is_user_displayed()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_new_channel(self):
        self.driver.maximize_window()
        self.create = CreateDataPage(self.driver)
        self.create.go_to_Home()
        time.sleep(3)
        self.create.add_new_channel(data.channel_name, data.new_user)
        assert self.create.is_channel_visible()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_users_to_channel(self):
        self.create = CreateDataPage(self.driver)
        self.create.add_users_to_channel(data.new_user)
        allure.attach(self.driver.get_screenshot_as_png(), name="AddUser", attachment_type=AttachmentType.PNG)
        assert self.create.is_message_visible()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_discussion(self):
        self.create = CreateDataPage(self.driver)
        self.create.go_to_Home()
        time.sleep(3)
        self.create.add_discussion(data.channel_name, data.discussion_name, data.new_user, data.discussion_message)
        allure.attach(self.driver.get_screenshot_as_png(), name="CreateDiscussion", attachment_type=AttachmentType.PNG)
        assert self.create.is_discussion_visible()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_DM(self):
        self.create = CreateDataPage(self.driver)
        self.create.add_DM(data.new_user)
        assert self.create.is_DM_visible()
