from playwright.sync_api import sync_playwright # importação base do modo sync

with sync_playwright() as p: #inicialização do programa utilizando playwright sync
    browser = p.chromium.launch(headless=False) # abrir o launcher e desativar o modo headless para mostrar a tela (pode executar sem)
    page = browser.new_page() # criar uma nova pagina 
    page.goto("https://www.youtube.com/watch?v=FK_5SQPq6nY&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A") # enviar o url
    page.wait_for_timeout(3000) # pega em milissegundos (3s)
    page.screenshot(path="demo.png") # printa
    browser.close() # fecha