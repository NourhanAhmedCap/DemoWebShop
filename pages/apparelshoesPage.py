from playwright.sync_api import Page, expect


class apparelshoesPage():
    #---------------Locators--------------
    BlueJeans = '[data-productid="36"]'
    Rockabilly = '[data-productid="5"]'
    GolfBelt = '[data-productid="40"]'
    LeatherHandbag = '[data-productid="29"]'
    



    def __init__(self, page: Page):
        self.page = page

    def AddItemsTocart(self, Locator ):
        Product = self.page.locator(Locator)
        Product.get_by_role("button", name="Add to cart").click()
