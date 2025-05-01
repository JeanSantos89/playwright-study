# Playwright 

Este repositório contém exemplos e instruções para automações com **Playwright**, utilizando modo *headless* (executa sem exibir o navegador) e suporte para seletores **CSS/XPath**.

---

## Tipos de Execução

- `sync`: Ideal para automações simples.  
- `async`: Recomendado para automações mais avançadas ou com paralelismo.

---

## CSS Seletores

- #id
- .class
- tagname[attribute="value"]

---

## XPATH
- //tagname[@attribute="value"]                   --> Relative XPath
- //tagname[text()="Texto exato"]                --> Seleciona por texto
- //tagname[contains(@attribute, "valor")]       --> Contém valor parcial
- //tagname[contains(text(), "parte do texto")]  --> Contém parte do texto
- //tagname[starts-with(@id, "inicio")]          --> Começa com
- //tagname[ends-with(@id, "fim")]               --> Termina com

---

## Dropdown
- dropdown = page.query_selector('//select[@id="Skills"]')
- dropdown.select_option(label='Adobe Photoshop')
- page.select_option('//select[@id="Skills"]', label='Adobe Photoshop')

---

## Radio Button
- //tagname[@attribute="value"]

---

## Check Box
- //tagname[@attribute="value"]




