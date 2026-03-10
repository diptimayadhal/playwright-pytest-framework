from pages.dashboard_pages import DashboardPage
import time


def test_dashboard_loaded(logged_in_page):

    dashboard = DashboardPage(logged_in_page)
    time.sleep(5)
    assert dashboard.is_dashboard_visible()