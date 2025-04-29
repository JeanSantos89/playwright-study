from playwright.sync_api import sync_playwright

with sync_playwright() as p: 
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page() 
    page.goto('https://demo.automationtesting.in/Register.html')

    # selecionar dropdown
    select_dropdown = page.query_selector('//select[@id="Skills"]')
    select_dropdown.select_option(label='Adobe Photoshop')

    page.wait_for_timeout(3000) 
    browser.close() 


