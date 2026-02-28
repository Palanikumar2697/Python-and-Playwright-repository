from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://uncodemy.com/')
    page.wait_for_timeout(4000)

#     page.locator('//span[@id="categoriesBtn"]').hover()
#     page.locator('//a[text()="Full-Stack-Development"]').hover()
#     page.wait_for_timeout(4000)
    
#     full_stack_development = [
#     page.locator('//a[text()="Full Stack With NodeJs"]'),
#     page.locator('//a[text()="Python Full Stack"]'),
#     page.locator('//a[normalize-space()="Java Full Stack Using React"]'),
#     page.locator('//a[contains(text(),"Web Designing")]'),
#     page.locator('//a[text()="Web Development"]'),
#     page.locator('//a[contains(text(),"Frontend")]'),
#     page.locator('//a[contains(text(),"Angular")]'),
#     page.locator('//a[contains(text(),"ReactJs")]'),
#     page.locator('//a[text()="Data Structureand Algorithm"]'),
#     page.locator('//a[contains(text(),"Mean")]'),
#     page.locator('//a[contains(text(),"Mern")]')
# ]
    
#     for i in full_stack_development:
#         print(i)
#         page.wait_for_timeout(4000)
    page.locator('//span[@id="categoriesBtn"]').hover()
    page.locator('//a[text()="Data Science"]').hover()
    page.wait_for_timeout(4000)    
    data_science=[
    page.locator('//a[text()="Business Analytics"]'),
    page.locator('//a[text()="Python"]'),
    page.locator('//a[text()="Data Analytics using Python"]'),
    page.locator('//a[contains(text()="Data Science & Machine")]')

]
    
    for i in data_science:
       print(i)
       page.wait_for_timeout(2000)

   
 
    