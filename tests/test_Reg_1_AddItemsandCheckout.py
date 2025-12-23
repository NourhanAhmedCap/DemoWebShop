from playwright.sync_api import Playwright, Page, expect
from pages.page_setup import init_pages
import pytest
import time

@pytest.mark.regression
def test_1_Reg_AddItemsandCheckout(BrowserInstance, page:Page, config, test_data ):
    page = BrowserInstance
    user = test_data["data"]["valid_user"]
    pages = init_pages(page)
    pages.login.open(config["base_url"])
    page.locator(pages.login.LOGIN_BUTTON).click()
    page.locator(pages.login.Email).fill(user["Email"])
    page.locator(pages.login.Password).fill(user["Password"])
    page.locator(pages.login.RememberMe).click()
    page.locator(pages.login.LoginToAccount).click()
    page.get_by_role("link", name="Apparel & Shoes").nth(1).click()
    pages.apparelshoes.AddItemsTocart(pages.apparelshoes.BlueJeans)
    page.wait_for_timeout(2000)
    pages.apparelshoes.AddItemsTocart(pages.apparelshoes.GolfBelt)
    page.locator(pages.shoppingCart.Cart).click()
    pages.assertions.AssetHaveCount(pages.shoppingCart.Items, 2)
    page.locator(pages.shoppingCart.Terms).click()
    page.locator(pages.shoppingCart.CheckOutBtn).click()
    pages.shoppingCart.checkoutprocess(test_data)
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Continue").click()
    page.locator(pages.shoppingCart.GroundMethod).click()
    page.get_by_role("button", name="Continue").click()
    page.locator(pages.shoppingCart.Cash).click()
    page.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Continue").click()
    pages.assertions.AssetHaveCount(pages.shoppingCart.Items, 2)
    pages.shoppingCart.checkthePrices('Sub-Total:', '2.00')
    pages.shoppingCart.checkthePrices('Shipping:', '10.00')
    pages.shoppingCart.checkthePrices('Payment method additional fee:', '7.00')
    pages.shoppingCart.checkthePrices('Tax:', '0.00')
    pages.shoppingCart.checkthePrices('Total:', '19.00')
    page.locator(pages.shoppingCart.ConfirmBtn).click()
    page.wait_for_timeout(2000)
    pages.assertions.AssertErrorMessagAppears(pages.shoppingCart.ConfirmMessage,"Your order has been successfully processed!")
    pages.basics.logout_after_test()


    


  