#Stepik_auto_test_FINAL_PROJ
#pages/base_page.py
#base_page.py

from selenium.webdriver import Remote as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import math

# конструктор — метод, который вызывается, когда мы создаем объект.
# Конструктор объявляется ключевым словом __init__.
# В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
# Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
class BasePage():
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)       # неявное ожидание со значением по умолчанию в 10

    #метод open. Он должен открывать нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    #в этом методе будем перехватывать исключение
    def is_element_present(self, how, what):
        # элемент есть на странице
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # проверка, что элемент не появляется на странице в течение заданного времени:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        # проверка, что какой-то элемент исчезает
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

#