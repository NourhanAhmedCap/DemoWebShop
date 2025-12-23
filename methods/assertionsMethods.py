from playwright.sync_api import Page, expect

class assertionsMethods():
    def __init__(self, page: Page):
        self.page = page

    def AssertElementVsisble(self, Locator):
        expect(self.page.locator(Locator)).to_be_visible()

    def AssertErrorMessagAppears(self, Locator, text):
        expect(self.page.locator(Locator)).to_have_text(text)

    def AssetHaveCount(self, Locator:str, count):
         expect(self.page.locator(Locator)).to_have_count(count)
    def ValueisCorrect(self, Locator, value):
        expect(self.page.locator(Locator)).to_have_value(value)