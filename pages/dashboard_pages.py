from locators.dashboard_locators import DashboardLocators
from utils.logger import get_logger

logger = get_logger()


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def wait_for_dashboard(self):

        logger.info("Waiting for dashboard to load")

        self.page.wait_for_selector(DashboardLocators.DASHBOARD)

    def is_dashboard_visible(self):

        logger.info("Checking if dashboard is visible")

        return self.page.is_visible(DashboardLocators.DASHBOARD)