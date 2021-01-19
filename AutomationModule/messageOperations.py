import time
from selenium.common.exceptions import NoSuchElementException

class MessageOperations:

    def __init__(self, browser):
        self.browser = browser

    def performReadUnread(self):
        try:
            unread = self.browser.find_element_by_xpath("//*[contains(text(),'Mark Unread')]")
            if unread.is_displayed():
                time.sleep(3)
                unread.click()
                print("changed to unread")
        except NoSuchElementException:
            try:
                read = self.browser.find_element_by_xpath("//*[contains(text(),'Mark Read')]")
                if read.is_displayed():
                    time.sleep(3)
                    read.click()
                    print("changed to read")
            except NoSuchElementException:
                time.sleep(1)
