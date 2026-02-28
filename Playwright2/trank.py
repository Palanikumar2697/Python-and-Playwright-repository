from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.tranktechnologies.com/')
    page.wait_for_url('https://www.tranktechnologies.com/')
    
    verticals=page.locator('(//li[@class="drop_down"][1])')
    page.wait_for_timeout(5000)
    #overall menus
    trading=page.locator('(//a[@href="#"])[3]')
    retail_and_ecommerce=page.locator('//li[@data-id="retailEcommerce"]')
    healthcare=page.locator('//li[@data-id="healthcare"]')
    fintech=page.locator('//li[@data-id="fintech"]')
    custom_app=page.locator('//li[@data-id="customApp"]')
    #Trading menu click
    st=page.locator('(//a[@class="mm-active"])[1]')
    pt=page.locator('//a[text()="Paper Trading"]')
    cfd=page.locator('(//a[text()="CFD Trading"])[1]')
    tad=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
    at=page.locator('//a[text()="Algo Trading"]')
    ct=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
    wpt=page.locator('(//a[text()="Web Portal Trading"])[1]')
    
    trading_rows=[st,pt,cfd,tad,at,ct,wpt]
    for i in trading_rows:
        verticals.hover()
        trading.hover()
        i.click()
        page.wait_for_timeout(3000)
        page.go_back()

    ewd=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company-in-india"])[1]')
    ead=page.locator('//a[text()="eCommerce App Development"]')

    retail_and_ecommerce_rows=[ewd,ead]
    for j in retail_and_ecommerce_rows:
       verticals.hover()
       retail_and_ecommerce.hover()
       j.click()
       page.wait_for_timeout(3000)
       page.go_back()

    dn=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
    hta=page.locator('(//a[text()="Health tracking App"])[1]')

    healthcare_rows=[dn,hta]
    for z in healthcare_rows:
        verticals.hover()
        healthcare.hover()
        z.click()
        page.wait_for_timeout(3000)
        page.go_back()
    psd=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
    crypto=page.locator('(//a[text()="Crypto"])[1]')

    fintech_rows=[psd,crypto]
    for y in fintech_rows:
        verticals.hover()
        fintech.hover()
        y.click()
        page.wait_for_timeout(3000)
        page.go_back()
    dad=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
    hrm=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
    crm=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
    erp=page.locator('(//a[text()="ERP App Development"])[1]')
    travel=page.locator('(//a[text()="Travel"])[1]')
    el=page.locator('(//a[text()="E-Learning"])[1]')
    dad1=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
    re=page.locator('(//a[text()="Real Estate"])[1]')
    crmu=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')

    custom_app_rows=[dad,hrm,crm,erp,travel,el,dad1,re,crmu]
    for c in custom_app_rows:
        verticals.hover()
        custom_app.hover()
        c.click()
        page.wait_for_timeout(3000)
        page.go_back()
       

    
       



