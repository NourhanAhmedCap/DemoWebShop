from playwright.sync_api import Playwright, Page, expect
from pages.page_setup import init_pages
import pytest

@pytest.mark.smoketest
def test_3_Smoke_LoginWithInvalidCredin(BrowserInstance, page:Page, config, test_data ):
    page = BrowserInstance
    user = test_data["data"]["valid_user"]
    pages = init_pages(page)
    pages.login.open(config["base_url"])
    page.locator(pages.login.LOGIN_BUTTON).click()
    page.locator(pages.login.Email).fill(user["Email"])
    page.locator(pages.login.Password).fill(user["WrongPAssword"])
    page.locator(pages.login.RememberMe).click()
    page.locator(pages.login.LoginToAccount).click()
    pages.assertions.AssertErrorMessagAppears(pages.login.LoginErrorMessage, "Login was unsuccessful. Please correct the errors and try again. The credentials provided are incorrect")

