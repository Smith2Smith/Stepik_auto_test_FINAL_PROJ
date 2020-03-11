#Stepik_auto_test_FINAL_PROJ
#Stepik_auto_test_FINAL_PROJ/test_product_page.py
#test_product_page.py

# ФАЙЛ С ТЕСТАМИ добавление в корзину со страницы товара

#Запуск :
#pytest -v -s --tb=line --language=en test_product_page.py

from .pages.product_page import ProductPage
import pytest

#link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    #page.solve_quiz_and_get_code()
    page.should_be_add_product_to_basket()
    page.should_be_correct_name_add_product_to_backet(page.product_name())
    page.should_be_correct_price_basket(page.product_price())
    #page.should_not_be_success_message()
    #page.should_be_success_message_disappeared()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message_disappeared()

#