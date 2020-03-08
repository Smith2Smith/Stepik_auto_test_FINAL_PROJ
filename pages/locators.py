#Stepik_auto_test_FINAL_PROJ
#pages/locators.py
#locators.py

from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FIELD_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FIELD_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_FIELD_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FIELD_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_FIELD_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")

#