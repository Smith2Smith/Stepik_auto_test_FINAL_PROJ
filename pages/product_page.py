#Stepik_auto_test_FINAL_PROJ
#Stepik_auto_test_FINAL_PROJ/pages/product_page.py
#product_page.py

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()

#