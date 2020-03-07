#Stepik_auto_test_FINAL_PROJ
#pages/login_page.py
#login_page.py

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # проверить текущий url браузера , что в нем есть подстрока 'login'
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        # #login_form
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # #register_form
        assert True

#