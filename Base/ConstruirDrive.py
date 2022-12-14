from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Utils.urls import urls

class Base:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(urls["saucedemo"])
        self.driver.maximize_window()

    def get_driver(self):
        return self.driver