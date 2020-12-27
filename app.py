import time
import pandas as pd
from pandas.core.accessor import register_dataframe_accessor
from pandas.io.sql import table_exists
from selenium import webdriver
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas

url = "https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/"

driver = webdriver.Chrome(executable_path=r'files\\chromedriver.exe')
driver.get(url)
time.sleep(6)
driver.execute_script('window.scrollBy(0, 500)')


tabela = driver.find_element_by_xpath("//div//*[@id='mod-603-standings-round-robin']//div[1]//div[1]//table")

html_content = tabela.get_attribute('outerHTML') 
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table))[0]

df = pd.DataFrame(data = df_full)
print(df)

raw_data = {'Autor': ['Cesar'],
'Empresa': ['Itaú'], 'Ação': ['ITB']}

df_add = pd.DataFrame(data = raw_data, columns=['Autor', 'Empresa', 'Ação']   
)


linhas = len(df)

for i in range(1, linhas,1):

    df_concat = pd.concat([df_add, df_add ]* i) 
print(df_concat)

df_planilha = df_concat.join(df)

df_planilha = pd.concat([df_planilha, df_planilha])

raw_data = {'Autor': ['Cristina'],
'Empresa': ['Bradesco'], 'Ação': ['BDC']}

df_add = pd.DataFrame(data = raw_data, columns=['Autor', 'Empresa', 'Ação'])

for a in range(1, linhas,1):

    df_concat = pd.concat([df_add, df_add ]* a) 
print(df_concat)

df_planilha = pd.concat([df_planilha, df_concat.join(df)])


df_planilha.to_excel("saida.xlsx", index=False)




""" 
pdf = canvas.Canvas("ARQUIVO.pdf")
pdf.drawString(0, 500, str(df_full))
pdf.save() """

""" linhas = len(tabela.find_elements_by_tag_name("tr"))

for i in range(1,linhas, 1):
    print(i)
    path = r"//div//*[@id='mod-603-standings-round-robin']//div[1]//div[1]//table//tbody//tr[{}]//td[3]//a".format(i)
    print(path)
    driver.find_element_by_xpath(path).click()
    time.sleep(10)
    driver.get(url)
 """

