from Pages.ChatActionsPage import ChatActionsPage
from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
import allure
data_env = Data()
data = data_env.get_data()


class Test_ChatActions(BaseTest):
    @allure.severity(allure.severity_level.NORMAL)
    def test_post_message(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        self.driver.maximize_window()
        self.chat = ChatActionsPage(self.driver)
        self.chat.post_message(data.message)
        assert self.chat.message_sent_is_visible()

    def test_send_audio(self):
        self.chat = ChatActionsPage(self.driver)
        self.chat.send_audio(data.caption)
        assert self.chat.audio_sent_is_visible()



