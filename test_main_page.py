#Stepik_auto_test_FINAL_PROJ
#Stepik_auto_test_FINAL_PROJ/test_main_page.py
#test_main_page.py

# ФАЙЛ С ТЕСТАМИ главной страницы сайта

#Запуск :
#pytest -v --tb=line --language=en test_main_page.py

#--tb=line указывает, что нужно выводить только одну строку из лога каждого упавшего теста

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.mark.need_review_custom_scenarios
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)              # инициализируем Page Object, передаем в конструктор
                                                    # экземпляр драйвера и url адрес
        page.open()                                 # открываем страницу
        page.go_to_login_page()     # выполняем метод страницы переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @pytest.mark.need_review_custom_scenarios
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()         # проверяем есть ли ссылка на логин

@pytest.mark.need_review_custom_scenarios
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_product_in_basket()
    basket_page.should_be_message_about_empty_basket()

#