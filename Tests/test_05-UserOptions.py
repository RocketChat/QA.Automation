import time
from allure_commons.types import AttachmentType
from Pages.UserOptionsPage import UserOptionsPage
from Pages.LoginLogoutPage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
import allure
import pytest
data_env = Data()
data = data_env.get_data()


class Test_DMOptions(BaseTest):
    @allure.severity(allure.severity_level.NORMAL)
    def test_perform_read_unread_user(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(data.user_name, data.password)
        # self.driver.maximize_window()
        self.dmOptions = UserOptionsPage(self.driver)
        self.dmOptions.double_click_Home()
        self.dmOptions.go_to_option()
        allure.attach(self.driver.get_screenshot_as_png(), name="OptionsDM", attachment_type=AttachmentType.PNG)
        label1 = self.dmOptions.get_button_label()
        print(label1)
        self.dmOptions.performReadUnread()
        self.dmOptions.double_click_Home()
        time.sleep(2)
        self.dmOptions.go_to_option()
        label2 = self.dmOptions.get_button_label()
        assert (label1 != label2)
        time.sleep(2)
        self.dmOptions.double_click_Home()
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    def test_perform_favorite_unfavorite_user(self):
        self.dmOptions = UserOptionsPage(self.driver)
        value = self.dmOptions.get_label_text()
        self.dmOptions.go_to_option()
        self.dmOptions.perform_favorite()
        assert self.dmOptions.favorite_item_label() == value
        self.dmOptions.go_to_Home()
        time.sleep(2)
        self.dmOptions.go_to_option()
        self.dmOptions.perform_unfavorite()
        time.sleep(3)
        self.dmOptions.go_to_Home()
        self.dmOptions.go_to_option()
        assert self.dmOptions.is_favorite_button_displayed()
        self.dmOptions.double_click_Home()
        time.sleep(2)

    @allure.severity(allure.severity_level.NORMAL)
    def test_perform_hide_show_user(self):
        self.dmOptions = UserOptionsPage(self.driver)
        value = self.dmOptions.get_label_text()
        print(value)
        self.dmOptions.go_to_option()
        self.dmOptions.perform_hide()
        self.dmOptions.perform_show(value)
        assert value
