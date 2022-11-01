import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from Config.Configdata import dress1, p_dress
from Pages.HomePageLocators import *
from Pages.OrderLocators import *
from Utilities.CommonPageUtilities import *
from conftest import driver
from selenium.webdriver import ActionChains


class HomePageFunctions:
    def search_bar(self):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, search_field)))
        driver.find_element(By.CSS_SELECTOR, search_field).send_keys(dress1)
        driver.find_element(by=By.CSS_SELECTOR, value=search_box).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,p_dress )))
        # time.sleep(5)
        driver.find_element(By.XPATH, p_dress).click()

    def add_to_cart(self):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, add_to_cart)))
        cart = driver.find_element(By.XPATH, add_to_cart)
        actions = ActionChains(driver)
        actions.move_to_element(cart).perform()
        cart.click()

    def proceed_to_checkout(self):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, proceed_to_checkout)))
        # time.sleep(5)
        checkout = driver.find_element(By.CSS_SELECTOR, proceed_to_checkout)
        checkout.click()
        # driver.find_element(By.CSS_SELECTOR, proceed_to_checkout).click()

    def proceed_to_checkout_in_summary(self):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, proceed_to_checkout_in_summary)))
        checkout_in_summary = driver.find_element(By.CSS_SELECTOR, proceed_to_checkout_in_summary)
        actions = ActionChains(driver)
        actions.move_to_element(checkout_in_summary).perform()
        driver.find_element(By.CSS_SELECTOR, proceed_to_checkout_in_summary).click()

    def proceed_to_checkout_in_address(self):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, proceed_to_checkout_in_address)))
        checkout_in_address = driver.find_element(By.CSS_SELECTOR, proceed_to_checkout_in_address)
        actions = ActionChains(driver)
        actions.move_to_element(checkout_in_address).perform()
        driver.find_element(By.CSS_SELECTOR, proceed_to_checkout_in_address).click()

    def proceed_to_checkout_in_shipping(self):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, proceed_to_checkout_in_shipping)))
        checkout_in_shipping = driver.find_element(By.CSS_SELECTOR, proceed_to_checkout_in_shipping)
        actions = ActionChains(driver)
        actions.move_to_element(checkout_in_shipping).perform()
        # driver.find_element(By.CSS_SELECTOR, teams_of_service).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, teams_of_service)))
        # time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, teams_of_service).click()
        driver.find_element(By.CSS_SELECTOR, proceed_to_checkout_in_shipping).click()

    def proceed_to_checkout_in_payment(self):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, payment_via_cheque)))
        checkout_in_payment = driver.find_element(By.CSS_SELECTOR, payment_via_cheque)
        actions = ActionChains(driver)
        actions.move_to_element(checkout_in_payment).perform()
        driver.find_element(By.CSS_SELECTOR, payment_via_cheque).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, confirm_my_order)))
        driver.find_element(By.CSS_SELECTOR, confirm_my_order).click()

    def final_order(self):
        self.search_bar()
        self.add_to_cart()
        self.proceed_to_checkout()
        self.proceed_to_checkout_in_summary()
        self.proceed_to_checkout_in_address()
        self.proceed_to_checkout_in_shipping()
        self.proceed_to_checkout_in_payment()

    def view_cart(self):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, view_cart)))
        Util().click_on(view_cart)

    def click_sign_out(self):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, sign_out)))
        Util().click_on(sign_out)

    def click_contact_us(self):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, contact_us)))
        Util().click_on(contact_us)
