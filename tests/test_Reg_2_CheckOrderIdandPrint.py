from playwright.sync_api import Playwright, Page, expect
from pages.page_setup import init_pages
import pytest
import re

@pytest.mark.regression
def test_2_Reg_CheckOrderIdandPrint(BrowserInstance, page:Page, config, test_data ):
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
    page.wait_for_timeout(5000)
    pages.apparelshoes.AddItemsTocart(pages.apparelshoes.GolfBelt)
    page.locator(pages.shoppingCart.Cart).click()
    page.wait_for_timeout(5000)
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
    Order = page.locator(".details").text_content()
    OrderNumber = re.search(r"Order number:\s*(\d+)", Order or "").group(1)
    with open("order_number.txt", "w") as f:
        f.write(OrderNumber)
    print("Saved Ordernumber:",OrderNumber)
    page.locator('a[href^="/orderdetails/"]').click()
    expect(page.locator(".order-number")).to_contain_text(OrderNumber)
    pages.basics.download_file(OrderNumber)
    page.wait_for_timeout(5000)
    page.pause()
    pages.basics.logout_after_test()


    


  