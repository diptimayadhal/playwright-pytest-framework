from locators.login_locators import LoginLocators
from base.base_page import BasePage
from utils.config_reader import load_config
from utils.logger import get_logger

config = load_config()
logger = get_logger()


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    def open(self):

        logger.info("Opening login page")

        self.page.goto(config["base_url"])

    def login(self, username, password):

        logger.info("Entering username")
        self.fill(LoginLocators.USERNAME, username)

        logger.info("Entering password")
        self.fill(LoginLocators.PASSWORD, password)

        logger.info("Clicking login button")
        self.click(LoginLocators.LOGIN_BUTTON)

        logger.info("Waiting for dashboard page")
        self.wait_for_url("**/dashboard**")

    def get_error_message(self):

        logger.info("Fetching error message")

        return self.page.inner_text(LoginLocators.ERROR_MESSAGE)