import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Відкрити сторінку входу")
    def open(self):
        self.open_url(self.URL)
        return self

    @allure.step("Ввести облікові дані користувача {username}")
    def enter_credentials(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)

    @allure.step("Натиснути кнопку «Увійти»")
    def submit_login(self):
        self.click(self.LOGIN_BUTTON)

    @allure.step("Увійти під користувачем {username}")
    def login_as(self, username, password):
        self.enter_credentials(username, password)
        self.submit_login()
