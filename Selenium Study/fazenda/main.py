import time
from selenium import webdriver

url = 'https://afazenda.r7.com/a-fazenda-12/votacao'
driver = webdriver.Chrome(executable_path=r'files\\chromedriver.exe')
    
driver.get(url)
time.sleep(5)
driver.find_element_by_xpath('//div[@id="box_5f9b28d14b495515e3000035"]//div//div//div//div//section//div[2]//figure[3]//button').click()

driver.find_element_by_xpath("//html//body//div[7]//div[1]//div//div//div//div[1]//ul//li[2]//*[@class='card-selectable']")



if len(driver.find_elements_by_xpath("html//body//div[7]//div[1]//div//div//div//div[1]//ul//li[1][@class='card-selectable']")) > 0:
    driver.find_element_by_id('759').click()
else: 
    pass

driver.find_element_by_id('760').click()
driver.find_element_by_xpath("//div[@class='card-selectable-action']//button").click()
time.sleep(4)