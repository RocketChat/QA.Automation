from selenium.webdriver.common.by import By
import time
from Pages.BasePage import BasePage
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class CreateDataPage(BasePage):
    AVATAR = (By.XPATH, "//*[@id='rocket-chat']/aside/div[1]/div/div/div[1]")
    ADMINISTRATION_BUTTON = (By.CSS_SELECTOR, "body > div.rc-popover.rc-popover-- > div > div > div > div:nth-child(5) > li > div > div.rcx-option__content")
    USERS_BUTTON = (By.CSS_SELECTOR, "#rocket-chat > aside > div.flex-nav > div > div > div > div > div.rc-scrollbars-view > div > div > a:nth-child(3)")
    NEW_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/section/div[1]/div/div/button[1]")
    NAME_INPUT = (By.CSS_SELECTOR, "div.rc-scrollbars-view > form > fieldset > div:nth-child(1) > span > input")
    USERNAME_INPUT = (By.CSS_SELECTOR, "div.rc-scrollbars-view > form > fieldset > div:nth-child(2) > span > label > input")
    EMAIL_INPUT = (By.CSS_SELECTOR, "div.rc-scrollbars-view > form > fieldset > div:nth-child(3) > span:nth-child(2) > label > input")
    STATUS_INPUT = (By.CSS_SELECTOR, "div.rc-scrollbars-view > form > fieldset > div:nth-child(4) > span > label > input")
    BIO_INPUT = (By.CSS_SELECTOR, "div.rc-scrollbars-view > form > fieldset > div:nth-child(5) > span > label > textarea")
    NICKNAME_INPUT = (By.CSS_SELECTOR, "div.rc-scrollbars-view > form > fieldset > div:nth-child(6) > span > label > input")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "div.rc-scrollbars-view > form > fieldset > div:nth-child(7) > span > label > input")
    ROLES_INPUT = (By.CSS_SELECTOR, "div.rc-scrollbars-view > form > fieldset > div:nth-child(10) > span >div>div>div>input")
    OPTION_USER = (By.CSS_SELECTOR, "body > div:nth-child(22) > div > div > ol > li:nth-child(5) > div >label>input")
    SAVE_BUTTON = (By.CSS_SELECTOR, "div.rc-scrollbars-view > form > fieldset > div:nth-child(13) > span > div > button.rcx-box.rcx-box--full.rcx-box--animated.rcx-button.rcx-css-t3n91h")

    USER = (By.XPATH, "//a[@aria-label='" + data.new_username + "']/parent::div")
    USER_CREATED = (By.XPATH, "//*[contains(text(),'" + data.new_user + "')]")
    DM_BUTTON = (By.XPATH, "//button[contains(text(),'Direct Message')]")
    TEXTAREA = (By.XPATH, "//*[@name='msg']")
    CLOSE_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/aside/div[5]/div/div/header/div/button")

    ADD_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(5)")
    CHANNEL_BUTTON = (By.CSS_SELECTOR, ".rc-popover__list>li:nth-child(1)")
    CHANNEL_NAME_INPUT = (By.XPATH, "//*[@id='modal-root']/div/dialog/div/div[1]/div/div[1]/span/label/input")
    INVITE_USER_INPUT = (By.XPATH, "//*[@id='modal-root']/div/dialog/div/div[1]/div/div[7]/div/div[1]/input")
    CREATE_BUTTON = (By.XPATH, "//*[@id='modal-root']/div/dialog/div/div[2]/div/button[2]")
    CHANNEL_CREATED = (By.XPATH, "//*[contains(text(),'" + data.channel_name + "')]")

    MEMBER_BUTTON = (By.XPATH, '//*[@id="rocket-chat"]/div[2]/div/main/header/div/div[3]/button[@title="Members"]')
    ADD_USERS = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/div/aside/footer/div/button[2]")
    INPUT_FIELD = (By.CSS_SELECTOR, "div.rc-scrollbars-view > div > div > div > div.rcx-box> input")
    ADD_USERS_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/main/div/aside/footer/button")
    MESSAGE = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child>div:nth-child(2)>div:nth-child(2)")

    DISCUSSION_BUTTON = (By.CSS_SELECTOR, ".rc-popover__list>li:nth-child(4)")
    CHANNEL_INPUT = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[1]/div/fieldset/div[2]/span/div/div[1]/input')
    #DISCUSSION_INPUT = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[1]/div/fieldset/div[4]/span/label/input')
    DISCUSSION_INPUT = (By.XPATH, '//input[@type="text"]')
    CHANNEL_USERS_INPUT = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[1]/div/fieldset/div[5]/span/div/div[1]/input')
    DISCUSSION_MESSAGE = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[1]/div/fieldset/div[6]/span/textarea')
    CREATE__DISCUSSION_BUTTON = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[2]/div/button')
    CREATED_DISCUSSION = (By.XPATH, "//*[contains(text(),'" + data.discussion_name + "')]")

    DMBUTTON = (By.CSS_SELECTOR, ".rc-popover__list>li:nth-child(3)")
    DM_USERS_INPUT = (By.XPATH, '//*[@id="modal-root"]/div/dialog/div/div[1]/div/div[2]/div/div[1]/input')
    CREATE_DM_BUTTON = (By.XPATH, "//button[contains(text(), 'Create')]")
    HOME_BUTTON = (By.CSS_SELECTOR, ".rcx-box>button:nth-child(1)")

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_user(self, new_user, new_username, new_email, new_status, new_bio, new_nickname, new_password):
        self.do_click(self.AVATAR)
        self.do_click(self.ADMINISTRATION_BUTTON)
        self.do_click(self.USERS_BUTTON)
        self.do_click(self.NEW_BUTTON)
        self.save_screenshot("/Screenshots/NewUser.png")

        self.do_click(self.NAME_INPUT)
        self.do_send_keys(self.NAME_INPUT, new_user)
        self.do_enter(self.NAME_INPUT)

        self.do_click(self.USERNAME_INPUT)
        self.do_send_keys(self.USERNAME_INPUT, new_username)
        self.do_enter(self.USERNAME_INPUT)

        self.do_click(self.EMAIL_INPUT)
        self.do_send_keys(self.EMAIL_INPUT, new_email)
        self.do_enter(self.EMAIL_INPUT)

        self.do_click(self.STATUS_INPUT)
        self.do_send_keys(self.STATUS_INPUT, new_status)
        self.do_enter(self.STATUS_INPUT)

        self.do_click(self.BIO_INPUT)
        self.do_send_keys(self.BIO_INPUT, new_bio)
        self.do_enter(self.BIO_INPUT)
        time.sleep(5)

        self.do_click(self.NICKNAME_INPUT)
        self.do_send_keys(self.NICKNAME_INPUT, new_nickname)
        self.do_enter(self.NICKNAME_INPUT)

        self.do_click(self.PASSWORD_INPUT)
        self.do_send_keys(self.PASSWORD_INPUT, new_password)
        self.do_enter(self.PASSWORD_INPUT)

        #self.do_click(self.ROLES_INPUT)
        #self.do_click(self.OPTION_USER)
        #self.do_click(self.PASSWORD_INPUT)

        time.sleep(3)
        self.do_click(self.SAVE_BUTTON)
        #self.driver.refresh()

    def is_user_visible(self):
        return self.is_visible(self.USER_CREATED)

    def is_user_displayed(self):
        return self.is_displayed(self.USER)

    def dm_new_user(self, new_message):
        #self.do_click(self.USER_CREATED)
        self.do_click(self.DM_BUTTON)
        self.do_click(self.TEXTAREA)
        self.do_send_keys(self.TEXTAREA, new_message)
        self.do_enter(self.TEXTAREA)
        time.sleep(5)

    def add_new_channel(self, channel_name, new_user):
        """There is currently an issue so we have to first click on the close button"""
        #self.do_click(self.CLOSE_BUTTON)
        #time.sleep(3)
        self.do_click(self.ADD_BUTTON)
        self.do_click(self.CHANNEL_BUTTON)
        self.save_screenshot("/Screenshots/ChannelModal.png")
        self.do_click(self.CHANNEL_NAME_INPUT)
        self.do_send_keys(self.CHANNEL_NAME_INPUT, channel_name)
        self.do_enter(self.CHANNEL_NAME_INPUT)
        time.sleep(3)
        # self.do_click(self.INVITE_USER_INPUT)
        # self.do_send_keys(self.INVITE_USER_INPUT, new_user)
        # time.sleep(5)
        # self.do_enter(self.INVITE_USER_INPUT)
        # time.sleep(5)

        self.do_click(self.CREATE_BUTTON)

    def is_channel_visible(self):
        return self.is_visible(self.CHANNEL_CREATED)

    def add_users_to_channel(self, new_user):
        #self.do_click(self.CHANNEL_CREATED)
        time.sleep(4)
        self.do_click(self.MEMBER_BUTTON)
        self.do_click(self.ADD_USERS)
        self.save_screenshot("/Screenshots/UserModal.png")
        self.do_click(self.INPUT_FIELD)
        self.do_send_keys(self.INPUT_FIELD, new_user)
        self.do_enter(self.INPUT_FIELD)
        self.do_click(self.ADD_USERS_BUTTON)

    def is_message_visible(self):
        return self.is_visible(self.MESSAGE)

    def add_discussion(self, channel_name, discussion_name, new_user, discussion_message):
        time.sleep(5)
        self.do_click(self.ADD_BUTTON)
        self.do_click(self.DISCUSSION_BUTTON)
        self.save_screenshot("/Screenshots/DiscussionModal.png")
        self.do_click(self.CHANNEL_INPUT)
        self.do_send_keys(self.CHANNEL_INPUT, channel_name)
        time.sleep(3)
        self.do_enter(self.CHANNEL_INPUT)
        time.sleep(3)

        self.do_click(self.DISCUSSION_INPUT)
        self.do_send_keys(self.DISCUSSION_INPUT, discussion_name)

        self.do_click(self.CHANNEL_USERS_INPUT)
        self.do_send_keys(self.CHANNEL_USERS_INPUT, new_user)
        time.sleep(3)
        self.do_enter(self.CHANNEL_USERS_INPUT)

        self.do_click(self.DISCUSSION_MESSAGE)
        self.do_send_keys(self.DISCUSSION_MESSAGE, discussion_message)
        time.sleep(2)

        self.do_click(self.CREATE__DISCUSSION_BUTTON)
        time.sleep(3)

    def is_discussion_visible(self):
        return self.is_visible(self.CREATED_DISCUSSION)

    def add_DM(self, new_user):
        self.do_click(self.ADD_BUTTON)
        self.do_click(self.DMBUTTON)
        self.save_screenshot("/Screenshots/DMModal.png")
        self.do_click(self.DM_USERS_INPUT)
        self.do_send_keys(self.DM_USERS_INPUT, new_user)
        time.sleep(3)
        self.do_enter(self.DM_USERS_INPUT)
        time.sleep(3)
        self.do_click(self.CREATE_DM_BUTTON)

    def is_DM_visible(self):
        return self.is_visible(self.TEXTAREA)

    def go_to_Home(self):
        self.do_click(self.HOME_BUTTON)





















