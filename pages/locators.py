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


class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:nth-child(1)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET = (By.CSS_SELECTOR, '.btn-group')
    FILL_BASKET = (By.CSS_SELECTOR, '[class="col-sm-6 h3"]')
    BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner p')


class RegistrationPageLocators():
    EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')

