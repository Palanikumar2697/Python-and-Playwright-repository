from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    #Navigate to URL for automation
    page.goto("https://www.saucedemo.com/")
    #Wait for 5 seconds to see the URL
    page.wait_for_timeout(5000)
    page.locator('//input[@id="user-name"]').fill('standard_user')
    page.wait_for_timeout(3000)
    page.locator('//input[@name="password"]').fill('secret_sauce')
    page.wait_for_timeout(3000)
    page.locator('//input[@name="login-button"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@id="add-to-cart-sauce-labs-backpack"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@id="add-to-cart-sauce-labs-onesie"]').click()
    page.wait_for_timeout(3000)
    page.locator('//a[@class="shopping_cart_link"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@name="checkout"]').click()
    page.wait_for_timeout(3000)
    page.locator('//input[@name="firstName"]').fill('Test')
    page.wait_for_timeout(3000)
    page.locator('//input[@id="last-name"]').fill("Palz")
    page.wait_for_timeout(3000)
    page.locator('//input[@data-test="postalCode"]').fill('test123')
    page.wait_for_timeout(3000)
    page.locator('//input[@id="continue"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@name="finish"]').click()
    page.wait_for_timeout(3000)
    page.wait_for_timeout(2000)
    #Back_to_home
    page.locator('//button[@id="back-to-products"]').click()
    page.wait_for_timeout(2000)







