from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

# entrar google
navegador = webdriver.Chrome()

navegador.get('https://www.google.com/')

# cotação dolar
pesquisa = navegador.find_element(
'xpath',
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

pesquisa.send_keys('cotação dolar')
pesquisa.send_keys(Keys.ENTER)

dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(dolar)

# cotação euro
navegador.get('https://www.google.com/')

pesquisa = navegador.find_element(
'xpath',
'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

pesquisa.send_keys('cotação euro')
pesquisa.send_keys(Keys.ENTER)

euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(euro)

# cotação ouro
navegador.get('https://www.melhorcambio.com/ouro-hoje')

ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value')

ouro =  ouro.replace(',', '.')

print(ouro)

# importar database

tabela = pd.read_excel(r'C:\Users\Thigas\OneDrive\Documentos\Aula 3\Produtos.xlsx')
print(tabela)

# recalcular
tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(dolar)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(euro)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(ouro)

tabela['Preço de Compra'] = tabela['Cotação'] * tabela['Preço Original']
tabela['Preço de Venda'] = tabela['Preço de Compra'] * tabela['Margem']

# exportar a database 
tabela.to_excel("Produtos novo.xlsx", index=False)