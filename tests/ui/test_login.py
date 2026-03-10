from pages.login_page import LoginPage
import pytest

@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login(page):

    login = LoginPage(page)

    login.open()

    login.login("Admin", "admin123")

    page.wait_for_url("**/dashboard**")

    assert "dashboard" in page.url.lower()

def test_invalid_login(page):

    login = LoginPage(page)

    login.open()

    login.login("wrong", "wrong")

    error = login.get_error_message()

    assert "Invalid credentials" in error