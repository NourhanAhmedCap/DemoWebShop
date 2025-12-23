from playwright.sync_api import Playwright, Page, expect


class shoppingCartPage():


#---------------Locators--------------
    Items = '.cart-item-row'
    Cart = '#topcartlink'
    CheckOutBtn = '#checkout'
    Terms = '#termsofservice'
    FirstName = '#BillingNewAddress_FirstName'
    LastName ='#BillingNewAddress_LastName'
    Email = '#BillingNewAddress_Email'
    Company = '#BillingNewAddress_Company'
    Country ='#BillingNewAddress_CountryId'
    State = '#BillingNewAddress_StateProvinceId'
    City = '#BillingNewAddress_City'
    Address1 ='#BillingNewAddress_Address1'
    Address2 ='#BillingNewAddress_Address2'
    Zip = '#BillingNewAddress_ZipPostalCode'
    Phone ='#BillingNewAddress_PhoneNumber'
    Fax = '#BillingNewAddress_FaxNumber'
    ShippingAdd = '#shipping-address-select'
    InStorePickup ='#PickUpInStore'
    GroundMethod= '#shippingoption_0'
    NextDayAir40Method= '#shippingoption_1'
    SecondDayAir40Method= '#shippingoption_2'
    Cash = '#paymentmethod_0'
    Check = '#paymentmethod_1'
    CreditCard = '#paymentmethod_2'
    Purchase = '#paymentmethod_3'
    SubTotal = '.product-price'
    ConfirmBtn = '.button-1.confirm-order-next-step-button'
    ConfirmMessage = 'div.section.order-completed .title strong'


    def __init__(self, page: Page):
        self.page = page

    def checkthePrices(self, text, text2):
        line = self.page.locator(f"tr:has(td.cart-total-left:has-text('{text}'))")
        price = line.locator(f"td.cart-total-right .product-price:has-text('{text2}')")
        expect(price).to_have_text(text2)

    def checkoutprocess(self, test_data):
        from pages.page_setup import init_pages
        pages = init_pages(self.page)
        user = test_data["data"]["valid_user"]

        if self.page.locator("#billing-address-select").is_enabled():
            self.page.get_by_role("button", name="Continue").click()
            
        else:
            
            pages.assertions.ValueisCorrect(pages.shoppingCart.FirstName, user["FirstName"])
            pages.assertions.ValueisCorrect(pages.shoppingCart.LastName, user["LastName"])
            pages.assertions.ValueisCorrect(pages.shoppingCart.Email, user["Email"])
            self.page.locator(pages.shoppingCart.Company).fill(user["Company"])
            self.page.locator(pages.shoppingCart.Country).select_option(user["Country"])
            self.page.locator(pages.shoppingCart.City).fill(user["City"])
            self.page.locator(pages.shoppingCart.Address1).fill(user["Address1"])
            self.page.locator(pages.shoppingCart.Zip).fill(user["Zip"])
            self.page.locator(pages.shoppingCart.Phone).fill(user["Phone"])
            self.page.get_by_role("button", name="Continue").click()