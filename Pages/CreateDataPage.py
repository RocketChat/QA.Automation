from selenium.webdriver.common.by import By
import time
from Pages.BasePage import BasePage
from Config.main import Data
data_env = Data()
data = data_env.get_data()


class CreateDataPage(BasePage):

    MORE_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[6]")
    ADMINISTRATION_BUTTON = (By.XPATH, "//span[contains(text(),'Administration')]")
    USERS_BUTTON = (By.XPATH, "//div[contains(text(), 'Users')]")
    NEW_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/section/div[1]/div/div/button[1]")
    NAME_INPUT = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[1]/span/input")
    USERNAME_INPUT = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[2]/span/label/input")
    EMAIL_INPUT = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[3]/span[1]/label/input")
    STATUS_INPUT = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[4]/span/label/input")
    BIO_INPUT = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[5]/span/label/textarea")
    NICKNAME_INPUT = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[6]/span/label/input")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[7]/span/label/input")
    ROLES_INPUT = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[10]/span/div/div[1]/div/input")
    OPTION_USER = (By.CSS_SELECTOR, "body > div:nth-child(23) > div > div > ol > li:nth-child(5) > div > div")
    SAVE_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/form/fieldset/div[13]/span/div/button[2]")

    USER_CREATED = (By.XPATH, "//*[contains(text(),'" + data.new_user + "')]")
    DM_BUTTON = (By.XPATH, "//button[contains(text(),'Direct Message')]")
    TEXTAREA = (By.XPATH, "//*[@name='msg']")
    CLOSE_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/aside/div[5]/div/div/header/div/button")

    ADD_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/aside/div[1]/div/div/div[2]/button[5]")
    CHANNEL_BUTTON = (By.XPATH, "//span[contains(text(),'Channel')]")
    CHANNEL_NAME_INPUT = (By.XPATH, "//*[@id='create-channel']/div[2]/div[1]/label/div[2]/input")
    INVITE_USER_INPUT = (By.XPATH, "//*[@id='create-channel']/div[2]/div[2]/label/div[2]/div[2]/input")
    CREATE_BUTTON = (By.XPATH, "//*[@id='create-channel']/div[3]/input")
    CHANNEL_CREATED = (By.XPATH, "//*[contains(text(),'" + data.channel_name + "')]")

    MEMBER_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/div/main/header/div/div[3]/button[4]")
    ADD_USERS = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/div/main/div/aside/footer/div/button[2]")
    INPUT_FIELD = (By.XPATH, "//input[@placeholder='Choose users']")
    ADD_USERS_BUTTON = (By.XPATH, "//*[@id='rocket-chat']/div[2]/div/div/main/div/aside/footer/button")
    MESSAGE = (By.CSS_SELECTOR, ".wrapper>ul>li:last-child>div:nth-child(2)>div:nth-child(2)>span:nth-child(3)")

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_user(self, new_user, new_username, new_email, new_status, new_bio, new_nickname, new_password):
        self.do_click(self.MORE_BUTTON)
        self.do_click(self.ADMINISTRATION_BUTTON)
        self.do_click(self.USERS_BUTTON)
        self.do_click(self.NEW_BUTTON)

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

        self.do_click(self.NICKNAME_INPUT)
        self.do_send_keys(self.NICKNAME_INPUT, new_nickname)
        self.do_enter(self.NICKNAME_INPUT)

        self.do_click(self.PASSWORD_INPUT)
        self.do_send_keys(self.PASSWORD_INPUT, new_password)
        self.do_enter(self.PASSWORD_INPUT)

        self.do_click(self.ROLES_INPUT)
        self.do_click(self.OPTION_USER)
        self.do_click(self.PASSWORD_INPUT)
        time.sleep(3)

        self.do_click(self.SAVE_BUTTON)
        self.driver.refresh()

    def is_user_visible(self):
        return self.is_visible(self.USER_CREATED)

    def dm_new_user(self, new_message):
        self.do_click(self.USER_CREATED)
        self.do_click(self.DM_BUTTON)
        self.do_click(self.TEXTAREA)
        self.do_send_keys(self.TEXTAREA, new_message)
        self.do_enter(self.TEXTAREA)
        time.sleep(5)

    def add_new_channel(self, channel_name, new_user):
        """There is currently an issue so we have to first click on the close button"""
        self.do_click(self.CLOSE_BUTTON)
        time.sleep(3)
        self.do_click(self.ADD_BUTTON)
        self.do_click(self.CHANNEL_BUTTON)
        self.do_click(self.CHANNEL_NAME_INPUT)
        self.do_send_keys(self.CHANNEL_NAME_INPUT, channel_name)
        self.do_enter(self.CHANNEL_NAME_INPUT)
        time.sleep(3)
        #self.do_click(self.INVITE_USER_INPUT)
        #self.do_send_keys(self.INVITE_USER_INPUT, new_user)
        #time.sleep(5)
        #self.do_enter(self.INVITE_USER_INPUT)
        #time.sleep(5)

        self.do_click(self.CREATE_BUTTON)

    def is_channel_visible(self):
        return self.is_visible(self.CHANNEL_CREATED)

    def add_users_to_channel(self, new_user):
        self.do_click(self.CHANNEL_CREATED)
        self.do_click(self.MEMBER_BUTTON)
        self.do_click(self.ADD_USERS)
        self.do_click(self.INPUT_FIELD)
        self.do_send_keys(self.INPUT_FIELD, new_user)
        self.do_enter(self.INPUT_FIELD)
        self.do_click(self.ADD_USERS_BUTTON)

    def is_message_visible(self):
        return self.is_visible(self.MESSAGE)



















