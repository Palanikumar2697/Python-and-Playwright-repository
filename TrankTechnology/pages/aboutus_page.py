class AboutUs:
    def __init__(self,page):
        self.page=page
        self.about_us=page.locator('(//a[text()="About us"])[1]')

    def aboutus_click(self):
        self.about_us.click()
        self.page.wait_for_timeout(3000)
        self.page.go_back()
    
    
