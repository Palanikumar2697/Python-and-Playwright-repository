class Navigation:

    def __init__(self, page):
        self.page = page
        self.producten = page.get_by_role(
            "link", name="Producten", exact=True
        )
        self.main_menus = page.locator("a.dropdown-btn")

        self.merken = page.get_by_role("link", name="Merken", exact=True)
        self.inspiratie = page.get_by_role("link", name="Inspiratie", exact=True)
        self.Opruiming = page.get_by_role("link", name="Opruiming", exact=True)


    def hover_all_main_menus(self):
        for i in range(self.main_menus.count()):
            self.main_menus.nth(i).hover()

    def hover_producten_and_side_menu(self):

        # Hover main menu first
        self.producten.hover()

        self.page.wait_for_selector("#Producten-tab", state="visible")

        side_items = self.page.locator("#Producten-tab a:visible")

        for i in range(side_items.count()):
            self.producten.hover()
            side_items.nth(i).hover()
            self.page.wait_for_timeout(1000)
    
    def hover_marken_and_side_menu(self):

     self.merken.hover()
     self.page.wait_for_selector("#Merken-tab", state="visible")

     side_items = self.page.locator("#Merken-tab a")

    # Validate links exist
     assert side_items.count() > 0

    # Only test first 30 (avoid scroll issues)
     for i in range(min(30, side_items.count())):
        item = side_items.nth(i)
        if item.is_visible():
            item.hover()
        self.page.wait_for_timeout(1000)

    def hover_inspiratie_and_side_menu(self):

     self.inspiratie.hover()
     self.page.wait_for_selector("#Inspiratie-tab", state="visible")

    # Only visible links
     side_items = self.page.locator("#Inspiratie-tab a:visible")

     count = side_items.count()
     print(f"Visible Inspiratie submenu items: {count}")

     for i in range(count):
        self.inspiratie.hover()  # keep menu open

        item = side_items.nth(i)

        # No need scroll now
        item.hover()

        self.page.wait_for_timeout(800)
    def Opruiming_menu_click(self):

    # Click Opruiming menu
     self.Opruiming.click()

    # Add Steiner Wildlife 8x42 to cart
     product = self.page.locator(
        "a.product-card-outer-container",
        has_text="Steiner Wildlife 8x42"
    )

     product.locator("div.cta-container button").click()

    # Click visible "Bestellen" button inside cart drawer
     self.page.get_by_role("button", name="Bestellen").click()

     self.page.get_by_role("button", name=" Doorgaan met bestellen").first.click()

     self.page.locator("button[data-dd-action-name='order-and-pay']").click()

      
           
          
    