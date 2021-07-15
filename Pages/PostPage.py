from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.main import Data
import time
data_env = Data()
data = data_env.get_data()


class PostPage(BasePage):
    PRIVATE_CHANNEL = (By.XPATH, "//*[contains(text(),'" + data.channel_name + "')]")
    TextArea = (By.XPATH, "//*[@name='msg']")
    MESSAGE_SENT = (By.XPATH, "//*[text()[contains(.,'" + data.message + "')]]")
    PUBLIC_CHANNEL = (By.XPATH, "//*[contains(text(),'general')]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(2)")
    SEARCH_INPUT = (By.XPATH, "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input")
    EMOJI_PICKER = (By.XPATH, "//span[@class='rc-message-box__icon emoji-picker-icon js-emoji-picker']")
    EMOJI_INPUT = (By.XPATH, "//input[@name='name']")
    EMOJI = (By.XPATH, "//*[@data-emoji='smiley']")
    EMOJI_SENT = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child>div>div:last-child>span")
    USER = (By.XPATH, "//*[text()[contains(.,'" + data.user + "')]]")

    def __init__(self, driver):
        super().__init__(driver)

    def post_message_in_private_channel(self, message):
        self.do_click(self.PRIVATE_CHANNEL)
        self.do_click(self.TextArea)
        self.do_send_keys(self.TextArea, message)
        self.do_enter(self.TextArea)
        self.save_screenshot("/Screenshots/MessagePrivate.png")

    def post_message_in_public_channel(self, message):
        self.do_click(self.PUBLIC_CHANNEL)
        self.do_click(self.TextArea)
        self.do_send_keys(self.TextArea, message)
        self.do_enter(self.TextArea)
        self.save_screenshot("/Screenshots/MessagePublic.png")

    def post_emoji(self, emoji):
        self.do_click(self.USER)
        self.do_click(self.TextArea)
        self.do_click(self.EMOJI_PICKER)
        self.do_click(self.EMOJI_INPUT)
        self.do_send_keys(self.EMOJI_INPUT, emoji)
        time.sleep(3)
        self.do_click(self.EMOJI)
        self.do_enter(self.TextArea)
        self.save_screenshot("/Screenshots/MessageEmoji.png")

    def message_sent_is_visible(self):
        return self.is_visible(self.MESSAGE_SENT)

    def emoji_sent_is_visible(self):
        return self.is_visible(self.EMOJI_SENT)






