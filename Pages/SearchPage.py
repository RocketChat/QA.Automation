from selenium.webdriver.common.by import By
import time

from Pages.BasePage import BasePage
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class SearchPage(BasePage):
    HEADER = (By.CSS_SELECTOR, ".rc-header")
    HOME_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(1)")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(2)")
    SEARCH_INPUT = (By.XPATH, "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input")
    TEXTAREA = (By.XPATH, "//textarea[@name='msg']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def is_home_icon_displayed(self):
        return self.is_visible(self.HOME_BUTTON)

    def is_search_icon_displayed(self):
        return self.is_visible(self.SEARCH_BUTTON)

    def perform_search_user(self, user):
        self.do_click(self.SEARCH_BUTTON)
        self.do_click(self.SEARCH_INPUT)
        self.do_send_keys(self.SEARCH_INPUT, user)
        time.sleep(5)
        self.save_screenshot("/Screenshots/SearchUser.png")
        self.do_enter(self.SEARCH_INPUT)
        time.sleep(5)

    def perform_search_private_channel(self, channelName):
        self.do_click(self.SEARCH_BUTTON)
        self.do_click(self.SEARCH_INPUT)
        self.do_send_keys(self.SEARCH_INPUT, channelName)
        time.sleep(5)
        self.save_screenshot("/Screenshots/SearchPrivateChannel.png")
        self.do_enter(self.SEARCH_INPUT)
        time.sleep(5)

    def perform_search_public_channel(self, publicChannel):
        self.do_click(self.SEARCH_BUTTON)
        self.do_click(self.SEARCH_INPUT)
        self.do_send_keys(self.SEARCH_INPUT, publicChannel)
        time.sleep(5)
        self.save_screenshot("/Screenshots/SearchPublicChannel.png")
        self.do_enter(self.SEARCH_INPUT)
        time.sleep(5)

    def is_textarea_visible(self):
        return self.is_visible(self.TEXTAREA)





