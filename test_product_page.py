#Stepik_auto_test_FINAL_PROJ
#Stepik_auto_test_FINAL_PROJ/test_product_page.py
#test_product_page.py

# ФАЙЛ С ТЕСТАМИ добавление в корзину со страницы товара

#Запуск :
#pytest -v -s --tb=line --language=en test_product_page.py


from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_product_to_basket()
    page.should_be_correct_name_add_product_to_backet(page.product_name())
    page.should_be_correct_price_basket(page.product_price())

#