from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import *


class Util:
    def find(self, element):
        if element.startswith('//'):
            found_element = driver.find_element(By.XPATH, element)
        else:
            found_element = driver.find_element(By.CSS_SELECTOR, element)
        return found_element

    def click_on(self, element):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))
        driver.find_element(by=By.CSS_SELECTOR, value=element).click()
