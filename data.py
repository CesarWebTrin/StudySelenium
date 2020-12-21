from logging import exception
import time
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

url = "file:///D:/CESAR/PROGRAMACAO/Python/study/data/index.html"

driver = webdriver.Chrome(executable_path=r'files\\chromedriver.exe')
driver.get(url)
try: 
    driver.find_element_by_xpath('html//body//input').click()
    driver.find_element_by_xpath("//select[@id='itens']//option[4]").click()
    time.sleep(3)
except UnexpectedAlertPresentException:
    alert = driver.switch_to_alert()
    alert.accept()
    driver.find_element_by_xpath("//select[@id='itens']//option[4]").click()
    driver.find_element_by_xpath('html//body//input').click()



