#Stepik_auto_test_FINAL_PROJ
#Stepik_auto_test_FINAL_PROJ/test_product_page.py
#test_product_page.py

# ФАЙЛ С ТЕСТАМИ страницы товара

#Запуск :
#pytest -v -s --tb=line --language=en test_product_page.py
#pytest -m test1 -v -s --tb=line --language=en test_product_page.py
#pytest -m add_to_basket -v -s --tb=line --language=en test_product_page.py

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

#link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        # зарегистрировать нового пользователя
        email = "Aa" + str(time.time()) + "@test.ru"
        password = "Aa" + str(time.time())
        page.register_new_user(email, password)
        # проверить, что пользователь залогинен
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        #page.solve_quiz_and_get_code()
        page.should_be_add_product_to_basket()
        page.should_be_correct_name_add_product_to_backet(page.product_name())
        page.should_be_correct_price_basket(page.product_price())


#@pytest.mark.test1
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_product_to_basket()
    page.should_be_correct_name_add_product_to_backet(page.product_name())
    page.should_be_correct_price_basket(page.product_price())

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_success_message_disappeared()

#@pytest.mark.test2
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#@pytest.mark.test1
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

#@pytest.mark.test1
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_product_in_basket()
    basket_page.should_be_message_about_empty_basket()

#
# @pytest.mark.login
# class TestLoginFromProductPage():
#     # этот класс только для примера подготовки и очистки данных
#     @pytest.fixture(scope="function", autouse=True)
#     def setup(self):
#         self.product = ProductFactory(title="Best book created by robot")
#         # создаем по апи
#         self.link = self.product.link
#         yield
#         # после этого ключевого слова начинается teardown
#         # выполнится после каждого теста в классе
#         # удаляем те данные, которые мы создали
#         self.product.delete()
#
#     def test_guest_can_go_to_login_page_from_product_page(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
#
#     def test_guest_should_see_login_link(self, browser):
#         page = ProductPage(browser, self.link)
#         # дальше обычная реализация теста
#

#
