from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.pickaboo.com/product/television/'
driver.get(url)

for i in range(1, 7):
    next_button = driver.find_element('xpath', '//button[@aria-label="Go to next page"]')
    product = 1
    while product <=20:
        name = driver.find_element('xpath', f'(//p[@class="product-title"])[{product}]').text
        price = driver.find_element('xpath', f'(//p[@class="product-price"])[{product}]/span').text
        try:
            previous_price = driver.find_element('xpath', f'(//p[@class="product-price"]){[product]}/s').text
        except:
            previous_price = None
        
        
        print(product)
        print(name)
        print(price)
        print(previous_price)
        product += 1
    time.sleep(5)
    next_button.click()
