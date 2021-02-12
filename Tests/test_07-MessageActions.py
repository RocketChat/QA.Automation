from Pages.CreateDataPage import CreateDataPage
from Pages.Loginpage import LoginPage
from Pages.MessageActionsPage import MessageActionsPage
from Tests.test_base import BaseTest
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class Test_MessageActions(BaseTest):
    def test_add_quote(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        self.driver.maximize_window()
        self.messageActions = MessageActionsPage(self.driver)
        self.messageActions.send_message(data.message)
        self.messageActions.mouse_over_message()

        self.messageActions.add_quote(data.QUOTE)
        assert self.messageActions.is_quote_visible()

    def test_add_reaction(self):
        self.messageActions = MessageActionsPage(self.driver)
        self.messageActions.click_user()
        self.messageActions.mouse_over_message()
        self.messageActions.add_reaction(data.EMOJI_SEARCH)
        assert self.messageActions.is_emoji_visible()

    def test_reply_in_thread(self):
        self.messageActions = MessageActionsPage(self.driver)
        self.messageActions.click_user()
        self.messageActions.mouse_over_message()
        self.messageActions.reply_in_thread(data.REPLY_IN_THREAD)
        assert self.messageActions.is_reply_in_thread_visible()
