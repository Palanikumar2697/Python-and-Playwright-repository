

class Blog:
    def __init__(self, page):
        self.page = page
        self.blog = page.locator('(//a[text()="Blog"])[1]')

        self.App_Development = page.locator('(//a[text()="App Development"])[1]')
        self.Web_Development = page.locator('(//a[text()="Web Development"])[1]')
        self.Software_Development = page.locator('(//a[text()="Software Development"])[1]')
        self.Digital_Marketing = page.locator('(//a[text()="Digital Marketing"])[1]')
        self.Email_Marketing = page.locator('(//a[text()="Email Marketing"])[1]')
        self.Artifical_Intelligence = page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
        self.UI_UX_Design = page.locator('//a[@href="/blog/category/ui-ux-design/"]')

    def Blog_Submenu(self):
        self.blog.click()

        self.listBlogus = [
            self.App_Development,
            self.Web_Development,
            self.Software_Development,
            self.Digital_Marketing,
            self.Email_Marketing,
            self.Artifical_Intelligence,
            self.UI_UX_Design
        ]

        for i in self.listBlogus:
            i.click()
            self.page.wait_for_timeout(3000)
            self.page.go_back()
        self.search=self.page.locator('//span[@class="search"]')
        self.search.click()
        self.searchInput=self.page.locator('//input[@class="search_text"]').fill('How Much Does It Cost to Build a Website in 2025?')
        self.searchresults=self.page.locator('//button[@class="search_submit"]').click()
        self.page.wait_for_timeout(3000)