from PagesObjects.LoginPage import LoginPage
from Data.account import login_data

class TestLogin:

    def test_home_page_title(self, setup):
        self.driver = setup
        act_title = self.driver.title
        self.driver.close()

        assert act_title == "Swag Labs"

    def test_login(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.set_username(login_data["username"])
        self.lp.set_password(login_data["password"])
        self.lp.click_login()
        act_url = self.driver.current_url
        self.driver.close()

        assert act_url == "https://www.saucedemo.com/inventory.html"