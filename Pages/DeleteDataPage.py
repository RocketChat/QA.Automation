from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from Pages.BasePage import BasePage
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class DeleteDataPage(BasePage):
    AVATAR = (By.XPATH, "//*[@id='rocket-chat']/aside/div[1]/div/div/div[1]")
    ADMINISTRATION_BUTTON = (By.CSS_SELECTOR,
                             "body > div.rc-popover.rc-popover-- > div > div > div > div:nth-child(5) > li > div > div.rcx-option__content")
    USERS_BUTTON = (By.CSS_SELECTOR,
                    "#rocket-chat > aside > div.flex-nav > div > div > div > div > div.rc-scrollbars-view > div > div > a:nth-child(3)")
    USER_CREATED = (By.XPATH, "//*[contains(text(),'" + data.new_user + "')]")
    USER = (By.XPATH, "//a[@aria-label='" + data.new_username + "']/parent::div")
    MORE_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div/div/div[2]/div/button[3]")
    DELETE_BUTTON = (By.XPATH, "//*[contains(text(),'Delete')]")
    CONFIRM_DELETE = (By.XPATH, "//*[@id='modal-root']/div/dialog/div/div[2]/div/div/button[2]")
    OK_BUTTON = (By.XPATH, "//*[contains(text(),'Ok')]")
    CLOSE_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/aside/div[5]/div/div/header/div/button")
    HOME_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(1)")

    CHANNEL = (By.XPATH, "//*[contains(text(),'" + data.channel_name + "')]")
    INFO_BUTTON = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/header/div/div[3]/button[1]')
    DELETE = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/div/aside/div/div/div[1]/div/div/div[2]/div/button[2]")
    DELETE_CONFIRM_CHANNEL = (By.XPATH, "//button[contains(text(), 'Yes, delete it!')]")

    TEAM_CREATED = (By.XPATH, "//*[contains(text(),'" + data.team_name + "')]")
    CONTINUE = (By.XPATH, "//button[contains(text(), 'Continue')]")
    REMOVE_BUTTON = (By.XPATH, '//*[contains(text(), "Remove")]')

    def __init__(self, driver):
        super().__init__(driver)

    def Delete_user(self):
        self.do_click(self.AVATAR)
        self.do_click(self.ADMINISTRATION_BUTTON)
        time.sleep(3)
        self.do_click(self.USERS_BUTTON)
        self.do_click(self.USER_CREATED)
        self.do_click(self.MORE_BUTTON)
        self.save_screenshot("/Screenshots/DeleteUser.png")
        self.do_click(self.DELETE_BUTTON)
        self.do_click(self.CONFIRM_DELETE)
        self.do_click(self.OK_BUTTON)
        self.do_click(self.CLOSE_BUTTON)

    def Delete_channel(self):
        self.do_click(self.CHANNEL)
        self.do_click(self.INFO_BUTTON)
        self.save_screenshot("/Screenshots/DeleteChannel.png")
        self.do_click(self.DELETE)
        self.do_click(self.DELETE_CONFIRM_CHANNEL)
        self.do_click(self.HOME_BUTTON)

    def user_not_displayed(self):
        try:
            if self.is_displayed(self.USER):
                print("User is still displayed when it should not!")
            exit()

        except (NoSuchElementException, TimeoutException):
            print("User deleted successfully")

    def channel_not_displayed(self):
        try:
            if self.is_displayed(self.CHANNEL):
                raise Exception("Channel is still displayed when it should not!")

        except (NoSuchElementException, TimeoutException):
            print("Channel deleted successfully")

    def Delete_team(self):
        self.do_click(self.TEAM_CREATED)
        time.sleep(5)
        self.do_click(self.INFO_BUTTON)
        self.save_screenshot("/Screenshots/DeleteTeam.png")
        self.do_click(self.DELETE)
        self.do_click(self.CONTINUE)
        self.do_click(self.REMOVE_BUTTON)
        self.do_click(self.HOME_BUTTON)

    def team_not_displayed(self):
        try:
            if self.is_displayed(self.TEAM_CREATED):
                raise Exception("Team is still displayed when it should not!")

        except (NoSuchElementException, TimeoutException):
            print("Team deleted successfully")




