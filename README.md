Playwright 

- Executa em modo headless de forma automática. Então, ao executar a automação, ele não irá mostrar nada, mas estará executando.

    * Não mostra # browser = p.chromium.launch()
    * Mostra # browser = p.chromium.launch(headless=False)
    * sync: automações simples
    * async: automações avançadas

* CSS SELECTOR - id #, class . - tagname[attribute = "value"] -
* xpath - Relative xpath -  //tagname[@attributename="value"] -
* text - '//tagname[text()=""'] - clicar pelo texto
* contains - //tagname[contains()@attribute,"value"] -
    text - //tagname[contains(text(),"metade do texto")] - Procura qualquer coisa que contenha o texto escrito
    starts-with - //tagname[starts-with(@id, 'prasanth')]
    ends-with - //tagname[ends-with(@id, ' 1345')]
**

- Dropdown (clica e aparece uma lista)
    page.query_selector('//select[@id="Skills"]')
    variavel.select_option(label='Adobe Photoshop')
                        ou
    page..select_option('//select[@id="Skills"]', label='Adobe Photoshop')
                    