class ContactUs:
    def __init__(self, page):
        self.page = page

        # Contact Us menu
        self.contact_us = page.locator('(//a[text()="Contact us"])[1]')

        # Contact Form fields
        self.name = page.locator('(//input[@placeholder="Your Name"])[2]')
        self.email = page.locator('//input[@id="email_contact"]')
        self.send_otp = page.locator('//button[@id="send_otp"]')
        self.otp = page.locator('(//input[@placeholder="Enter OTP"])[2]')
        self.company = page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service = page.locator('(//select[@name="service"])[2]')
        self.phone = page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message = page.locator('(//textarea[@name="message"])[2]')
        self.submit = page.locator('//input[@name="contact"]')

    # 
    def fill_contact_form(self):
        self.contact_us.click()

        self.name.fill("Test")
        self.email.fill("mytest123@test.com")
        self.company.fill("ABC Pvt Ltd")
        self.phone.fill("9876543210")
        self.message.fill("Testing automation contact form")

        self.service.select_option(index=4)

        # # OTP if required
        # self.send_otp.click()
        # self.otp.fill("1234")

        # self.submit.click()

        self.page.wait_for_timeout(3000)