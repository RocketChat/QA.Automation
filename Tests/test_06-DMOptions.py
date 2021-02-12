import time
from Pages.DMOptionsPage import DMOptionsPage
from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data

data_env = Data()
data = data_env.get_data()


class Test_DMOptions(BaseTest):

    def test_perform_read_unread_user(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        self.driver.maximize_window()
        self.dmOption = DMOptionsPage(self.driver)
        self.dmOption.go_to_option()
        label1 = self.dmOption.get_button_label()
        self.dmOption.performReadUnread()
        time.sleep(2)
        self.dmOption.go_to_option()
        label2 = self.dmOption.get_button_label()
        assert (label1 != label2)

    def test_perform_favorite_unfavorite_user(self):
        self.dmOption = DMOptionsPage(self.driver)
        value = self.dmOption.get_label_text()
        self.dmOption.go_to_option()
        self.dmOption.perform_favorite()
        assert self.dmOption.favorite_item_label() == value
        self.dmOption.perform_unfavorite()
        self.dmOption.go_to_option()
        assert self.dmOption.is_favorite_button_displayed()

    def test_perform_hide_show_user(self):
        self.dmOption = DMOptionsPage(self.driver)
        self.dmOption.go_to_option()
        self.dmOption.perform_hide()
        value = self.dmOption.get_label_text()
        print(value)
        self.dmOption.perform_show(value)
        assert value
