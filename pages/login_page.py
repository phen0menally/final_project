from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import RegistrationPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "It is not login page"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Not Found Login Form"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Not Found Register Form"

    def register_new_user(self, email, password):
        self.browser.find_element(*RegistrationPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*RegistrationPageLocators.PASS1).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.PASS2).send_keys(password)
        self.browser.find_element(*RegistrationPageLocators.REG_BTN).click()


