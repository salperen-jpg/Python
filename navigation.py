from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path='C:\chromedriver'

driver=webdriver.Chrome(path)

driver.maximize_window()

driver.get('https://google.com.tr')


searchButton=driver.find_element_by_name('q')
searchButton.send_keys('hepsiburada' + Keys.RETURN)



link=driver.find_element_by_partial_link_text('Türkiye\'nin En Büyük Online Alışveriş Sitesi Hepsiburada.com')
link.click()

driver.implicitly_wait(5)

searchButton2=driver.find_element_by_class_name("desktopOldAutosuggestTheme-input")
searchButton2.send_keys('Iphone 11 pro max' + Keys.RETURN)

time.sleep(15)



driver.close()