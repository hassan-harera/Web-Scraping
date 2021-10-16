from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

categories = [
   "https://www.carrefouregypt.com/mafegy/ar/c/FEGY1760000?currentPage=3&filter=&nextPageOffset=0&pageSize=400&sortBy=relevance"
]

fileWrite = open("carfour.json", "a", encoding="utf-8")
fileRead = open("carfour.json", "r", encoding="utf-8")

for category in categories:
    driver.maximize_window()
    driver.get(category)

    xPath = """//div[@class="css-1hbp62g"]/button"""
    driver.find_element_by_xpath(xPath).click()

    for scroll in range(1, 50):
        driver.execute_script("window.scrollTo(0, window.scrollY + " + str(scroll * 60) + ");")
        time.sleep(0.5)

    if "No items were found matching the selected" not in driver.page_source:
        productLinks = driver.find_elements_by_xpath('//div[@class="css-1r8exng"]/a/img')
        print(len(productLinks))

        for product in productLinks:
            image = product.get_attribute("src")
            name = product.get_attribute('alt')

            fileWrite.write(name + "," + image + "\n")
            fileWrite.flush()

driver.close()
