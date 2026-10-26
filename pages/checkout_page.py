import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    @allure.step("Заповнити дані доставки")
    def fill_shipping_details(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.POSTAL_CODE, postal_code)

    @allure.step("Продовжити оформлення замовлення")
    def continue_checkout(self):
        self.click(self.CONTINUE)

    @allure.step("Підтвердити замовлення")
    def finish_order(self):
        self.click(self.FINISH)

    @allure.step("Перевірити повідомлення про успішне замовлення")
    def is_order_complete(self):
        self.wait.until(EC.visibility_of_element_located(self.COMPLETE_HEADER))
        return self.get_text(self.COMPLETE_HEADER) == "Thank you for your order!"
