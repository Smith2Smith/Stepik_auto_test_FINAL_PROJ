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

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")  # кнопка добавить в корзину в карточке продукта
    MESSAGE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner")   # сообщение о добавленном в корзину продукте
    PRICE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert-info p strong")  # цена добавленного в корзину продукта в сообщении
    PRODUCT_NAME_IN_PRODUCT_CARD = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")       # название продукта в карточке продукта
    PRICE_IN_PRODUCT_CARD = (By.CSS_SELECTOR, ".product_main .price_color")        # цена продукта в карточке продукта

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".header .btn-group a.btn.btn-default")

class BasketPageLocators():
    FIRST_PRODUCT_LINK = (By.CSS_SELECTOR, ".basket_summary .basket-items:nth-child(6) .col-sm-4 h3 a")
    MESSAGE_TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")

#