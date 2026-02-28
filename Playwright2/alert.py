# Alert 
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")

    # ————————————————
    # 1) Simple Alert
    # Attach listener BEFORE the click
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator('//button[@class="btn btn-danger"]').click()
    page.wait_for_timeout(2000)
    
    # ————————————————
    # 2) Confirm Box
    page.locator('(//a[@class="analystic"])[2]').click()
    page.once("dialog", lambda dialog: dialog.dismiss())   # OK
    page.locator('//button[@onclick="confirmbox()"]').click()
    page.wait_for_timeout(2000)

    # ————————————————
    # 3) Prompt Box
    page.locator('(//a[@class="analystic"])[3]').click()
    page.once("dialog", lambda dialog: dialog.accept("Sandhya"))
    page.locator('//button[@onclick="promptbox()"]').click()
    page.wait_for_timeout(2000)