from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class BarcoTest:
    def WarrantyTest(serialNumbers):
        chromeOptions = Options()
        chromeOptions.headless = True
        
        driver = webdriver.Chrome('./chromedriver', options=chromeOptions)

        driver.get("https://www.barco.com/en/clickshare/support/warranty-info")

        accept_botton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_botton.click()

        input_serial = driver.find_element(By.ID, "SerialNumber")
        input_serial.send_keys(serialNumbers)
        input_serial.send_keys(Keys.ENTER)

        time.sleep(3)

        try:
            warranty_result = driver.find_element(By.XPATH, "//dt[contains(text(), 'Description')]")
            return True
        except NoSuchElementException:
            return False