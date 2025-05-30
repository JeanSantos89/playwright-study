from playwright.sync_api import sync_playwright

with sync_playwright() as p: 
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page() 
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login') # enviar o url

# xpath - Relative xpath
# Using attribute - //tagname[@attributename="value"] 
    login = page.wait_for_selector('//input[@name="username"]') # pesquisa isso e vê se é 1 / 1
    login.type('Admin')
    senha = page.wait_for_selector('//input[@type="password"]') 
    senha.type('admin123') 
    
# text - '//tagname[text()=""'] pegar o texto do campo
    page.wait_for_selector('//p[text()="Forgot your password? "]').click()

# contains
# attributes - //tagname[contains()@attribute,"value"] - se conter algo
    page.wait_for_selector('//input[contains()@placeholder, "Username"]').click()
    page.wait_for_timeout(3000) 
    browser.close() 


