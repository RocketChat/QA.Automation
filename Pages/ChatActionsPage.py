from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.main import Data
import time
data_env = Data()
data = data_env.get_data()


class ChatActionsPage(BasePage):
    USER = (By.XPATH, "//*[text()[contains(.,'" + data.user + "')]]")
    TextArea = (By.XPATH, "//*[@name='msg']")
    MESSAGE_SENT = (By.XPATH, "//*[text()[contains(.,'" + data.message + "')]]")
    AUDIO = (By.CSS_SELECTOR, ".rc-message-box__audio-message")
    DONE_ICON = (By.CSS_SELECTOR, ".rc-message-box__audio-message.rc-message-box__audio-message--recording > div.rc-message-box__icon.rc-message-box__audio-message-done.js-audio-message-done")
    FILE_DESCRIPTION = (By.XPATH, "//*[@id='file-description']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "body > div.rc-modal-wrapper > dialog > footer > input.rc-button.rc-button--primary.js-confirm")
    AUDIO_SENT = (By.XPATH, "//*[text()[contains(.,'" + data.caption + "')]]")

    def __init__(self, driver):
        super().__init__(driver)

    def post_message(self, message):
        self.do_click(self.USER)
        self.do_click(self.TextArea)
        self.do_send_keys(self.TextArea, message)
        self.do_enter(self.TextArea)

    def message_sent_is_visible(self):
        return self.is_visible(self.MESSAGE_SENT)

    def send_audio(self, caption):
        self.do_click(self.AUDIO)
        time.sleep(30)
        self.do_click(self.DONE_ICON)
        self.do_click(self.FILE_DESCRIPTION)
        self.do_send_keys(self.FILE_DESCRIPTION, caption)
        self.do_click(self.SUBMIT_BUTTON)
        time.sleep(10)

    def audio_sent_is_visible(self):
        return self.is_visible(self.AUDIO_SENT)



