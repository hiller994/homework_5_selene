from itertools import dropwhile
from selene import query
from selene import command

import pytest
from selene import browser, have, be, by
from selenium.webdriver.common.by import By #пример селениума вебдрайвре
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

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
    #browser.all('#todo-list').with_(timeout=4.0).should(have.size(3)) # ждем 4 сек перед действием
    #browser.all('#todo-list').with_(timeout=browser.config.timeout*2).should(have.size(3))  # ждем (таймаут из конфига * 2) перед действием
    browser.all('#todo-list>li').should(have.size(3)) #тут мы проверяем (should), что есть 3 записи, которые мы сделали выше. Match вместо have

    #-----------------пример проверки строки выше на selenium
    assert browser.driver.find_element(By.CSS_SELECTOR, '#todo-list>li')
    # или скоращаем с помощью библиотеки by
    assert len(browser.driver.find_element(*by.css('#todo-list>li'))) == 3 #проверяем, что размер (len = 3). Это плохая проверка, т.к. селениум будет сразу проверять элемент, но данные могут не сразу подтянуться
    #should, в отличии от ассерта в селениуме, умеет ждать.


    '''
    #пример ожидания в селениуме и проверке данных
    WebDriverWait(driver=browser.driver, timeout=3.0).until(lambda driver: len(browser.driver.find_element(*by.css('#todo-list>li'))==3))
    #НО благодаря селен, можно сокращаем:
    browser.all('#todo-list>li').should(have.size(3)) # проверяем, что именно 3 появилось записм
    browser.all('#todo-list>li').wait.for_(have.size(3)) # ДОЖИДАЕМСЯ, что именно 3 появилось записм
    '''

    #query – библиотека, позволяющая использовать selenium webdriver в selene
    #пример вытягивание из объекта данных, напирмер:
    initial_value = browser.element('#new-todo').get(query.attribute('value')) #присваиваем переменной значение из элемента
    browser.element('#new-todo').should(have.value(initial_value)) #далее в переменной проверяем, что именно это значение и есть





    #COMMAND библиотека, которая позволяет выполнять компанды, например выделение текста:
    browser.element('#new-todo')perfom(command.select_all) #через перформ выделяет текст в элементе
    '''
    В селен есть не все команды, например нет
- drag and drop
- upload
Для этого всего есть библиотека command

    '''
#Чтобы запустить отдельную строку, нужно:
#Выделить нужную строку -> ПКМ -> Execute Selection in Python Console
#РАБОТАЕТ ПО ОСТАНОВЕ

#также можно использовать команды, чтобы использовать JS при тесте. Например: обычный клик не работает и кликаем через JS
browser.element('#save').click()
browser.element('#save').perform(command.js.click)
#или
browser.element('#save').with_(click_by_js=True).click() # Это клик JS именно на эту кнопку

#У автотестов есть проблема - вводится текст по 1 букве. Чтобы ускорить текст, можно использовать конфиг
browser.config.type_by_js = True

#Если нужно несколько кликов, то:
save = browser.element('#save').with_(click_by_js=True)
save.click()
save.click()
save.click()
save.click()

#--------------------
#Коллекции
#на примере этой строки
browser.all('#todo-list>li').should(have.size(3)) #тут мы проверяем (should), что есть 3 записи, которые мы сделали выше. Match вместо have
browser.all('#todo-list>li').first.should(have.exact_text('a')) # проверяем, что в первом элементе родительского элемента есть текст А
browser.all('#todo-list>li').second.should(have.exact_text('a')) # следующий
#или обращаться по индексам
browser.all('#todo-list>li')[2].should(have.exact_text('с')) # т.е. в 3 элементе есть текст а
browser.all('#todo-list>li')[-1].should(have.exact_text('с')) # это последний элемент

# в одну срочку проверяем сразу все элементы
browser.all('#todo-list>li').should(have.exact_texts('a','b','c')) # вызывается только на all, а не на element
#проверяет, что именно в этом элементе присутствуют значения, в таком количесвте и в таком порядке

#находим элемент внутри элемента
browser.all('#todo-list>li').second.element('.toggle').click() #мы тут из родительского элемента находим чек-бокс и кликаем. Тут выбираем номеру в списке second
#или найти по тексту этот чек-бокс
browser.all('#todo-list>li').element_by(have.exact_text('b')).element('toggle').click()

#находим элементы по нужному нам параметру, например в списке найти элементы, которые отмечены чек-боксами
browser.all('#todo-list>li').element_by(have.css_class('completed')).should(have.exact_text('b')) #находит 1 элемент с классом 'completed'
browser.all('#todo-list>li').by(have.css_class('completed')).should(have.exact_texts('b')) #находит все элементы с классом 'completed' и из них находит именно элемент с текстом b
browser.all('#todo-list>li').by(have.no.css_class('completed')).should(have.exact_texts('a''c')) #находит все элементы с классом ' НЕ completed' и из них находит именно элемент с текстом a и с. Проверяем, что они остались активны

#нахождение элемента по xpath
browser.element('//*[@id="todo-list"]/li[normalsize-space(.)="b"]//*[contains(concat(" ", @class, " "), " toggle "))]').click()