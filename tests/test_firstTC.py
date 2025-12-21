from playwright.sync_api import Playwright, Page
from pages.page_setup import init_pages
import pytest

@pytest.mark.smoketest
def test_OpendemowebshopandRegister(BrowserInstance, page:Page, playwright:Playwright,config ):
    page = BrowserInstance
    pages = init_pages(page)
    pages.login.open(config["base_url"])