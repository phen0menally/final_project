from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class CartPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    BOOK_NAME = (By.CSS_SELECTOR, '[class="active"]')
    BOOK_NAME_AFTER_ADD = (By.CSS_SELECTOR, '.alertinner strong')
    BOOK_PRICE = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] > [class="price_color"]')
    CART_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')

