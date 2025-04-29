from playwright.sync_api import sync_playwright

with sync_playwright() as p: 
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page() 
    page.goto("") # enviar o url

# CSS SELECTOR - id #, class ., attribute tagname[attribute = "value"]
    # id: 
    caixaDeTexto = page.wait_for_selector('#email') # espera o id email aparecer na pagina
    caixaDeTexto.type('emailteste@gmail.com') # digita no txt box
    
    botaologin = page.wait_for_selector("#botao") # espera o id do botao aparecer na pagina
    botaologin.click() # clicar no botao
    
    page.wait_for_timeout(3000) 
    browser.close() 


