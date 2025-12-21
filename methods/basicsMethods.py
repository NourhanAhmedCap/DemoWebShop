from playwright.sync_api import Page, expect


class basicsMethods():
    def __init__(self, page: Page):
        self.page = page

    def ClickonButton(self, Locator):
        self.page.locator(Locator).click()

    def logout_after_test(self):
        self.page.locator(".ico-logout").click()
        