from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.automationtesting.co.uk/dropdown.html#")
    page.wait_for_timeout(5000)
    cars= page.locator('//select[@id="cars"]')
    options = cars.locator('option')
    count = options.count()
    for i in range(count):
        cars.select_option(index=1)
        page.wait_for_timeout(5000)
    
    page.goto('https://www.globalsqa.com/demo-site/select-dropdown-menu/')
    page.wait_for_timeout(3000)
    country= page.locator('select:visible').click()
    page.wait_for_timeout(2000)
    options =country.locator('option')
    count=options.count()
    for y in range(count):
        
    # cars.select_option('Honda')
    # page.wait_for_timeout(5000)
    # cars.select_option('Jeep')
    # page.wait_for_timeout(5000)
    # cars.select_option('BMW')
    # page.wait_for_timeout(5000)

