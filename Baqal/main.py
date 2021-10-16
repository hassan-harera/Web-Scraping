from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.minimize_window()

categories = [
    "https://albaqqal.com/product-category/%d8%a7%d9%84%d9%85%d8%b9%d9%84%d8%a8%d8%a7%d8%aa-%d9%88-%d9%85%d8%ac%d9%85%d8%af%d8%a7%d8%aa/page/"
]

fileWrite = open("baqal.json", "a", encoding="utf-8")
fileRead = open("baqal.json", "r", encoding="utf-8")

for category in categories:

    for page in range(1, 100):
        driver.get(category + str(page))

        if "الصفحة غير موجودة" not in driver.page_source:
            productLinks = driver.find_elements_by_xpath('//div[@class="product-element-top"]/a')
            print(len(productLinks))

            for product in productLinks:
                driver2 = webdriver.Chrome(ChromeDriverManager().install())
                driver2.maximize_window()
                driver2.minimize_window()
                driver2.get(product.get_attribute("href"))

                image = ""
                price = ""
                name = ""
                try:
                    WebDriverWait(driver2, 2, ignored_exceptions=True).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "woocommerce-product-gallery__image"))
                    )

                    price = driver2.find_element_by_xpath('//p[@class="price"]').text
                    image = driver2.find_element_by_xpath(
                        '//figure[@class="woocommerce-product-gallery__image"]/img').get_attribute("src")
                    name = driver2.find_element_by_xpath('//h1[@class="product_title entry-title"]').text

                    fileWrite.write(" " + name + "," + price + "," + image + "\n")
                    fileWrite.flush()
                    driver2.close()

                except :
                    fileWrite.write(" " + name + "," + price + "," + image + "\n")
                    fileWrite.flush()
                    driver2.close()

driver.close()
