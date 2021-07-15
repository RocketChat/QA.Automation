from selenium.webdriver.common.by import By
import time
from Pages.BasePage import BasePage
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class TeamsPage(BasePage):
    """Add new team"""
    ADD_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(5)")
    TEAM_BUTTON = (By.CSS_SELECTOR, ".rc-popover__list>li:nth-child(2)")
    TEAM_NAME = (By.XPATH, "//*[@id='modal-root']/div/dialog/div/div[1]/div/div[1]/span/label/input")
    TEAM_TOPIC = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[1]/div/div[2]/span/input')
    CREATE_BUTTON = (By.XPATH, "//button[contains(text(), 'Create')]")
    TEAM_CREATED = (By.XPATH, "//*[contains(text(),'" + data.team_name + "')]")

    """Add members to team"""
    MEMBERS = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/header/div/div[3]/button[@title='Teams Members']")
    ADD_USERS = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/div/aside/footer/div/button[2]")
    INPUT_FIELD = (By.CSS_SELECTOR, "div.rc-scrollbars-view > div > div > div > div.rcx-box> input")
    ADD_USERS_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/div/aside/footer/button")
    MESSAGE = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child>div:nth-child(2)>div:nth-child(2)")

    """Add existing channel to team"""
    CHANNELS = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/header/div/div[3]/button[@title="Team Channels"]')
    ADD_EXISTING = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/div/aside/footer/div/button[1]')
    CHANNEL_INPUT = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[1]/div/div/div/div[1]/input')
    ADD_CHANNEL = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[2]/div/button[2]')
    CHANNEL_ADDED = (By.XPATH, "//*[contains(text(),'" + data.channel_name + "')]")
    HOME_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(1)")

    """Add New channel to team"""
    CREATE_NEW = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/div/aside/footer/div/button[2]')
    NAME_INPUT = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[1]/div/div[1]/span/label/input')
    NEW_CHANNEL = (By.XPATH, "//*[contains(text(),'" + data.new_channel + "')]")
    CREATE_CHANNEL = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[2]/div/button[2]')

    """Remove channel from team"""
    CHANNEL = (By.XPATH, "//li[@class='rcx-option']//div[contains(text(), '" + data.channel_name + "')]/parent::div/parent::div/parent::li/parent::div")
    OPTIONS_BUTTON = (By.XPATH, "//li[@class='rcx-option']//div[contains(text(), '" + data.channel_name + "')]/parent::div/parent::div/parent::li/parent::div//button[@class='rcx-box rcx-box--full rcx-box--animated rcx-button--tiny-square rcx-button--square rcx-button--ghost rcx-button rcx-css-ue04py']")
    REMOVE_FROM_TEAM = (By.XPATH, "//*[contains(text(), 'Remove from team')]")
    REMOVE_BUTTON = (By.XPATH, "//*[@id='modal-root']/div/dialog/div/div[2]/div/button[2]")

    """Convert channel to team"""
    CHANNEL_BUTTON = (By.CSS_SELECTOR, ".rc-popover__list>li:nth-child(1)")
    CHANNEL_NAME_INPUT = (By.XPATH, "//*[@id='modal-root']/div/dialog/div/div[1]/div/div[1]/span/label/input")
    CHANNEL_CREATED = (By.XPATH, "//*[contains(text(),'" + data.channel2team + "')]")
    INFO_BUTTON = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/header/div/div[3]/button[1]')
    MORE_BUTTON = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/div/aside/div/div/div[1]/div/div/div[2]/div/button[3]')
    CONVERT_TO_TEAM = (By.XPATH, '//li[@class="rcx-option"][@value="convert"]')
    CONVERT_BUTTON = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[2]/div/div/button[2]')

    """Edit Team"""
    EDIT_BUTTON = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/div/aside/div/div/div[1]/div/div/div[2]/div/button[1]')
    NAME = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/div/aside/div/div/div[1]/form/div[2]/span/input')
    SAVE_BUTTON = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/div/aside/div/div/div[1]/form/div[10]/span/div/div/button[2]')
    TEAM_EDIT = (By.XPATH, "//*[contains(text(),'" + data.new_name + "')]")

    """Move to Team"""
    CHANNEL_CREATED2 = (By.XPATH, "//*[contains(text(),'" + data.channel + "')]")
    MOVE_TO_TEAM = (By.XPATH, '//li[@class="rcx-option"][@value="move"]')
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(text(), 'Continue')]")
    YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Yes')]")
    SEARCH_CHANNEL = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[1]/div/div[5]/div/div[1]/input')
    MOVED_CHANNEL = (By.XPATH, '//li[@class="rcx-option"]//div[contains(text(),"' + data.channel + '")]')

    def __init__(self, driver):
        super().__init__(driver)

    def add_team(self, team_name, team_topic):
        self.do_click(self.ADD_BUTTON)
        self.do_click(self.TEAM_BUTTON)
        self.save_screenshot("/Screenshots/TeamModal.png")
        self.do_click(self.TEAM_NAME)
        self.do_send_keys(self.TEAM_NAME, team_name)
        self.do_click(self.TEAM_TOPIC)
        self.do_send_keys(self.TEAM_TOPIC, team_topic)
        self.do_click(self.CREATE_BUTTON)

    def is_team_visible(self):
        return self.is_visible(self.TEAM_CREATED)

    def add_members_to_team(self, new_user):
        self.do_click(self.TEAM_CREATED)
        time.sleep(5)
        self.do_click(self.MEMBERS)
        self.do_click(self.ADD_USERS)
        self.save_screenshot("/Screenshots/UsersToTeam.png")
        self.do_click(self.INPUT_FIELD)
        self.do_send_keys(self.INPUT_FIELD, new_user)
        time.sleep(3)
        self.do_enter(self.INPUT_FIELD)
        self.do_click(self.ADD_USERS_BUTTON)

    def is_message_visible(self):
        return self.is_visible(self.MESSAGE)

    def add_existing_channel_to_team(self, channel_name):
        self.do_click(self.TEAM_CREATED)
        time.sleep(5)
        self.do_click(self.CHANNELS)
        self.save_screenshot("/Screenshots/AddChannelsToTeam.png")
        self.do_click(self.ADD_EXISTING)
        self.do_click(self.CHANNEL_INPUT)
        self.do_send_keys(self.CHANNEL_INPUT, channel_name)
        time.sleep(3)
        self.do_enter(self.CHANNEL_INPUT)
        self.do_click(self.ADD_CHANNEL)

    def is_channel_visible(self):
        return self.is_visible(self.CHANNEL_ADDED)

    def go_to_Home(self):
        self.do_click(self.HOME_BUTTON)

    def add_new_channel_to_team(self, new_channel):
        self.do_click(self.TEAM_CREATED)
        time.sleep(5)
        self.do_click(self.CHANNELS)
        self.do_click(self.CREATE_NEW)
        self.save_screenshot("/Screenshots/NewChannelToTeam.png")
        self.do_click(self.NAME_INPUT)
        self.do_send_keys(self.NAME_INPUT, new_channel)
        time.sleep(3)
        self.do_click(self.CREATE_CHANNEL)

    def is_new_channel_visible(self):
        return self.is_visible(self.NEW_CHANNEL)

    def remove_channel_from_team(self):
        self.do_click(self.TEAM_CREATED)
        time.sleep(5)
        self.do_click(self.CHANNELS)
        self.mouse_over(self.CHANNEL)
        time.sleep(2)
        self.do_click(self.OPTIONS_BUTTON)
        self.save_screenshot("/Screenshots/RemoveChannel.png")
        self.do_click(self.REMOVE_FROM_TEAM)
        self.do_click(self.REMOVE_BUTTON)

    def convert_channel_to_team(self, channel2team):
        self.do_click(self.ADD_BUTTON)
        time.sleep(5)
        self.do_click(self.CHANNEL_BUTTON)
        self.do_click(self.CHANNEL_NAME_INPUT)
        self.do_send_keys(self.CHANNEL_NAME_INPUT, channel2team)
        time.sleep(3)
        self.do_click(self.CREATE_BUTTON)
        time.sleep(2)
        self.do_click(self.CHANNEL_CREATED)
        time.sleep(5)
        self.do_click(self.INFO_BUTTON)
        self.do_click(self.MORE_BUTTON)
        time.sleep(10)
        self.save_screenshot("/Screenshots/ConvertToTeam.png")
        self.do_click(self.CONVERT_TO_TEAM)
        time.sleep(2)
        self.do_click(self.CONVERT_BUTTON)

    def edit_team(self, new_name):
        self.do_click(self.TEAM_CREATED)
        time.sleep(5)
        self.do_click(self.INFO_BUTTON)
        self.do_click(self.EDIT_BUTTON)
        self.save_screenshot("/Screenshots/EditTeamModal.png")
        self.do_click(self.NAME)
        self.do_send_keys(self.NAME, new_name)
        self.do_click(self.SAVE_BUTTON)

    def is_change_visible(self):
        return self.is_visible(self.TEAM_EDIT)

    def move_channel_to_team(self, channel, team_name):
        self.do_click(self.ADD_BUTTON)
        time.sleep(5)
        self.do_click(self.CHANNEL_BUTTON)
        self.do_click(self.CHANNEL_NAME_INPUT)
        self.do_send_keys(self.CHANNEL_NAME_INPUT, channel)
        time.sleep(3)
        self.do_click(self.CREATE_BUTTON)
        time.sleep(2)
        self.do_click(self.CHANNEL_CREATED2)
        time.sleep(5)
        self.do_click(self.INFO_BUTTON)
        self.do_click(self.MORE_BUTTON)
        time.sleep(10)
        self.save_screenshot("/Screenshots/MovetToTeam.png")
        self.do_click(self.MOVE_TO_TEAM)
        time.sleep(2)
        self.do_click(self.SEARCH_CHANNEL)
        self.do_send_keys(self.SEARCH_CHANNEL, team_name)
        time.sleep(2)
        self.do_enter(self.SEARCH_CHANNEL)
        time.sleep(2)
        self.do_click(self.CONTINUE_BUTTON)
        time.sleep(2)
        self.do_click(self.YES_BUTTON)
        time.sleep(5)
        self.save_screenshot("/Screenshots/ChannelMovedToTeam.png")
        self.do_click(self.TEAM_CREATED)
        time.sleep(5)
        self.do_click(self.CHANNELS)

    def is_channel_moved(self):
        return self.is_visible(self.MOVED_CHANNEL)





















