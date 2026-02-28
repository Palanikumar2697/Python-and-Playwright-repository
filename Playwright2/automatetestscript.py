from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Index.html")
    page.wait_for_timeout(5000)
    page.locator('//input[@id="email"]').fill('test@gmail.com')
    page.wait_for_timeout(5000)
    page.locator('#enterimg').click()
    page.get_by_text("Home").click();
    page.wait_for_timeout(5000)
    page.locator('//button[@id="btn1"]').click()
    page.wait_for_timeout(5000)
    page.locator('//input[@placeholder="E mail"]').fill('test@mail.com')
    page.wait_for_timeout(5000)
    page.locator('//input[@type="password"]').fill('Admin123')
    page.wait_for_timeout(5000)
    page.locator('#enterbtn').click()
    page.wait_for_timeout(5000)
