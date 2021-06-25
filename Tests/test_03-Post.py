from Pages.LoginLogoutPage import LoginPage
from Pages.PostPage import PostPage
from Tests.test_base import BaseTest
from Config.main import Data
import allure
data_env = Data()
data = data_env.get_data()


class Test_Post(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_post_in_private_channel(self):
        # self.loginPage = LoginPage(self.driver)
        # self.loginPage.do_login(data.user_name, data.password)
        # self.driver.maximize_window()
        self.post = PostPage(self.driver)
        self.post.post_message_in_private_channel(data.message)
        assert self.post.message_sent_is_visible()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_post_message_in_public_channel(self):
        self.post = PostPage(self.driver)
        self.post.post_message_in_public_channel(data.message)
        assert self.post.message_sent_is_visible()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_post_emoji(self):
        self.post = PostPage(self.driver)
        self.post.post_emoji(data.EMOJI_SEARCH)
        assert self.post.emoji_sent_is_visible()
