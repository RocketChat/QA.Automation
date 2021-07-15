from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from selenium.webdriver import ActionChains
import time
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class ViewModePage(BasePage):

    VIEW_MODE_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(4)")
    EXTENDED_MODE = (By.CSS_SELECTOR, "body > div.rc-popover.rc-popover-- > div > div > div > ul:nth-child(2) > li:nth-child(1) > label > label")
    HOME = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(1)")
    MEDIUM_MODE = (By.CSS_SELECTOR, "body > div.rc-popover.rc-popover-- > div > div > div > ul:nth-child(2) > li:nth-child(2) > label > label")
    CONDENSED_MODE = (By.CSS_SELECTOR, "body > div.rc-popover.rc-popover-- > div > div > div > ul:nth-child(2) > li:nth-child(3) > label > label")

    def __init__(self, driver):
        super().__init__(driver)

    def select_Extended_Mode(self):
        self.do_click(self.VIEW_MODE_BUTTON)
        time.sleep(3)
        self.do_click(self.EXTENDED_MODE)
        time.sleep(3)
        self.save_screenshot("/Screenshots/ExtendedMode.png")

    def select_Medium_Mode(self):
        self.do_click(self.VIEW_MODE_BUTTON)
        time.sleep(3)
        self.do_click(self.MEDIUM_MODE)
        time.sleep(3)
        self.save_screenshot("/Screenshots/MediumMode.png")

    def select_Condensed_Mode(self):
        self.do_click(self.VIEW_MODE_BUTTON)
        time.sleep(3)
        self.do_click(self.CONDENSED_MODE)
        time.sleep(3)
        self.save_screenshot("/Screenshots/CondensedMode.png")

    def double_click_home(self):
        self.do_double_click(self.HOME)

