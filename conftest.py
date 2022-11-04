import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

@pytest.fixture()
def initiate_driver():
    driver.get("http://automationpractice.com/index.php")
    driver.maximize_window()
    yield driver
    driver.quit()
