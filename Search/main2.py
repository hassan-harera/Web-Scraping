from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
import requests
import urllib
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import shutil
import pyperclip

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.google.com/')
search = driver.find_element_by_name('q')

products = pd.read_csv("products.csv")
products.drop(axis=1, index=2)

for product in range(0, len(products)):
    print(products.iloc[product, 1])
    search.send_keys(products.iloc[product, 1], Keys.ENTER)

    time.sleep(2)
    elem = driver.find_element_by_link_text('Images')
    elem.get_attribute('href')
    elem.click()

    value = 0
    for i in range(20):
        driver.execute_script('scrollBy("+ str(value) +",+100);')
        value += 100
        time.sleep(4)

driver.close()
