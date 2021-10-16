from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())

f = open("gym.json", "a")
driver.get("https://www.pinterest.com/pin/91479436171084790/")
myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'XiG zI7 iyn Hsu')))
images = driver.find_elements_by_xpath('//div[@class="XiG zI7 iyn Hsu"]/img')
for image in images:
    link = image.get_attribute("srcset")
    f.write(link + "\n")
    f.flush()

driver.close()
