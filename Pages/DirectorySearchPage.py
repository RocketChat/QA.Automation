from selenium.webdriver.common.by import By
import time

from Pages.BasePage import BasePage
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class DirectorySearchPage(BasePage):
    DIRECTORY_SEARCH = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(3)")
    SEARCH_INPUT = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/section/div[3]/form/label/input')
    CHANNEL_SECTION = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/section/div[2]/div/div/button[1]')
    USERS_SECTION = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/section/div[2]/div/div/button[2]')
    TEAMS_SECTION = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/section/div[2]/div/div/button[3]')
    RESULT = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/section/div[3]/div/div/div[1]/div/table/tbody/tr/td[1]/div')
    CHANNEL = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/header/div/div[2]/div[1]/div[2][contains(text(),'" + data.channel_name + "')]")
    USER = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/header/div/div[2]/div[1]/div[2][contains(text(),'" + data.user + "')]")
    TEAM = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/header/div/div[2]/div[1]/div[2][contains(text(),'" + data.team_name + "')]")
    TextArea = (By.XPATH, "//*[@name='msg']")

    def __init__(self, driver):
        super().__init__(driver)

    def search_channel(self, channelName):
        self.do_click(self.DIRECTORY_SEARCH)
        self.do_click(self.SEARCH_INPUT)
        self.do_send_keys(self.SEARCH_INPUT, channelName)
        time.sleep(3)
        self.save_screenshot("/Screenshots/DirectorySearchChannel.png")
        self.do_click(self.RESULT)
        time.sleep(3)

    def is_channel_name_visible(self):
        return self.is_visible(self.CHANNEL)

    def search_user(self, user):
        self.do_click(self.DIRECTORY_SEARCH)
        self.do_click(self.USERS_SECTION)
        self.do_click(self.SEARCH_INPUT)
        self.do_send_keys(self.SEARCH_INPUT, user)
        time.sleep(3)
        self.save_screenshot("/Screenshots/DirectorySearchUser.png")
        self.do_click(self.RESULT)
        time.sleep(3)

    def is_user_visible(self):
        return self.is_visible(self.USER)

    def search_team(self, team):
        self.do_click(self.DIRECTORY_SEARCH)
        self.do_click(self.TEAMS_SECTION)
        self.do_click(self.SEARCH_INPUT)
        self.do_send_keys(self.SEARCH_INPUT, team)
        time.sleep(3)
        self.save_screenshot("/Screenshots/DirectorySearchTeam.png")
        self.do_click(self.RESULT)
        time.sleep(3)

    def is_team_name_visible(self):
        return self.is_visible(self.TEAM)


