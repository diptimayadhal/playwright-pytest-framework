from pages.logout_pages import LogoutPage
from pages.dashboard_pages import DashboardPage
from pages.login_page import LoginPage


def test_logout(logged_in_page):

    page = logged_in_page

    logout = LogoutPage(page)
    dashboard = DashboardPage(page)
    login = LoginPage(page)

    logout.logout()

    # verify dashboard is NOT visible
    assert not dashboard.is_dashboard_visible()