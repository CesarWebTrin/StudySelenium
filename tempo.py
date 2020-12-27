import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://g1.globo.com/previsao-do-tempo/sp/sao-paulo.ghtml")

soup = BeautifulSoup(page.content, 'html.parser')


days = soup.find(class_ = "forecast-next-days__content")
today = soup.find(class_="columns medium-24 large-12 medium-centered")

nome = [today.find(class_="forecast-header__date").get_text()]

tempmax = today.find(class_= "forecast-today__temperature forecast- today__temperature--max").get_text()
tempmin = today.find(class_="forecast-today__temperature forecast- today__temperature--min").get_text()

tempmax = tempmax[0:4]
tempmin = tempmin[0:4]
temp2 = [tempmax]
temp2 +=[tempmin]




nome += [n.get_text() for n in days.select(".forecast-table .forecast-next- days__item-label")]
temp2 += [d.get_text() for d in days.select(".forecast-table .forecast-next-days__item-value")]




temmax = temp2[0:18:2]
temmin = temp2[1:18:2]

tempo = pd.DataFrame({
   "nome": nome,
   "temperatura_max":temmax,
    "temperatura_min":temmin
   })



tempo.to_excel(r"C:\Users\nlsouza\Desktop\python5.xlsx")