from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(3000)
    page.locator('//input[@id="name"]').fill('Arun')
    page.wait_for_timeout(3000)
    page.locator('//input[@placeholder="Enter EMail"]').type('test@abc.com')
    page.wait_for_timeout(3000)
    page.locator('//input[@placeholder="Enter Phone"]').fill('98277266266')
    page.wait_for_timeout(3000)
    page.locator('//textarea[@id="textarea"]').type('test address,xyz,72772')
    page.wait_for_timeout(3000)
    page.locator('//input[@id="male"]').click()
    page.wait_for_timeout(3000)
    page.locator('//input[@id="female"]').click()
    page.wait_for_timeout(3000)
    page.locator('//input[@value="sunday"]').check()
    page.wait_for_timeout(3000)
    page.locator('(//input[@type="checkbox"])[2]').check()
    page.wait_for_timeout(3000)
    page.locator('(//input[@type="checkbox"])[4]').check()
    page.wait_for_timeout(3000)
    page.locator('(//input[@type="checkbox"])[2]').uncheck()
    page.wait_for_timeout(3000)
    page.locator('(//input[@type="checkbox"])[5]').check()
    page.wait_for_timeout(3000)
    page.locator('(//input[@type="checkbox"])[6]').check()
    page.wait_for_timeout(3000)
    page.locator('(//input[@type="checkbox"])[7]').check()
    page.wait_for_timeout(3000)
    dropdown = page.locator('#country')
    options = page.locator('#country option')
    count = options.count()

    for i in range(count):
       value = options.nth(i).get_attribute("value")
       dropdown.select_option(value)
       page.wait_for_timeout(1000)  
    
    dropdown = page.locator('#colors')
    options = dropdown.locator('option')

    values = []

    for i in range(options.count()):
      value = options.nth(i).get_attribute("value")
      values.append(value)

# Remove duplicates but preserve order
    unique_values = list(dict.fromkeys(values))

    print(unique_values)

    dropdown.select_option(unique_values)

    selected = dropdown.evaluate(
    "el => Array.from(el.selectedOptions).map(o => o.value)"
)

    print(selected)




    dropdown = page.locator('#animals')
    options = dropdown.locator('option')

    values = []

    for i in range(options.count()):
       option = options.nth(i)
       if i>=4:
        option.scroll_into_view_if_needed()
       page.wait_for_timeout(1000)
       value=option.get_attribute("value")
       values.append(value)

    dropdown.select_option(values)
    page.wait_for_timeout(1000)
    page.locator('//input[@id="datepicker"]').click()
    page.wait_for_timeout(1000)
    page.locator('//a[@data-date="15"]').click()
    page.locator('//input[@id="txtDate"]').click()
    page.locator('//a[@data-date="17"]').click()
    page.wait_for_timeout(3000)
    page.locator('//input[@placeholder="Start Date"]').click()
    page.wait_for_timeout(3000)
    page.locator('//input[@id="end-date"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@class="submit-btn"]').click()
    page.wait_for_timeout(3000)
    page.locator('//input[@id="Wikipedia1_wikipedia-search-input"]').fill('www.google.com')
    page.locator('//input[@class="wikipedia-search-button"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@name="start"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@class="stop"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@id="alertBtn"]').click()
    page.once("dialog", lambda dialog: dialog.dismiss()) 
    page.wait_for_timeout(3000)
    page.locator('//button[@id="confirmBtn"]').click()
    page.once("dialog", lambda dialog: dialog.accept())
    page.wait_for_timeout(3000)
    page.locator('//button[@id="promptBtn"]').click()
    page.once("dialog", lambda dialog: dialog.accept("Nan2"))
    page.once("dialog", lambda dialog: dialog.dismiss()) 
    page.wait_for_timeout(3000)
    page.locator('//button[@onclick="myFunction()"]').click()
    page.wait_for_timeout(3000)
    page.locator('//button[@id="PopUp"]').click()
    page.wait_for_timeout(2000)

    



 

    


