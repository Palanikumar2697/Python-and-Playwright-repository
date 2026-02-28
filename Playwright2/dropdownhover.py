from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://uncodemy.com/')
   

    cat=page.locator('//span[@id="categoriesBtn"]')
   
    
    fsd=page.locator('//a[text()="Full-Stack-Development"]')
    ds=page.locator('//a[text()="Data Science"]')
    st= page.locator('(//a[text()="Software Testing"])[1]')
    ct= page.locator('//a[text()="Cloud Tools"]')
    dm= page.locator('(//a[text()="Digital Marketing"])[1]')
    jt= page.locator('//a[text()="Java Technology+"]')
    ns=page.locator('//a[text()="Network & Security"]')
    pl=page.locator('//a[text()="Programming Language"]')
    cad= page.locator('//a[text()="CAD Training"]')
    gd=page.locator('(//a[text()="Graphic Designing"])[1]')

   
    categories = [fsd,ds,st,ct,dm,jt,ns,pl,cad,gd]

    fswm=page.locator('//a[text()="Full Stack With NodeJs"]')
    pfs=page.locator('//a[text()="Python Full Stack"]')
    jfsur=page.locator('//a[normalize-space()="Java Full Stack Using React"]')
    wd=page.locator('//a[contains(text(),"Web Designing")]')
    wdeve= page.locator('//a[text()="Web Development"]')
    frontend=page.locator('//a[contains(text(),"Frontend")]')
    angular=page.locator('//a[contains(text(),"Angular")]')
    reactjs=page.locator('//a[contains(text(),"ReactJs")]')
    dsa=dsa = page.get_by_role("link", name="Data Structureand Algorithm")
    mean=page.locator('//a[contains(text(),"Mean")]')
    mern=page.locator('//a[contains(text(),"Mern")]')

    full_stack_development = [fswm,pfs,jfsur,wd,wdeve,frontend,angular,reactjs,dsa,mean,mern]

    for j in full_stack_development:
            cat.hover()
            fsd.hover()
            j.click()
            page.wait_for_timeout(2000)
            page.go_back()
    

    ba=page.locator('//a[text()="Business Analytics"]')
    python= page.locator('//a[text()="Python"]')
    daup=page.locator('//a[normalize-space()="Data Analytics using Python"]')
    dsml=page.locator('//a[normalize-space()="Data Science & Machine Learning using Python"]')
    mlup=page.locator('//a[normalize-space()="Machine Learning using Python"]')
    aup=page.locator('//a[normalize-space()="AI Using Python"]')
    

    data_science=[ba,python,daup,dsml,mlup,aup]

    for x in data_science:
          cat.hover()
          ds.hover()
          x.click()
          page.wait_for_timeout(2000)
          page.go_back()


    
    st1 = page.locator('(//a[text()="Software Testing"])[2]')
    mt=page.locator('//a[normalize-space()="Manual Testing"]')
    at=page.locator('//a[normalize-space()="Automation Testing"]')
    istqb=page.locator('//a[normalize-space()="ISTQB Training"]')
    mtst=page.locator('//a[normalize-space()="Manual + Selenium"]')

    software_testing=[st1,mt,at,istqb,mtst]

    for y in software_testing:
        cat.hover()
        st.hover()
        y.click()
        page.wait_for_timeout(2000)
        page.go_back()
    mz=page.locator('//a[text()="Microsoft Azure"]')
    devOps=page.locator('//a[text()="DevOps"]')
    aws=page.locator('//a[text()="Amazon Web Services (AWS)"]')
    cc=page.locator('//a[text()="Cloud Computing"]')
    sf=page.locator('//a[text()="Salesforce"]')

    cloud_tools=[mz,devOps,aws,cc,sf]
    for z  in cloud_tools:
        cat.hover()
        ct.hover()
        z.click()
        page.wait_for_timeout(2000)
        page.go_back()
    dm1=page.locator('(//a[text()="Digital Marketing"])[2]')
    adm = page.locator('//a[normalize-space()="AdvanceDigital Marketing"]')
    soe = page.locator('//a[normalize-space()="SEO(SearchEngine Optimization)"]')

    digital_marketing=[dm1,adm,soe]
    for b in digital_marketing:
         cat.hover()
         dm.hover()
         b.click()
         page.wait_for_timeout(2000)
         page.go_back()

    java=page.locator('//a[text()="Java"]')
    adm=page.locator('//a[normalize-space()="Java ForBeginners"]')
    je=java=page.locator('//a[text()="Java Expert"]')
    spmswh = page.locator('//a[contains(normalize-space(),"SpringBoot Microservices")]'
)

    Java_Technology=[java,adm,je,spmswh]
    for e in Java_Technology:
         cat.hover()
         jt.hover()
         e.click()
         page.wait_for_timeout(2000)
         page.go_back()
    eh= page.locator('//a[text()="Ethical Hacking"]')
    cs=page.locator('//a[text()="Cyber Security"]')
    ccnp=page.locator('//a[text()="CCNP"]')
    mcsa=page.locator('//a[text()="MCSA"]')
    vmware=page.locator('//a[text()="Vmware"]')
    Network_Security=[eh,cs,ccnp,mcsa,vmware]
    for c in Network_Security:
         cat.hover()
         ns.hover()
         c.click()
         page.wait_for_timeout(2000)
         page.go_back()
         
    cwds= page.locator('//a[contains(normalize-space(),"CWith Data Structure")]'
)
    ooda = page.locator(
    '//a[normalize-space()="Object Oriented DataStructure & Algorithms Training"]'
)

    net=page.locator('//a[text()=".NET 4 Months"]')
    netfs=page.locator('//a[text()=".NET Full Stack"]')
    r=page.locator('//a[text()="R Programming"]')
    Programming_Language=[cwds,ooda,net,netfs,r]
    for d in Programming_Language:
         cat.hover()
         pl.hover()
         d.click()
         page.wait_for_timeout(2000)
         page.go_back()
    autocad=page.locator('//a[text()="AUTOCAD"]')
    cnc=page.locator('//a[text()="CNC Programming"]')
    cad_training=[autocad,cnc]
    for d in cad_training:
         cat.hover()
         cad.hover()
         d.click()
         page.wait_for_timeout(2000)
         page.go_back()
    gd1=page.locator('(//a[text()="Graphic Designing"])[2])')
    uiux=page.locator('//a[text()="UI/UX Designing"]')
    Graphic_Designing=[gd1,uiux]
    for f in Graphic_Designing:
         cat.hover()
         gd.hover()
         f.click()
         page.wait_for_timeout(2000)
         page.go_back()

    


   

    

    


 