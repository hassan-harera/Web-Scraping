from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())

f = open("fitnessprogramer.json", "a")

for i in range(1, 2, 1):
    driver.get("https://fitnessprogramer.com/exercise-primary-muscle/neck/page/" + str(i))
    if "Page not Found" not in driver.page_source:
        images = driver.find_elements_by_xpath('//div[@class="thumbnails"]/img')
        for image in images:
            link = image.get_attribute("src")
            f.write(link + "\n")
            f.flush()

    else:
        driver.close()
driver.close()
