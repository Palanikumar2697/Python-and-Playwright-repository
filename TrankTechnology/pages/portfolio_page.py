class Portfolio:
    def __init__(self,page):
        self.page=page
        self.portfolio=page.locator('//a[text()="Portfolio"]')
    def portfolio_click(self):
        self.portfolio.click()
        self.page.wait_for_timeout(3000)
        
       