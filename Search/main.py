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
driver.maximize_window()
time.sleep(30)

baseSearch = "https://www.google.com/search?q="
suffix = "&hl=en&gl=ar&tbm=isch&sxsrf=AOaemvLClN8FChmMeCCP3wv2fzlihR-05g%3A1632621606010&source=hp&biw=1920&bih=880&ei=JdRPYanWO8mblwT-047QDw&oq=&gs_lcp=CgNpbWcQARgAMgoIIxDvAxDqAhAnMgoIIxDvAxDqAhAnMgoIIxDvAxDqAhAnMgoIIxDvAxDqAhAnMgoIIxDvAxDqAhAnMgoIIxDvAxDqAhAnMgoIIxDvAxDqAhAnMgoIIxDvAxDqAhAnMgoIIxDvAxDqAhAnMgoIIxDvAxDqAhAnUABYAGCoOWgBcAB4AIABAIgBAJIBAJgBAKoBC2d3cy13aXotaW1nsAEK&sclient=img"

fileWrite = open("searchResult.json", "a", encoding="utf-8")
fileRead = open("searchResult.json", "r", encoding="utf-8")
#
products = pd.read_csv("products.csv")
products.drop(axis=1, index=2)

for product in range(0, len(products)):
    # driver.get(f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q=" + str(products.iloc[product, 1]))
    driver.get(f"https://www.bing.com/images/search?q=" + str(products.iloc[product, 1]))
    print(products.iloc[product, 1])

    pyperclip.copy(str(products.iloc[product, 1]))
    spam = pyperclip.paste()

    images = driver.find_elements_by_xpath('//div[@class="img_cont hoff"]/img')
    print(len(images))


    directory = str(product) + products.iloc[product, 1]
    path = os.path.join("C://Users//Harera//PycharmProjects//web scrape//Search//data//", directory)
    os.mkdir(path)

    for idx in range(0, 5):
        imageLink = images[idx].get_attribute("src")
        print(imageLink)

        try:
            if imageLink != None:
                src = str(imageLink)
                urllib.request.urlretrieve(src, os.path.join('/data/' + str(product) + str(products.iloc[product, 1]),
                                                             str(idx) + '.jpg'))
        except:
            pass

    fileWrite.write(str(products.iloc[product, 0]) + "," + str(products.iloc[product, 1]) + "," + imageLink)
    fileWrite.flush()

driver.close()
