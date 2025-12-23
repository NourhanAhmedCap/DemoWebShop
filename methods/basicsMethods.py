from playwright.sync_api import Page

class basicsMethods():
    def __init__(self, page: Page):
        self.page = page

    def ClickonButton(self, Locator):
        self.page.locator(Locator).click()

    def logout_after_test(self):
        self.page.locator(".ico-logout").click()
    
    def ClickonElementwithFilter(self, Locator,text ):
        self.page.locator(Locator).filter(has_text=text).click()