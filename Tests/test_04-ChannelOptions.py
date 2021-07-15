from allure_commons.types import AttachmentType
from Pages.ChannelOptionsPage import ChannelOptionsPage
from Pages.LoginLogoutPage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
import time
import allure
import pytest
data_env = Data()
data = data_env.get_data()


class Test_ChannelOptions(BaseTest):
    @allure.severity(allure.severity_level.NORMAL)
    def test_perform_favorite_unfavorite_channel(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(data.user_name, data.password)
        # self.driver.maximize_window()
        self.channelOptions = ChannelOptionsPage(self.driver)
        value = self.channelOptions.get_label_text()
        print(value)
        self.channelOptions.go_to_option()
        allure.attach(self.driver.get_screenshot_as_png(), name="Options", attachment_type=AttachmentType.PNG)
        self.channelOptions.perform_favorite()
        self.channelOptions.save_screenshot("/Screenshots/PerformFavorite.png")
        assert self.channelOptions.favorite_item_label() == value
        self.channelOptions.go_to_Home()
        time.sleep(2)
        self.channelOptions.go_to_option()
        self.channelOptions.perform_unfavorite()
        self.channelOptions.save_screenshot("/Screenshots/PerformFavorite.png")
        time.sleep(3)
        self.channelOptions.go_to_Home()
        self.channelOptions.go_to_option()
        assert self.channelOptions.is_favorite_button_displayed()
        self.channelOptions.double_click_Home()
        time.sleep(2)

    @allure.severity(allure.severity_level.NORMAL)
    def test_perform_read_unread_channel(self):
        self.channelOptions = ChannelOptionsPage(self.driver)
        self.channelOptions.go_to_option()
        label1 = self.channelOptions.get_button_label()
        print(label1)
        self.channelOptions.performReadUnread()
        self.channelOptions.double_click_Home()
        time.sleep(2)
        self.channelOptions.go_to_option()
        label2 = self.channelOptions.get_button_label()
        assert (label1 != label2)
        time.sleep(2)
        self.channelOptions.double_click_Home()
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    def test_perform_hide_show_channel(self):
        self.channelOptions = ChannelOptionsPage(self.driver)
        value = self.channelOptions.get_label_text()
        print(value)
        self.channelOptions.go_to_option()
        self.channelOptions.perform_hide()
        time.sleep(2)
        self.channelOptions.perform_show(value)
        time.sleep(3)

    @allure.severity(allure.severity_level.CRITICAL)
    def test_perform_leave_join_channel(self):
        self.channelOptions = ChannelOptionsPage(self.driver)
        self.channelOptions.go_to_general()
        self.channelOptions.perform_leave()
        self.channelOptions.perform_join(data.PUBLIC_CHANNEL)
        assert self.channelOptions.is_channel_displayed()

