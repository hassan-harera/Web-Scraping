from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

categories = [
    # "https://spinneys-egypt.com/en/categories/fresh-food?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/spinneys-products?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/food-cupboard?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/dairy-butter?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/electronics-appliances?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/home-garden?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/fashion-linen?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/baby?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/chilled-frozen?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/beverage?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/sweets-snacks?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/beauty-personal-care1?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/cleaning?locale=en&page=",
    # "https://spinneys-egypt.com/en/categories/hot-offers?locale=en&page=",
]

f = open("spinneys.json", "a", encoding="utf-8")


def getProducts(subCategoryLink, subCategoryName):
    for page in range(1, 20):
        driver.get(subCategoryLink + "?locale=en&page=" + str(page))
        driver.implicitly_wait(500)

        if "No items were found matching the selected" not in driver.page_source:
            productImages = driver.find_elements_by_xpath('//div[@class="inner"]/a/img')
            productPrices = driver.find_elements_by_xpath('//div[@class="product-price"]/span')
            print(len(productImages))

            for productIdx in range(0, len(productImages)):
                image = productImages[productIdx].get_attribute("src")
                name = productImages[productIdx].get_attribute("alt")
                price = productPrices[productIdx].text
                f.write(name + "," + price + "," + subCategoryName + "," + image + "\n")
                f.flush()
        else:
            break


for category in categories:
    driver.get(category)
    driver.implicitly_wait(1500)
    categoryName = driver.find_element_by_xpath(
        '//div[@class="row py-1 align-it text-capitalize"]/h1').text
    # getProducts(category, categoryName)

    subCategories = driver.find_elements_by_xpath(
        '//div[@class="row flex-wrap justify-content-start px-3 d-flex align-items-start text-capitalize"]/a')
    for idx in range(1, len(subCategories)):
        driver.get(category)
        driver.implicitly_wait(1500)
        subCategories = driver.find_elements_by_xpath(
            '//div[@class="row flex-wrap justify-content-start px-3 d-flex align-items-start text-capitalize"]/a')
        subCategoryName = subCategories[idx].text
        subCategoryLink = subCategories[idx].get_attribute("data-href")
        print(subCategoryLink)
        getProducts(subCategoryLink, subCategoryName)
driver.close()
