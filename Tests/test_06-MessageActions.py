from allure_commons.types import AttachmentType
from Pages.LoginLogoutPage import LoginPage
from Pages.MessageActionsPage import MessageActionsPage
from Tests.test_base import BaseTest
from Config.main import Data
import allure
import time
data_env = Data()
data = data_env.get_data()


class Test_MessageActions(BaseTest):
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_quote(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(data.user_name, data.password)
        # self.driver.maximize_window()
        self.messageActions = MessageActionsPage(self.driver)
        self.messageActions.send_message(data.message)
        self.messageActions.mouse_over_message()
        time.sleep(2)
        self.messageActions.add_quote(data.QUOTE)
        allure.attach(self.driver.get_screenshot_as_png(), name="Quote", attachment_type=AttachmentType.PNG)
        assert self.messageActions.is_quote_visible()

    @allure.severity(allure.severity_level.NORMAL)
    def test_add_reaction(self):
        self.messageActions = MessageActionsPage(self.driver)
        self.messageActions.click_user()
        self.messageActions.mouse_over_message()
        self.messageActions.add_reaction(data.EMOJI_SEARCH)
        allure.attach(self.driver.get_screenshot_as_png(), name="Reaction", attachment_type=AttachmentType.PNG)
        assert self.messageActions.is_emoji_visible()

    @allure.severity(allure.severity_level.NORMAL)
    def test_reply_in_thread(self):
        self.messageActions = MessageActionsPage(self.driver)
        self.messageActions.click_user()
        self.messageActions.mouse_over_message()
        self.messageActions.reply_in_thread(data.REPLY_IN_THREAD)
        allure.attach(self.driver.get_screenshot_as_png(), name="Thread", attachment_type=AttachmentType.PNG)
        assert self.messageActions.is_reply_in_thread_visible()
