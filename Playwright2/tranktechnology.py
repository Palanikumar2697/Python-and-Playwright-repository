from playwright.sync_api import sync_playwright
import os

# Create screenshot folder
os.makedirs("screenshotstest1", exist_ok=True)

def click_menu_items(page, main_menu, sub_menu, items, menu_name):
    submenu_count = 0

    print(f"\n🔷 Starting traversal for: {menu_name}")

    for index, item in enumerate(items, start=1):
        main_menu.hover()
        sub_menu.hover()

        item.wait_for(state="visible", timeout=10000)

        # Screenshot before click
        page.screenshot(path=f"screenshots/{menu_name}_submenu_{index}_before.png")

        submenu_text = item.inner_text().strip()
        print(f"   ➜ Clicking Submenu {index}: {submenu_text}")

        item.click()
        page.wait_for_load_state("domcontentloaded")

        # Screenshot after navigation
        page.screenshot(path=f"screenshots/{menu_name}_submenu_{index}_after.png")

        submenu_count += 1

        page.go_back()
        page.wait_for_load_state("domcontentloaded")

    print(f"✅ Completed {menu_name} | Total Submenus Traversed: {submenu_count}")
    return submenu_count


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://www.tranktechnologies.com/')
    page.wait_for_load_state("domcontentloaded")

    verticals = page.locator('(//li[@class="drop_down"][1])')

    # Overall menus
    trading = page.locator('(//a[@href="#"])[3]')
    retail_and_ecommerce = page.locator('//li[@data-id="retailEcommerce"]')
    healthcare = page.locator('//li[@data-id="healthcare"]')
    fintech = page.locator('//li[@data-id="fintech"]')
    custom_app = page.locator('//li[@data-id="customApp"]')

    # Trading
    trading_rows = [
        page.locator('(//a[@class="mm-active"])[1]'),
        page.locator('//a[text()="Paper Trading"]'),
        page.locator('(//a[text()="CFD Trading"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]'),
        page.locator('//a[text()="Algo Trading"]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]'),
        page.locator('(//a[text()="Web Portal Trading"])[1]')
    ]

    # Retail & Ecommerce
    retail_rows = [
        page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[1]'),
        page.locator('//a[text()="eCommerce App Development"]')
    ]

    # Healthcare
    healthcare_rows = [
        page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]'),
        page.locator('(//a[text()="Health tracking App"])[1]')
    ]

    # Fintech
    fintech_rows = [
        page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]'),
        page.locator('(//a[text()="Crypto"])[1]')
    ]

    # Custom App
    custom_app_rows = [
        page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]'),
        page.locator('(//a[text()="ERP App Development"])[1]'),
        page.locator('(//a[text()="Travel"])[1]'),
        page.locator('(//a[text()="E-Learning"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]'),
        page.locator('(//a[text()="Real Estate"])[1]'),
        page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
    ]

    total_count = 0

    total_count += click_menu_items(page, verticals, trading, trading_rows, "Trading")
    total_count += click_menu_items(page, verticals, retail_and_ecommerce, retail_rows, "Retail")
    total_count += click_menu_items(page, verticals, healthcare, healthcare_rows, "Healthcare")
    total_count += click_menu_items(page, verticals, fintech, fintech_rows, "Fintech")
    total_count += click_menu_items(page, verticals, custom_app, custom_app_rows, "CustomApp")

    print("\n🎯 TOTAL SUBMENUS TRAVERSED:", total_count)

    browser.close()
