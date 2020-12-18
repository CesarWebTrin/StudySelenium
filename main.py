import time
from selenium import webdriver

url = "https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/"

driver = webdriver.Chrome(executable_path=r'files\\chromedriver.exe')
driver.get(url)
time.sleep(6)

tabela = driver.find_element_by_xpath("//div//*[@id='mod-603-standings-round-robin']//div[1]//div[1]//table//tbody")

linhas = len(tabela.find_elements_by_tag_name("tr"))

for i in range(1,linhas, 1):
    print(i)
    path = r"//div//*[@id='mod-603-standings-round-robin']//div[1]//div[1]//table//tbody//tr[{}]//td[3]//a".format(i)
    print(path)
    driver.find_element_by_xpath(path).click()
    time.sleep(10)
    driver.get(url)
