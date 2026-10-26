
import allure
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.feature("Оформлення замовлення")
@allure.story("Успішна покупка")
@allure.title("Користувач купує Sauce Labs Backpack")
def test_buying_process(driver):
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Відкрити Swag Labs і виконати вхід"):
        login.open()
        login.login_as("standard_user", "secret_sauce")
        assert inventory.is_opened(), "Каталог товарів не відкрився"

    inventory.add_backpack_to_cart()
    inventory.open_cart()
    assert cart.has_backpack(), "Товар відсутній у кошику"

    cart.proceed_to_checkout()
    print("URL після Checkout:", driver.current_url)
    print("Заголовок сторінки:", driver.title)
    print("Текст сторінки:", driver.execute_script("return document.body.innerText"))


    checkout.fill_shipping_details("Test", "User", "79000")
    checkout.continue_checkout()
    checkout.finish_order()

    assert checkout.is_order_complete(), (
        "Не знайдено повідомлення про успішне замовлення"
    )
