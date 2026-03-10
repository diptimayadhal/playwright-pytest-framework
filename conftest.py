import pytest
import requests
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.logout_pages import LogoutPage
from utils.config_reader import load_config
from datetime import datetime
import os

config = load_config()


@pytest.fixture(scope="session")
def browser():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=config["headless"]
        )

        yield browser

        browser.close()


@pytest.fixture(scope="function")
def page(browser):

    context = browser.new_context()

    page = context.new_page()

    yield page

    context.close()


@pytest.fixture
def logged_in_page(page):

    login = LoginPage(page)

    login.open()

    login.login("Admin", "admin123")

    yield page

    logout = LogoutPage(page)

    logout.logout()


@pytest.fixture(scope="session")
def auth_cookies(browser):

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://opensource-demo.orangehrmlive.com")

    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")

    page.click("button[type='submit']")

    page.wait_for_url("**dashboard**")

    cookies = context.cookies()

    context.close()

    return cookies


@pytest.fixture
def orange_api(auth_cookies):

    session = requests.Session()

    for cookie in auth_cookies:
        session.cookies.set(cookie["name"], cookie["value"])

    return session

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        page = item.funcargs.get("page")

        if page:

            os.makedirs("reports/screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name

            screenshot_path = f"reports/screenshots/{test_name}_{timestamp}.png"

            try:
                page.screenshot(path=screenshot_path)
            except Exception as e:
                print(f"Screenshot capture failed: {e}")