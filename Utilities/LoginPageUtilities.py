from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.LoginPageLocators import *
from Pages.HomePageLocators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import *


class LoginPageFunctions:

    def sign_in_button(self):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, sign_in)))
        driver.find_element(by=By.CSS_SELECTOR, value=sign_in).click()

    def fill_username(self, email):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, email_field)))
        driver.find_element(by=By.CSS_SELECTOR, value=email_field).send_keys(email)

    def fill_password(self, passwd):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, password)))
        driver.find_element(by=By.CSS_SELECTOR, value=password).send_keys(passwd)

    def perform_login(self, email, passwd):
        self.fill_username(email)
        self.fill_password(passwd)
        driver.find_element(by=By.CSS_SELECTOR, value=sign_in_button).click()
