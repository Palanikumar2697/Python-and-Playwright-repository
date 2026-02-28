from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # page.wait_for_timeout(5000)
    print("url is launched")
    page.locator('//input[@name="username"]').fill("Admin")
    page.wait_for_timeout(2000)
    page.locator('//input[@name="password"]').fill("admin123")
    page.wait_for_timeout(5000)
    page.locator('//button[@type="submit"]').click()
    page.wait_for_timeout(5000)

    # page.locator('//button[@type="submit"]').click(force=True)
    page.screenshot(path="//Users/sgnormal/Desktop/Myfiles/myscreenshot.png")
    # force=True -> for clicking forcefully if any response is slow
    page.wait_for_timeout(8000)
    page.close
    
 