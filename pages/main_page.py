#Stepik_auto_test_FINAL_PROJ
#pages/main_page.py
#main_page.py

from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()


    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


#