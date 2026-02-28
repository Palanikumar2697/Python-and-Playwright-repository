import pytest
from playwright.sync_api import sync_playwright
from config import BASE_URL

@pytest.fixture(scope="session")

def page(request):
    p = sync_playwright().start()
    browser=p.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    page.goto(BASE_URL)
    page.wait_for_load_state("load")
    
    
    yield page

    context.close()
    browser.close()
    p.stop()