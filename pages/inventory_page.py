import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    BACKPACK_ADD = (By.ID, "add-to-cart-sauce-labs-backpack")

    @allure.step("Перевірити відкриття каталогу")
    def is_opened(self):
        self.wait.until(EC.url_contains("inventory.html"))
        return self.get_text(self.PAGE_TITLE) == "Products"

    @allure.step("Додати Sauce Labs Backpack до кошика")
    def add_backpack_to_cart(self):
        self.click(self.BACKPACK_ADD)

    @allure.step("Відкрити кошик")
    def open_cart(self):
        self.click(self.CART_LINK)

    @allure.step("Відсортувати товари за назвою від A до Z")
    def sort_by_name_ascending(self):
        Select(self.find(self.SORT_SELECT)).select_by_value("az")
