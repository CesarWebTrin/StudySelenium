import pandas as pd
import time 
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

url = "file:///D:/CESAR/PROGRAMACAO/Python/study/Pandaslimit/index.html"


driver = webdriver.Chrome(executable_path=r'files\\chromedriver.exe')
driver.get(url)
for i in range(1, 101, 1):
    driver.find_element_by_xpath("html//body//input").click()

tabela = driver.find_element_by_id('minhaTabela')

html_content = tabela.get_attribute('outerHTML') 
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

df_full = pd.read_html(str(table))
print(df_full)

time.sleep(6)
