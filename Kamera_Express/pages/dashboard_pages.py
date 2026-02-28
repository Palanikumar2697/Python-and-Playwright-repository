class Dashboard:
    def __init__(self, page):
        self.page = page
        self.cookie_accept = page.locator('button:has-text("Accept all")')
        self.login = page.locator('(//div[@class="login-button"])[2]')
        self.login_button_popup = page.locator('(//a[@href="/login"])[2]')
        self.email = page.locator('//input[@type="email"]')
        self.password = page.locator('//input[@type="password"]')
        self.login_submit = page.locator('//input[@id="btn_login"]')

    def accept_cookies(self):
        try:
            if self.cookie_accept.is_visible():
                self.cookie_accept.click()
        except:
            pass

    def open_login_popup(self):
        self.login.hover()
        self.login_button_popup.click()

    def login_click(self):
        self.email.fill('testuser@gmail.com')
        self.password.fill('User@123')
        self.login_submit.click()
        self.page.wait_for_timeout(10000)
        
        