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
import pyautogui

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

products = pd.read_csv("products.csv")
count = 130338

time.sleep(10)
for product in range(52, len(products)):
    # https://www.google.com/search?q=
    driver.get(
        f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q=" + str(products.iloc[product, 1]))
    # driver.get(f"https://www.google.com/search?q=" + str(products.iloc[product, 1]) +
    #            "&tbm=isch&hl=ar&tbs=isz:m&sa=X&ved=0CAMQpwVqFwoTCMDVhuO6nfMCFQAAAAAdAAAAABAN&biw=1903&bih=937#imgrc=6irsyUWCRbsH2M")
    print(products.iloc[product, 1])
    time.sleep(1)
    driver.execute_script('scrollBy("+ str(value) +",+300);')

    images = driver.find_elements_by_xpath('//div[@class="NZWO1b"]/img')
    print(len(images))
    pyperclip.copy(str(count))
    count += 1

    for idx in range(0, 1):
        imageLink = images[idx].get_attribute("src")
        driver2 = webdriver.Chrome(ChromeDriverManager().install())
        driver2.get(imageLink)

        pyautogui.press('esc')

        time.sleep(1)

        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)

        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')

        time.sleep(2)
        driver2.close()

driver.close()
