import os
from dotenv import load_dotenv
import pytest
from pathlib import Path
import json
import shutil
load_dotenv()

pytest.hookimpl(hookwrapper=True, trylast=True)
def pytest_runtest_makereport(item, call):
   
    rep = pytest.TestReport.from_item_and_call(item, call)
    setattr(item, "rep_" + rep.when, rep)
    return rep

#---------------------------------------------------------------------
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
#---------------------------------------------------------------------
@pytest.fixture(scope="function")
def BrowserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    raw_name = request.node.name
    test_name = "".join(c if c.isalnum() or c in ".-" else "_" for c in raw_name)
    if browser_name == "edge":
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"], channel="msedge")
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False, args=["--start-maximized"])
    else:
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    videos_dir = Path(rf"C:/Users/nourahme/DemoWebShop/reports/videos/{test_name}")
    context = browser.new_context(no_viewport=True, record_video_dir=str(videos_dir))
    page = context.new_page()
    yield page
    context.close()
    browser.close()
    failed = getattr(request.node, "_failed_call", False)
    if not failed:
        try:
            if videos_dir.exists():
                shutil.rmtree(videos_dir, ignore_errors=True)
        except Exception:
            pass
#---------------------------------------------------------------------
@pytest.fixture(scope="session")
def config():
    return {"base_url": os.getenv("BASE_URL")}
#---------------------------------------------------------------------
@pytest.fixture(autouse=True)
def trace_and_screenshot(BrowserInstance, request):
    page = BrowserInstance
    context = page.context
    raw_name = request.node.name
    test_name = "".join(c if c.isalnum() or c in ".-" else "_" for c in raw_name)
    base_dir = Path(r"C:/Users/nourahme/DemoWebShop/reports")
    traces_dir = base_dir / "traces"
    screenshots_dir = base_dir / "screenshots" 
    traces_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    rep_call = getattr(request.node, "rep_call", None)
    failed = bool(rep_call and rep_call.failed)
    setattr(request.node, "_failed_call", failed)
    if failed:
        try:
            screenshot_path = screenshots_dir / f"{test_name}.png"
            page.screenshot(path=str(screenshot_path), full_page=True)
        except Exception:
            pass
    if failed:
        context.tracing.stop(path=str(traces_dir / f"{test_name}-trace.zip"))
    else:
        context.tracing.stop()
#---------------------------------------------------------------------
@pytest.fixture(scope="session")
def test_data():
    data_dir = Path(__file__).parent / "data"
    all_data = {}
    if data_dir.exists():
        for file_path in data_dir.glob("*.json"):
            key = file_path.stem
            with file_path.open("r", encoding="utf-8") as f:
                all_data[key] = json.load(f)
    return all_data
#-----------------------------------------
@pytest.fixture(scope="session")
def buffer():
    return {}
@pytest.fixture()
def remember(buffer):
    def _remember(key, value):
        buffer[key]= value
        return value
    return _remember

@pytest.fixture()
def recall(buffer):
    def _recall(key, default=None):
        return buffer.get(key, default)
    return recall
