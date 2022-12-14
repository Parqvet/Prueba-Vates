from selenium.webdriver.common.by import By
from Utils.login_page_locators import login_page

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, login_page["textbox_username"]).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, login_page["textbox_password"]).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, login_page["button_login"]).click()