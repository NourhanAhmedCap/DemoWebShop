import pytest
import os
from dotenv import load_dotenv
load_dotenv()
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",)
@pytest.fixture(scope="session")
def BrowserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "edge":
         browser = playwright.chromium.launch(headless=False,args=["--start-maximized"], channel="msedge")
    elif browser_name == "firefox":
         browser = playwright.firefox.launch(headless=False,args=["--start-maximized"])
    else:
        browser = playwright.chromium.launch(headless=False,args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)    
    page = context.new_page()
    yield page
    context.close()
    browser.close()

@pytest.fixture(scope="session")
def config():
    return {
        "base_url": os.getenv("BASE_URL")}