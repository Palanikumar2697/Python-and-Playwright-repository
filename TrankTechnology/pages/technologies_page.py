class Technology:
    def __init__(self, page):
        self.page = page

        # Main Technology menu
        self.technology = page.locator('(//li[@class="drop_down"][2])')

        # Overall menus under verticals
        self.eCommerce_Development = page.locator('//strong[text()="eCommerce Development"]')
        self.mobile_app_development = page.locator('//strong[text()="Mobile App Development"]')
        self.artifical_intelligence = page.locator('//strong[text()="Artificial Intelligence"]')

        # Ecommerce Development
        self.magento_development = page.locator('//a[text()="Magento Development"]')
        self.openacart_development = page.locator('(//a[text()="Opencart Development"])[1]')
        self.codeigniter_development = page.locator('(//a[text()="Codeigniter Development"])[1]')
        self.wordpress_development = page.locator('(//a[text()="WordPress Development"])[1]')
        self.big_commerce = page.locator('(//a[text()="Big Commerce"])[1]')
        self.shofiy_development = page.locator('(//a[text()="Shopify Development"])[1]')
        self.cs_dart_development = page.locator('(//a[text()="CS-Cart Development"])[1]')
        self.nodejs_development = page.locator('(//a[text()="Node JS Development"])[1]')
        self.nope_development = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.woocomerce = page.locator('(//a[text()="Woo Commerce"])[1]')
        self.larvel_development = page.locator('(//a[text()="Laravel Development"])[1]')
        self.Prestashop_Development = page.locator('(//a[text()="Prestashop Development"])[1]')
        self.drupal_development = page.locator('(//a[text()="Drupal Development"])[1]')
        self.wix_development = page.locator('(//a[text()="Wix Development"])[1]')
        self.joomla_development = page.locator('(//a[text()="Joomla Development"])[1]')
        self.reactjs_development = page.locator('(//a[text()="React JS Development"])[1]')
        self.expressjs_development = page.locator('(//a[text()="Express JS Development"])[1]')

        # Mobile App Development
        self.reactivemobile_app_development = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.enterprise_app_development = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.xamarin_development = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.kotlin_development = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.flutter_mobile_development = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.iconic_development = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.swift_mobile_development = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.appointment_development = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')

    def technology_mousehover(self):
        self.technology.hover()

  
    def eCommerce_Development_mousehover(self):
        self.eCommerce_Development.hover()

    def mobile_app_development_mousehover(self):
        self.mobile_app_development.hover()

    def artifical_intelligence_mousehover(self):
        self.artifical_intelligence.hover()

    def eCommerce_Development_Submenu(self):
        self.lstecommerce_development = [
            self.magento_development,
            self.openacart_development,
            self.codeigniter_development,
            self.wordpress_development,
            self.big_commerce,
            self.shofiy_development,
            self.cs_dart_development,
            self.nodejs_development,
            self.nope_development,
            self.woocomerce,
            self.larvel_development,
            self.Prestashop_Development,
            self.drupal_development,
            self.wix_development,
            self.joomla_development,
            self.reactjs_development,
            self.expressjs_development
        ]

        for i in self.lstecommerce_development:
            self.technology_mousehover()
            self.eCommerce_Development_mousehover()
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()

    def mobile_app_development_click(self):
        self.lstmobile_app_development = [
            self.reactivemobile_app_development,
            self.enterprise_app_development,
            self.xamarin_development,
            self.kotlin_development,
            self.flutter_mobile_development,
            self.iconic_development,
            self.swift_mobile_development,
            self.appointment_development
        ]

        for j in self.lstmobile_app_development:
            self.technology_mousehover()
            self.mobile_app_development_mousehover()
            j.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
  
    def artifical_intelligence_click(self):
          self.technology_mousehover()
          self.artifical_intelligence_mousehover()
          self.page.wait_for_timeout(3000)
          self.page.go_back()