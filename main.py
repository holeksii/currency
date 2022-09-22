from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = '.\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://www.google.com')
print(driver.title)
