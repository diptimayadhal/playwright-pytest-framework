import pytest
from pages.login_page import LoginPage
from utils.data_loader import load_test_data

data = load_test_data("login_data.json")


@pytest.mark.ui
@pytest.mark.smoke
def test_valid_login(page):

    login = LoginPage(page)

    login.open()

    login.login(
        data["valid_login"]["username"],
        data["valid_login"]["password"]
    )

    assert "dashboard" in page.url.lower()