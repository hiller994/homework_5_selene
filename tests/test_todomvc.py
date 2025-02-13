from itertools import dropwhile

from selene import browser, have, be
from selenium.webdriver.common.by import By #пример селениума вебдрайвре

from homework_5_selene.conditions import match


def test_complete_todo():
    browser.open('/') # Селен будет ссылаться на сохраненный в конфиге URL
    browser.element('#new-todo').should(be.blank) # мы тут проверяем (should), что элемент пустой (be.blank)
    #browser.driver.find_element(By.CSS_SELECTOR, '#new-todo') #пример селениума вебдрайвре

    #browser.element(selector) # здесь находит 1 элемент по селектору
    #browser.all(selector) # здесь находит все элементы по селектору

    browser.element('#new-todo').type('a') #находим элемент new-toddo и пишем в нем текст 'a'
    #или вместо #new-toddo написать [id=..], # - это скоращение для id
    browser.element('#new-todo').type('b')
    browser.element('#new-todo').type('c')
    browser.all('#todo-list').with_(timeout=4.0).should(have.size(3)) # ждем 4 сек перед действием
    browser.all('#todo-list').with_(timeout=browser.config.timeout*2).should(have.size(3))  # ждем (таймаут из конфига * 2) перед действием
    browser.all('#todo-list').should(have.size(3)) #тут мы проверяем (should), что есть 3 записи, которые мы сделали выше. Match вместо have

