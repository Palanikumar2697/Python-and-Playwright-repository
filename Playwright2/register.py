from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")

    # Text fields
    page.locator('input[placeholder="First Name"]').fill("Test")
    page.locator('input[placeholder="Last Name"]').fill("Palz")
    page.locator('textarea[ng-model="Adress"]').fill("XYZ, test address, test City")
    page.wait_for_timeout(3000)
    page.locator('//input[@id="imagesrc"]').set_input_files(
    '/Users/sgnormal/Desktop/KET_Array_1765361705.pdf'
)
    page.wait_for_timeout(3000)
    page.locator('input[type="email"]').fill("test1@gmail.com")
    page.locator('input[type="tel"]').fill("7327373663")
    page.wait_for_timeout(3000)
    # Gender + Hobbies
    page.locator('input[value="FeMale"]').check()
    page.locator('#checkbox1').check()
    page.locator('#checkbox2').check()
    page.locator('input[value="Hockey"]').check()
    page.wait_for_timeout(3000)
    # Uncheck one
    page.locator('#checkbox2').uncheck()

    # Language dropdown (select few languages instead of all)
   # Open language dropdown
    page.locator('#msdd').click()

# Get all language options
    languages = page.locator('#msdd + div ul li a')

    count = languages.count()

    for i in range(count):
      languages.nth(i).click()

# Close dropdown
    page.locator('body').click()

    page.wait_for_timeout(5000)

    # Skills
    page.select_option("#Skills", label="C")
    page.wait_for_timeout(3000)
    # Country
    page.locator('//span[@class="select2-selection select2-selection--single"]').click() 
    page.locator('//input[@type="search"]').fill('India')
    page.locator('li.select2-results__option >> text=India').click()

    
    page.wait_for_timeout(3000)
    # Date of Birth
    page.select_option("#yearbox", label="1917")
    page.select_option('select[placeholder="Month"]', label="April")
    page.select_option("#daybox", label="25")
    page.wait_for_timeout(3000)
    # Password
    page.locator("#firstpassword").fill("Admin123")
    page.locator("#secondpassword").fill("Admin123")
    page.wait_for_timeout(5000)
    page.locator('//button[@id="submitbtn"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@id="Button1"]').click();
    page.wait_for_timeout(5000)