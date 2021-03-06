#Stepik_auto_test_FINAL_PROJ
#pages/login_page.py
#login_page.py

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FIELD_EMAIL)
        field.clear()
        field.send_keys(email)
        field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FIELD_PASSWORD1)
        field.clear()
        field.send_keys(password)
        field = self.browser.find_element(*LoginPageLocators.REGISTRATION_FIELD_PASSWORD2)
        field.clear()
        field.send_keys(password)
        link = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_REGISTER)
        link.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # проверить текущий url браузера , что в нем есть подстрока 'login'
        assert "login" in self.browser.current_url, "In current URL not found substring 'login'"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

#