from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FILL_BASKET), 'Корзина не пустая'

    def should_be_message_basket(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_TEXT), 'Корзина не пустая/Cообщение отсутствует'


