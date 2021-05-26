from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from Pages.BasePage import BasePage
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class AddTeamPage(BasePage):
    """Add new team"""
    ADD_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]")
    TEAM_BUTTON = (By.XPATH, "//span[contains(text(),'Team')]")
    TEAM_NAME = (By.XPATH, "//*[@id='modal-root']/div/dialog/div/div[1]/div/div[1]/span/label/input")
    TEAM_TOPIC = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[1]/div/div[2]/span/input')
    CREATE_BUTTON = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[2]/div/button[2]')
    TEAM_CREATED = (By.XPATH, "//*[contains(text(),'" + data.team_name + "')]")

    """Add members to team"""
    MEMBER_BUTTON = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/header/div/div[3]/button[5]')
    ADD_USERS = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/div/aside/footer/div/button[2]")
    INPUT_FIELD = (By.CSS_SELECTOR, "div.rc-scrollbars-view > div > div > div > div.rcx-box> input")
    ADD_USERS_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/div/aside/footer/button")
    MESSAGE = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child>div:nth-child(2)>div:nth-child(2)")

    def __init__(self, driver):
        super().__init__(driver)

    def add_team(self, team_name, team_topic):
        self.do_click(self.ADD_BUTTON)
        self.do_click(self.TEAM_BUTTON)
        self.do_click(self.TEAM_NAME)
        self.do_send_keys(self.TEAM_NAME, team_name)
        self.do_click(self.TEAM_TOPIC)
        self.do_send_keys(self.TEAM_TOPIC, team_topic)
        self.do_click(self.CREATE_BUTTON)

    def is_team_visible(self):
        return self.is_visible(self.TEAM_CREATED)

    def add_members_to_team(self, new_user):
        self.do_click(self.TEAM_CREATED)
        self.do_click(self.MEMBER_BUTTON)
        self.do_click(self.ADD_USERS)
        self.do_click(self.INPUT_FIELD)
        self.do_send_keys(self.INPUT_FIELD, new_user)
        time.sleep(3)
        self.do_enter(self.INPUT_FIELD)
        self.do_click(self.ADD_USERS_BUTTON)

    def is_message_visible(self):
        return self.is_visible(self.MESSAGE)




