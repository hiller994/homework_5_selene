import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True) #autouse=True фикстура выполняется автоматически
def browser_management():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs/'  # тут указываем URL, чтобы потом его не указывать
    browser.config.timeout = 2.0 #ЭТО ожидание селена, по умолчанию 4 сек
    #browser.config.driver_name = 'Chrome' #этот способ для примера новичков
    #browser.config.driver_options = webdriver.FirefoxOptions() #еще один способ открытия нужного браузера
    #browser.config.build_driver_strategy #тут описана логика определения бразера. Если мы ничего не указываем, открывается хром

    #как запускать браузер:
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless') # тут мы указываем, чтобы браузер стал невидимым (не открывем его) !!!!УМЕНЬШАНО ВРЕМЯ ТЕСТА
    browser.config.driver_options = driver_options # сам запуск

    yield

    browser.quit()