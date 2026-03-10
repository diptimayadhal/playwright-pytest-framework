class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.click(locator)

    def fill(self, locator, value):
        self.page.fill(locator, value)

    def wait_for_element(self, locator):
        self.page.wait_for_selector(locator)

    def get_text(self, locator):
        return self.page.inner_text(locator)