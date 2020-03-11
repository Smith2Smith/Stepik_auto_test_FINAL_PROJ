#Stepik_auto_test_FINAL_PROJ
#Stepik_auto_test_FINAL_PROJ/pages/product_page.py
#product_page.py

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        # добавить товар в корзину
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()

    def should_be_add_product_to_basket(self):
        # проверка: сообщение о том, что товар добавлен в корзину
        assert "has been added to your basket" in self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET).text, "Message about added to basket is incorrect"

    def should_be_correct_name_add_product_to_backet(self, product_name):
        # проверка: название товара в сообщении, совпадает с тем товаром, который добавили
        #assert product_name in self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET).text, "Product name added to cart is incorrect"
        assert product_name + " has been added to your basket." == self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET).text, "Product name added to cart is incorrect"

    def should_be_correct_price_basket(self, product_price):
        # проверка: стоимость корзины совпадает с ценой товара
        assert product_price == self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET).text, "Product price added to cart is incorrect"

    def product_name(self):
        # название товара в карточке товара
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_PRODUCT_CARD).text
        return product_name

    def product_price(self):
        # цена товара в карточке товара
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_PRODUCT_CARD).text
        return product_price

    def should_not_be_success_message(self):
        # проверка: не должно быть успешного сообщения
        # SUCCESS_MESSAGE заменен на MESSAGE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET), \
           "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        # проверка: успешное сообщение должно исчезнуть
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_HAS_BEEN_ADDED_TO_BASKET), \
            "Success message is not disappeared, but should not be"

#