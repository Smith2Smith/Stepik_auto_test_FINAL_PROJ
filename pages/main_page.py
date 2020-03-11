#Stepik_auto_test_FINAL_PROJ
#pages/main_page.py
#main_page.py

from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

#