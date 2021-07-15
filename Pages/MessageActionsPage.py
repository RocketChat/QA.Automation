from selenium.webdriver.common.by import By
import time
from Pages.BasePage import BasePage
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class MessageActionsPage(BasePage):
    USER = (By.XPATH, "//*[contains(text(),'" + data.new_username + "')]")
    TEXTAREA = (By.XPATH, "//*[@name='msg']")
    SOURCE = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child")
    ACTION_ONE = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child> div.message-actions > div.message-actions__buttons > button:nth-child(1)")
    QUOTE = (By.XPATH, "//*[text()[contains(.,'Testing quote')]]")

    ACTION_TWO = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child> div.message-actions > div.message-actions__buttons > button:nth-child(2)")
    EMOJI_INPUT = (By.XPATH, "//input[@name='name']")
    EMOJI = (By.XPATH, "//*[@data-emoji='smiley']")
    EMOJI_REPLY = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child>.reactions")

    ACTION_THREE = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child> div.message-actions > div.message-actions__buttons > button:nth-child(3)")
    THREAD_INPUT = (By.CSS_SELECTOR, "section > div.rc-message-box.rc-new > label >textarea")
    CLOSE_BUTTON = (By.CSS_SELECTOR, ".rcx-box >div>h3>div>div> button:nth-child(2)")
    MESSAGE_REPLY = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child>.thread-replied>span>span")

    def __init__(self, driver):
        super().__init__(driver)

    def send_message(self, message):
        self.do_click(self.USER)
        self.do_click(self.TEXTAREA)
        self.do_send_keys(self.TEXTAREA, message)
        self.do_enter(self.TEXTAREA)
        time.sleep(3)

    def mouse_over_message(self):
        self.mouse_over(self.SOURCE)

    def add_quote(self, quote):
        self.do_click(self.ACTION_ONE)
        self.do_click(self.TEXTAREA)
        self.do_send_keys(self.TEXTAREA, quote)
        self.do_enter(self.TEXTAREA)
        time.sleep(3)
        self.save_screenshot("/Screenshots/Quote.png")

    def click_user(self):
        self.do_click(self.USER)

    def add_reaction(self, emoji):
        self.do_click(self.ACTION_TWO)
        self.do_click(self.EMOJI_INPUT)
        self.do_send_keys(self.EMOJI_INPUT, emoji)
        time.sleep(3)
        self.do_click(self.EMOJI)
        time.sleep(3)
        self.save_screenshot("/Screenshots/Emoji.png")

    def reply_in_thread(self, reply):
        self.do_click(self.ACTION_THREE)
        self.do_click(self.THREAD_INPUT)
        self.do_send_keys(self.THREAD_INPUT, reply)
        self.do_enter(self.THREAD_INPUT)
        time.sleep(3)
        self.save_screenshot("/Screenshots/Thread.png")
        self.do_click(self.CLOSE_BUTTON)
        time.sleep(3)

    def is_quote_visible(self):
        return self.is_visible(self.QUOTE)

    def is_emoji_visible(self):
        return self.is_visible(self.EMOJI_REPLY)

    def is_reply_in_thread_visible(self):
        return self.is_visible(self.MESSAGE_REPLY)
