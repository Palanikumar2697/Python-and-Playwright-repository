import pytest
from config import BASE_URL
from pages.verticals_page import Verticals
from pages.technologies_page import Technology
from pages.aboutus_page import AboutUs
from pages.blog_page import Blog
from pages.contact_us_page import ContactUs
from pages.portfolio_page import Portfolio

@pytest.mark.smoke
def test_verticals(page):
    page.goto(BASE_URL)
    verticals = Verticals(page)
    verticals.tradingSubmenu_click()
    verticals.retailandecommerce_click()
    verticals.healthcare_click()
    verticals.fintech_click()
    verticals.customapp_click()

def test_technology(page):
    page.goto(BASE_URL)
    technology=Technology(page)
    technology.eCommerce_Development_Submenu()
    technology.mobile_app_development_click()
    technology.artifical_intelligence_click()

def test_aboutus(page):
    page.goto(BASE_URL)
    aboutus=AboutUs(page)
    aboutus.aboutus_click()

def test_blog(page):
    page.goto(BASE_URL)
    blog=Blog(page)
    blog.Blog_Submenu()

def test_contactus(page):
    page.goto(BASE_URL)
    contactus=ContactUs(page)
    contactus.fill_contact_form()

def test_portfolio(page):
    page.goto(BASE_URL)
    portfolio=Portfolio(page)
    portfolio.portfolio_click()