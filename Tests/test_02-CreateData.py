from Pages.CreateDataPage import CreateDataPage
from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class Test_Create(BaseTest):
    def test_create_new_user(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        self.driver.maximize_window()
        self.create = CreateDataPage(self.driver)
        self.create.add_new_user(data.new_user, data.new_username, data.new_email, data.new_status, data.new_bio, data.new_nickname, data.new_password)
        assert self.create.is_user_visible()

    def test_new_DM(self):
        self.create = CreateDataPage(self.driver)
        self.create.dm_new_user(data.new_message)

    def test_add_new_channel(self):
        self.create = CreateDataPage(self.driver)
        self.create.add_new_channel(data.channel_name, data.new_user)
        assert self.create.is_channel_visible()

    def test_add_users_to_channel(self):
        self.create = CreateDataPage(self.driver)
        self.create.add_users_to_channel(data.new_user)
        assert self.create.is_message_visible()
