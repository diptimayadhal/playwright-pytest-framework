from locators.logout_locators import LogoutLocators
from utils.logger import get_logger

logger = get_logger()


class LogoutPage:

    def __init__(self, page):
        self.page = page

def logout(self):

    logger.info("Clicking user dropdown")

    self.page.click(LogoutLocators.USER_DROPDOWN)

    logger.info("Waiting for logout button")

    self.page.wait_for_selector(LogoutLocators.LOGOUT_BUTTON)

    logger.info("Clicking logout button")

    self.page.click(LogoutLocators.LOGOUT_BUTTON)

    logger.info("Waiting for login page")

    self.page.wait_for_url("**/auth/login**")