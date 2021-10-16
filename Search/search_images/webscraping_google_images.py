import requests
from selenium import webdriver
import os
import time
import pandas as pd
import pyperclip
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager

folder_name = 'images'
if not os.path.isdir(folder_name):
    os.makedirs(folder_name)


def download_image(url, folder_name, num):
    reponse = requests.get(url)
    if reponse.status_code == 200:
        with open(os.path.join(folder_name, str(num) + ".jpg"), 'wb') as file:
            file.write(reponse.content)


products = pd.read_csv("../products.csv")
start = 130279
fileWrite = open("carfour.json", "a", encoding="utf-8")


def load_image(link, start):
    driver2 = webdriver.Chrome(ChromeDriverManager().install())
    driver2.get(link)

    pyperclip.copy(str(start))
    time.sleep(1)

    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    pyautogui.press('tab')
    pyautogui.press('enter')

    driver2.close()


driver = webdriver.Chrome(ChromeDriverManager().install())
for product in range(279, 280): #len(products)):
    search_query = (products.iloc[product, 1])
    search_URL = "https://www.google.com/search?q= " + search_query + "&source=lnms&tbm=isch"
    driver.get(search_URL)

    # for scroll in range(1, 10):
    #     driver.execute_script("window.scrollTo(0, window.scrollY + " + str(scroll * 100) + ");")
    #     time.sleep(1)
    # pyperclip.copy(str(start))
    # start += 1
    # time.sleep(20)
    for i in range(1, 2):
        # xPath = """//*[@id="islrg"]/div[1]/div[%s]""" % (i)
        # driver.find_element_by_xpath(xPath).click()
        images = driver.find_elements_by_xpath('//div[@class="bRMDJf islir"]/img')
        image = images[i].get_attribute("src")
        if image != None:
            load_image(image, start)
            start += 1
            # driver.find_element_by_xpath(xPath).click()
            # productLinks = driver.find_elements_by_xpath('//div[@class="qdnLaf isv-id"]/div[@class="v4dQwb"]/a/img')
            # productLinks = driver.find_elements_by_tag_name("img")
            # driver.execute_script("window.scrollTo(0, window.scrollY + " + str(100) + ");")
            # print(len(productLinks))

            # for product in productLinks:
            #     image = product.get_attribute("src")
            #     if ("data:image/jpeg" not in image and "encrypted" not in image):
            #         name = product.get_attribute('alt')
            #         load_image(image, start)
            #         fileWrite.write(name + "," + image + "\n")
            #         fileWrite.flush()

# driver.close()

# images = driver.find_elements_by_tag_name("img")
#
# for i in range(1, 11):
#     xPath = """//*[@id="islrg"]/div[1]/div[%s]""" % (i)
#     driver.find_element_by_xpath(xPath).click()
#     link = images[i].get_attribute("src")
#     name = images[i].get_attribute("alt")
#     load_image(link, start)
#     fileWrite.write(str(link) + "\n")
#     fileWrite.flush()
#     start += 1

# for i in range(1, 10):

#
# image = driver.find_element_by_xpath('//div[@class="v4dQwb"]/a/img')
# link = image.get_attribute("src")
# name = image.get_attribute('alt')
# fileWrite.write(name + "," + link + "\n")
# fileWrite.flush()

# previewImageElement = driver.find_element_by_xpath(previewImageXPath)
# previewImageURL = previewImageElement.get_attribute("src")
# if (previewImageURL == None):
#     continue
#
# timeStarted = time.time()
# while True:
#     currentTime = time.time()
#     if currentTime - timeStarted > 2:
#         print("Timeout! Will download a lower resolution image and move onto the next one")
#         break
#
#     imageElement = driver.find_element_by_xpath(
#         """//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img""")
#     imageURL = imageElement.get_attribute('src')
#
#     if imageURL != previewImageURL:
#         break
#
#     else:
#         currentTime = time.time()
#         if currentTime - timeStarted > 3:
#             print("Timeout! Will download a lower resolution image and move onto the next one")
#             break
#
#     try:
#         download_image(imageURL, folder_name, start)
#         start += 1
#         print("Downloaded element %s out of %s total. URL: %s" % (i, len_containers + 1, imageURL))
#     except:
#         print("Couldn't download an image %s, continuing downloading the next one" % (i))
#
# driver.close()
