from selenium.webdriver.common.by import By
import time
from Pages.BasePage import BasePage
from Config.main import Data
from selenium.common.exceptions import NoSuchElementException
data_env = Data()
data = data_env.get_data()


class ChannelOptionsPage(BasePage):
    VALUE = (By.XPATH, "//a[@aria-label='" + data.channel_name + "']//div[@data-qa='sidebar-item-title']")
    CHANNEL = (By.XPATH, "//a[@aria-label='" + data.channel_name + "']/parent::div")
    OPTIONS_BUTTON = (By.XPATH, "//a[@aria-label='" + data.channel_name + "']//button[@class='rcx-box rcx-box--full rcx-box--animated rcx-sidebar-item__menu rcx-button--mini-square rcx-button--square rcx-button--ghost rcx-button rcx-css-ue04py']")
    FAVORITE_BUTTON = (By.XPATH, "//*[contains(text(),'Favorite')]")
    #FAVORITE_ITEM = (By.CSS_SELECTOR, "#rocket-chat > aside > div.rooms-list.sidebar--custom-colors > div > div > div > div.rc-scrollbars-view > div:nth-child(1) > div > div:nth-child(2) > a > div > div.rc-box.rcx-box--full.rcx-sidebar-item__container.rcx-sidebar-item__content.undefined > div.rc-box.rcx-box--full.rcx-sidebar-item__title")
    FAVORITE_ITEM = (By.CSS_SELECTOR, ".rc-scrollbars-view>div>div>div:nth-child(2)>a>div>div:nth-child(2)>div>div:nth-child(2)")
    UNFAVORITE_BUTTON = (By.XPATH, "//*[contains(text(),'Unfavorite')]")
    HOME_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(1)")
    HIDE_OPTION = (By.XPATH, "//*[contains(text(),'Hide')]")
    HIDE_BUTTON = (By.XPATH, "//button[contains(text(),'Yes, hide it!')]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(2)")
    SEARCH_INPUT = (By.XPATH, "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/div/div[1]/div/label/input")
    TEXTAREA = (By.XPATH, "//textarea[@name='msg']")

    """Read and Unread"""
    BUTTON_LABEL = (By.CSS_SELECTOR, "ol > li:nth-child(2) > div > div.rcx-option__content")
    UNREAD_BUTTON = (By.XPATH, "//*[contains(text(),'Mark Unread')]")
    READ_BUTTON = (By.XPATH, "//*[contains(text(),'Mark Read')]")

    """Leave and Join"""
    SOURCE = (By.XPATH, "//a[@aria-label='general']/parent::div")
    OPTIONS_BUTTON_GENERAL = (By.XPATH,
                              "//a[@aria-label='general']//button[@class='rcx-box rcx-box--full rcx-box--animated rcx-sidebar-item__menu rcx-button--mini-square rcx-button--square rcx-button--ghost rcx-button rcx-css-ue04py']")
    LEAVE_OPTION = (By.XPATH, "//*[contains(text(),'Leave')]")
    LEAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Leave')]")
    DIRECTORY = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(3)")
    DIRECTORY_SEARCH_INPUT = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div[3]/form/label/input")
    DIRECTORY_SEARCH_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div[3]/div/div/div[1]/div[2]/div/div/div/div/table/tbody/tr")
    RESULT_1 = (By.CSS_SELECTOR, ".rc-scrollbars-view > div > table > tbody > tr > td:nth-child(1)")
    JOIN_BUTTON = (By.CSS_SELECTOR, ".js-join")
    PUBLIC_CHANNEL = (By.XPATH, "//*[contains(text(),'general')]")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_option(self):
        self.mouse_over(self.CHANNEL)
        time.sleep(2)
        self.do_click(self.OPTIONS_BUTTON)

    def go_to_general(self):
        self.mouse_over(self.SOURCE)
        time.sleep(2)
        self.do_click(self.OPTIONS_BUTTON_GENERAL)

    def go_to_Home(self):
        self.do_click(self.HOME_BUTTON)

    def double_click_Home(self):
        self.do_double_click(self.HOME_BUTTON)

    def perform_leave(self):
        self.do_click(self.LEAVE_OPTION)
        time.sleep(2)
        self.do_click(self.LEAVE_BUTTON)

    def perform_join(self, value):
        time.sleep(3)
        self.do_click(self.DIRECTORY)
        self.do_click(self.DIRECTORY_SEARCH_INPUT)
        self.do_send_keys(self.DIRECTORY_SEARCH_INPUT, value)
        time.sleep(2)
        self.do_enter(self.DIRECTORY_SEARCH_INPUT)
        #self.do_click(self.DIRECTORY_SEARCH_BUTTON)
        time.sleep(2)
        self.do_click(self.RESULT_1)
        time.sleep(2)
        self.do_click(self.JOIN_BUTTON)

    def is_channel_displayed(self):
        return self.is_displayed(self.PUBLIC_CHANNEL)

    def perform_favorite(self):
        self.do_click(self.FAVORITE_BUTTON)
        time.sleep(3)

    def favorite_item_label(self):
        return self.get_element_text(self.FAVORITE_ITEM)

    def perform_unfavorite(self):
        self.do_click(self.UNFAVORITE_BUTTON)

    def is_favorite_button_displayed(self):
        return self.is_displayed(self.FAVORITE_BUTTON)

    def get_label_text(self):
        return self.get_element_text(self.VALUE)

    def perform_hide(self):
        self.do_click(self.HIDE_OPTION)
        self.do_click(self.HIDE_BUTTON)

    def perform_show(self, value):
        self.do_click(self.SEARCH_BUTTON)
        self.do_click(self.SEARCH_INPUT)
        time.sleep(2)
        self.do_send_keys(self.SEARCH_INPUT, value)
        time.sleep(5)
        self.do_enter(self.SEARCH_INPUT)
        time.sleep(3)
        assert self.TEXTAREA

    def get_button_label(self):
        return self.get_element_text(self.BUTTON_LABEL)

    def performReadUnread(self):
        try:
            if self.is_displayed(self.UNREAD_BUTTON):
                time.sleep(2)
                self.do_click(self.UNREAD_BUTTON)
                print("changed to unread")
        except:
            self.do_click(self.READ_BUTTON)
            print("changed to read")




