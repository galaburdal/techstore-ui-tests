import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    BACKPACK = (By.XPATH, "//div[@class='inventory_item_name' and normalize-space()='Sauce Labs Backpack']")
    CHECKOUT = (By.ID, "checkout")

    @allure.step("Перевірити наявність Sauce Labs Backpack у кошику")
    def has_backpack(self):
        return self.wait.until(EC.visibility_of_element_located(self.BACKPACK)).is_displayed()

    @allure.step("Перейти до оформлення замовлення")
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT)
