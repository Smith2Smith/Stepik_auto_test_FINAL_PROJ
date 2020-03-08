#Stepik_auto_test_FINAL_PROJ
#Stepik_auto_test_FINAL_PROJ/test_login_page.py
#test_login_page.py

# ФАЙЛ С ТЕСТАМИ страницы логина сайта

#Запуск :
#pytest -v --tb=line --language=en test_login_page.py

#--tb=line указывает, что нужно выводить только одну строку из лога каждого упавшего теста

# from .pages.login_page import LoginPage
#
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#
#     page = LoginPage(browser, link)     # инициализируем Page Object, передаем в конструктор
#                                         # экземпляр драйвера и url адрес
#
#     page.open()                         # открываем страницу
#
#     page.should_be_login_page()         # выполняем метод страницы -
#                                         # проверяем страницу логина