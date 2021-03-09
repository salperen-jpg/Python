from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path='C:\chromedriver'

driver=webdriver.Chrome(path)
driver.get('https://google.com.tr')

search_Box=driver.find_element_by_name('q')

search_Box.send_keys('corona'+ Keys.RETURN)


try:
    content= WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'kp-wp-tab-overview'))
    )
    
    
except:
    driver.quit()




headers=content.find_elements_by_tag_name('h3')
for header in headers:
    print(header.text)



driver.quit()
