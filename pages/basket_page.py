#Stepik_auto_test_FINAL_PROJ/pages/basket_page.py
#pages/basket_page.py
#basket_page.py

from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FIRST_PRODUCT_LINK), "Product in basket, but should not be"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_TEXT_EMPTY_BASKET), "Message text about empty basket is not presented"

