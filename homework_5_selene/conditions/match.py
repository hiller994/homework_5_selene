#пред импорт
from selene.support.conditions.be import *
from selene.support.conditions.have import *

#тут мы объединили 2 библиотеки, чтобы в тесте не писать отдельно be и have
'''
например:
browser.element('#new-todo').should(match.blank) # мы тут проверяем (should), что элемент пустой (be.blank)
browser.all('#todo-list').should(match.size(3)) #тут мы проверяем (should), что есть 3 записи, которые мы сделали выше
'''


