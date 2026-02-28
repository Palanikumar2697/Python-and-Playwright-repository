from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.globalsqa.com/demo-site/draganddrop/")
    frame=page.frame_locator('(//iframe[@class="demo-frame"])[1]')
    img1=frame.locator('//img[@alt="The peaks of High Tatras"]')
    trash=frame.locator('//div[@id="trash"]')
    img2=frame.locator('//img[@alt="The chalet at the Green mountain lake"]')
    img3=frame.locator('//img[@alt="Planning the ascent"]')
    img4=frame.locator('//img[@alt="On top of Kozi kopka"]')
    def images_draganddrop():
      images=[img1,img2,img3,img3,img4]
      for i in images:
        i.drag_to(trash)
    
      page.wait_for_timeout(3000)
    images_draganddrop()
