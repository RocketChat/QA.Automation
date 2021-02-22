from allure_commons.types import AttachmentType
from Pages.DiscussionDMPage import DiscussionDMPage
from Pages.Loginpage import LoginPage
from Tests.test_base import BaseTest
from Config.main import Data
import allure
data_env = Data()
data = data_env.get_data()


class Test_DiscussionDM(BaseTest):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_discussion(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(data.user_name, data.password)
        self.driver.maximize_window()
        self.discussionDM = DiscussionDMPage(self.driver)
        self.discussionDM.create_discussion(data.channel_name, data.discussion_name, data.new_user, data.discussion_message)
        allure.attach(self.driver.get_screenshot_as_png(), name="CreateDiscussion", attachment_type=AttachmentType.PNG)
        assert self.discussionDM.is_discussion_visible()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_DM(self):
        self.discussionDM = DiscussionDMPage(self.driver)
        self.discussionDM.createDM(data.new_user)
        assert self.discussionDM.is_DM_visible()

