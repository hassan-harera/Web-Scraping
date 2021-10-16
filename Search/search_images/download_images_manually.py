import requests
from selenium import webdriver
import os
import time
import pandas as pd
import pyperclip
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager

products = pd.read_csv("../products.csv")
start = 130712
driver = webdriver.Chrome(ChromeDriverManager().install())
for product in range(294, len(products)):
    product = (products.iloc[product, 1])
    search_URL = "https://www.google.com/search?q= " + product + "&source=lnms&tbm=isch"
    driver.get(search_URL)

    pyperclip.copy(str(start))
    start += 1
    time.sleep(22)