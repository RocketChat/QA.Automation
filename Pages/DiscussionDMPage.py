from selenium.webdriver.common.by import By
import time
from Pages.BasePage import BasePage
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class DiscussionDMPage(BasePage):
    ADD_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]")
    DISCUSSION_BUTTON = (By.XPATH, "//span[contains(text(),'Discussion')]")
    CHANNEL_INPUT = (By.XPATH, "//*[@id='parentChannel']")
    DISCUSSION_INPUT = (By.XPATH, "//*[@id='discussion_name']")
    CHANNEL_USERS_INPUT = (By.XPATH, "//*[@id='users']")
    DISCUSSION_MESSAGE = (By.XPATH, "//*[@id='discussion_message']")
    CREATE__DISCUSSION_BUTTON = (By.XPATH, "//button[@form='create-discussion']")
    CREATED_DISCUSSION = (By.XPATH, "//*[contains(text(),'" + data.discussion_name + "')]")

    DM_BUTTON = (By.XPATH, "//*[contains(text(),'Direct Messages')]")
    DM_USERS_INPUT = (By.XPATH, "//*[@id='directMessageUsers']")
    CREATE_DM_BUTTON = (By.XPATH, "//button[@form='create-dm']")
    TEXTAREA = (By.XPATH, "//textarea[@name='msg']")

    def __init__(self, driver):
        super().__init__(driver)

    def create_discussion(self, channel_name, discussion_name, new_user, discussion_message):
        self.do_click(self.ADD_BUTTON)
        self.do_click(self.DISCUSSION_BUTTON)
        self.do_click(self.CHANNEL_INPUT)
        self.do_send_keys(self.CHANNEL_INPUT, channel_name)
        self.do_enter(self.CHANNEL_INPUT)

        self.do_click(self.DISCUSSION_INPUT)
        self.do_send_keys(self.DISCUSSION_INPUT, discussion_name)

        self.do_click(self.CHANNEL_USERS_INPUT)
        self.do_send_keys(self.CHANNEL_USERS_INPUT, new_user)
        time.sleep(3)
        self.do_enter(self.CHANNEL_USERS_INPUT)

        self.do_click(self.DISCUSSION_MESSAGE)
        self.do_send_keys(self.DISCUSSION_MESSAGE, discussion_message)
        time.sleep(2)

        self.do_click(self.CREATE__DISCUSSION_BUTTON)
        time.sleep(3)

    def is_discussion_visible(self):
        return self.is_visible(self.CREATED_DISCUSSION)

    def createDM(self, new_user):
        self.do_click(self.ADD_BUTTON)
        self.do_click(self.DM_BUTTON)
        self.do_click(self.DM_USERS_INPUT)
        self.do_send_keys(self.DM_USERS_INPUT, new_user)
        time.sleep(3)
        self.do_enter(self.DM_USERS_INPUT)
        self.do_click(self.CREATE_DM_BUTTON)

    def is_DM_visible(self):
        return self.is_visible(self.TEXTAREA)
