from playwright.sync_api import sync_playwright

with sync_playwright() as p: 
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page() 
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # enviar o url

# CSS SELECTOR - id #, class ., attribute tagname[attribute = "value"]
    # id: 
    login = page.wait_for_selector('input[name="username"]') 
    login.type('Admin')
    senha = page.wait_for_selector('input[type="password"]') 
    senha.type('admin123') 

    botaologin = page.wait_for_selector('button[type="submit"]') 
    botaologin.click()
    
    page.wait_for_timeout(3000) 
    browser.close() 


