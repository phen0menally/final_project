from selenium.webdriver.common.by import By
from .locators import CartPageLocators, ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_cart(self):
        cart = self.browser.find_element(*CartPageLocators.ADD_TO_CART)
        cart.click()

    def should_be_correct_product_name(self):
        book_name = self.browser.find_element(
            *CartPageLocators.BOOK_NAME)
        book_name_add = self.browser.find_element(
            *CartPageLocators.BOOK_NAME_AFTER_ADD)
        print(book_name.text)
        print(book_name_add.text)
        assert book_name.text == book_name_add.text, "Название книги на странице не совпадает"

    def should_be_correct_adding_product_price(self):
        message_basket_total = self.browser.find_element(
            *CartPageLocators.CART_PRICE)
        product_price = self.browser.find_element(
            *CartPageLocators.BOOK_PRICE)
        print(product_price.text)
        print(message_basket_total.text)
        assert product_price.text == message_basket_total.text, "Цена книги не совпадает с стоимостью корзины"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
