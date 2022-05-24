from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox

driver = Firefox('./')
driver.get('https://quotes.toscrape.com/login')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'username')))
driver.get('https://quotes.toscrape.com/scroll')

driver.quit()

