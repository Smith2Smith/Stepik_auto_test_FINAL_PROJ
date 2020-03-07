#Stepik_auto_test_FINAL_PROJ
#pages/base_page.py
#base_page.py

from selenium.webdriver import Remote as RemoteWebDriver

# конструктор — метод, который вызывается, когда мы создаем объект.
# Конструктор объявляется ключевым словом __init__.
# В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
# Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
class BasePage():
    def __init__(self, browser: RemoteWebDriver , url):
        self.browser = browser
        self.url = url

    #метод open. Он должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

#