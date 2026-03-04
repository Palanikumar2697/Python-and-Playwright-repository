import pytest
from config import BASE_URL
from pages.dashboard_pages import Dashboard
from pages.navigation_pages import Navigation


@pytest.mark.smoke
def test_login(page):
    page.goto(BASE_URL)
    dashboard=Dashboard(page)
    dashboard.accept_cookies()
    dashboard.open_login_popup()
    dashboard.login_click()

def test_navigation(page):
    nav = Navigation(page)

    # nav.hover_all_main_menus()
    # nav.hover_producten_and_side_menu()
    # nav.hover_marken_and_side_menu()
    # nav.hover_inspiratie_and_side_menu()
    nav.Opruiming_menu_click()
    # nav.Acties_menu_click()
    # nav.Search_Products()
    
   

   
    