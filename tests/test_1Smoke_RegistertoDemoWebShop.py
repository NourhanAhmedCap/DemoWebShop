from playwright.sync_api import Playwright, Page, expect
from pages.page_setup import init_pages
import pytest

@pytest.mark.smoketest
def test_OpendemowebshopandRegister(BrowserInstance, page:Page, config, test_data ):
    page = BrowserInstance
    user = test_data["data"]["valid_user"]
    pages = init_pages(page)
    pages.login.open(config["base_url"])
    page.locator(pages.login.Register).click()
    page.locator(pages.login.GenderFemale).click()
    page.locator(pages.login.Firstname).fill(user["FirstName"])
    page.locator(pages.login.Lastname).fill(user["LastName"])
    page.locator(pages.login.Email).fill(user["Email"])
    page.locator(pages.login.Password).fill(user["Password"])
    page.locator(pages.login.ConfirmPassword).fill(user["Password"])
    page.locator(pages.login.RegisterButtn).click()
    pages.assertions.AssertElementVsisble(pages.login.RegisterMessage)
    pages.basics.logout_after_test()



