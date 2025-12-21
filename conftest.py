
import os
from dotenv import load_dotenv
import pytest
from pathlib import Path
import requests
import json
load_dotenv()

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")

@pytest.fixture(scope="function")
def BrowserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    raw_name = request.node.nodeid
    test_name =  "".join(c if c.isalnum() or c in ".-" else "_" for c in raw_name)
    if browser_name == "edge":
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], channel="msedge")
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False, args=["--start-maximized"])
    else:
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(
        no_viewport=True,
        record_video_dir=(f"C:/Users/nourahme/DemoWebShop/reports/videos/{test_name}"))
    page = context.new_page()
    yield page
    context.close()
    browser.close()
@pytest.fixture(scope="session")
def config():
    return {"base_url": os.getenv("BASE_URL")}
# ---------------------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
# ------------------------------------------------------
@pytest.fixture(autouse=True)
def trace_and_screenshot(BrowserInstance, request):
    page = BrowserInstance
    context = page.context
    raw_name = request.node.nodeid
    test_name =  "".join(c if c.isalnum() or c in ".-" else "_" for c in raw_name)
    base_dir = Path(r"C:/Users/nourahme/DemoWebShop/reports")
    traces_dir = base_dir / "traces"
    screenshots_dir = base_dir / "screenshots" / test_name
    traces_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    context.tracing.start(screenshots=True,snapshots=True,sources=True,)
    yield
    rep_call = getattr(request.node, "rep_call", None)
    failed = bool(rep_call and rep_call.failed)
    if failed:
        try:
            title = page.title() or test_name
            safe_title = "".join(c if c.isalnum() or c in ".-" else "" for c in title)
            page.screenshot(path=str(screenshots_dir / f"{safe_title}.png"),full_page=True,)
        except Exception:
            pass
    context.tracing.stop(path=str(traces_dir / f"{test_name}-trace.zip"))
#---------------------------------------------
@pytest.fixture(scope="session")
def test_data():
    data_dir = Path(__file__).parent / "data"
    all_data = {}
    for file_path in data_dir.glob("*.json"):
        key = file_path.stem
        with file_path.open("r", encoding="utf-8") as f:
            all_data[key] = json.load(f)
    return all_data
     