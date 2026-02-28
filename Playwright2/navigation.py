from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    #Navigate to URL for automation
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #Wait for 5 seconds to see the URL
    page.wait_for_timeout(5000)
    #Locator using tagname with name
    page.locator('//input[@name="username"]').fill('admin')
    page.wait_for_timeout(3000)
    page.locator('//input[@name="password"]').fill('admin123')
    page.wait_for_timeout(3000)
    page.locator('//button[@type="submit"]').click(force=True)
    page.wait_for_timeout(3000)
    page.go_back()
    page.wait_for_timeout(2000)
    page.go_forward()
    page.wait_for_timeout(2000)
    page.reload()
    page.wait_for_timeout(3000)
