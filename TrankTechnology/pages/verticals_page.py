
class Verticals:
    def __init__(self, page):
        self.page = page

        # Main verticals menu
        self.verticals = page.locator('(//li[@class="drop_down"])[1]')

        # Overall menus under verticals
        self.trading = self.page.locator('(//a[@href="#"])[3]')
        self.retail_and_ecommerce = self.page.locator('//li[@data-id="retailEcommerce"]')
        self.healthcare = self.page.locator('//li[@data-id="healthcare"]')
        self.fintech = self.page.locator('//li[@data-id="fintech"]')
        self.custom_app = self.page.locator('//li[@data-id="customApp"]')

        # Trading menu items
        self.stock_trading = self.page.locator('(//a[@class="mm-active"])[1]')
        self.paper_trading = self.page.locator('//a[text()="Paper Trading"]')
        self.cfd_trading = self.page.locator('(//a[text()="CFD Trading"])[1]')
        self.trading_app_development = self.page.locator(
            '(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]'
        )
        self.algo_trading = self.page.locator('//a[text()="Algo Trading"]')
        self.custom_trading = self.page.locator(
            '(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]'
        )
        self.web_portal_trading = self.page.locator('(//a[text()="Web Portal Trading"])[1]')

        # Retail and Ecommerce
        self.ecommerce_website_development = self.page.locator(
            '(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[1]'
        )
        self.ecommerce_app_development = self.page.locator('//a[text()="eCommerce App Development"]')

        # Healthcare
        self.Diets_Nutrition = self.page.locator(
            '(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]'
        )
        self.Health_tracking_app = self.page.locator('(//a[text()="Health tracking App"])[1]')

        # Fintech
        self.pos_software_development = self.page.locator(
            '(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]'
        )
        self.Crypo =self.page.locator('(//a[text()="Crypto"])[1]')

        # Custom App
        self.desktop_app_development =self.page.locator(
            '(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]'
        )
        self.hrm_development = self.page.locator(
            '(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]'
        )
        self.crm_development = self.page.locator(
            '(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]'
        )
        self.erp_app_development = self.page.locator('(//a[text()="ERP App Development"])[1]')
        self.travel =self.page.locator('(//a[text()="Travel"])[1]')
        self.e_learning = self.page.locator('(//a[text()="E-Learning"])[1]')
        self.dating_app_development = self.page.locator(
            '(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]'
        )
        self.realstate =self.page.locator('(//a[text()="Real Estate"])[1]')
        self.crm_development_usa =self.page.locator(
            '(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]'
        )

    def vertical_mousehover(self):
        self.verticals.hover()

    def trading_mousehover(self):
        self.trading.hover()

    def retailandecommerce_mousehover(self):
        self.retail_and_ecommerce.hover()

    def healthcare_mousehover(self):
        self.healthcare.hover()

    def fintech_mousehover(self):
        self.fintech.hover()

    def customapp_mousehover(self):
        self.custom_app.hover()

    def tradingSubmenu_click(self):
        self.lsttrading = [
            self.stock_trading,
            self.paper_trading,
            self.cfd_trading,
            self.trading_app_development,
            self.algo_trading,
            self.custom_trading,
            self.web_portal_trading
        ]
        for i in self.lsttrading:
            self.vertical_mousehover()
            self.trading_mousehover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
        print('************Trading Completed**************')

    def retailandecommerce_click(self):
        self.lstretailandecommerce = [
            self.ecommerce_website_development,
            self.ecommerce_app_development
        ]
        for x in self.lstretailandecommerce:
            self.vertical_mousehover()
            self.retailandecommerce_mousehover()
            x.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
        print('************Retail and Ecommerce Completed**************')

    def healthcare_click(self):
        self.lsthealthcare = [
            self.Diets_Nutrition,
            self.Health_tracking_app
        ]
        for y in self.lsthealthcare:
            self.vertical_mousehover()
            self.healthcare_mousehover()
            y.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
        print('************Healthcare Completed**************')

    def fintech_click(self):
        self.lstfintech = [
            self.pos_software_development,
            self.Crypo
        ]
        for z in self.lstfintech:
            self.vertical_mousehover()
            self.fintech_mousehover()
            z.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
        print('************Fintech Completed**************')

    def customapp_click(self):
        self.lstcustomapp = [
            self.desktop_app_development,
            self.hrm_development,
            self.crm_development,
            self.erp_app_development,
            self.travel,
            self.e_learning,
            self.dating_app_development,
            self.realstate,
            self.crm_development_usa
        ]
        for k in self.lstcustomapp:
            self.vertical_mousehover()
            self.customapp_mousehover()
            k.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
        print('************CustomApp Completed**************')