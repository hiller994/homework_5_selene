import pytest
from selene import browser, Browser, by
from selene.support.shared import config
from selenium import webdriver
from selenium.webdriver.chromium.webdriver import ChromiumDriver



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

    # пример внедрения селена в проект селениум, заворачивание в фикстуру функциона:
    # пример фикстуры из селениум веб драйвер
    @pytest.fixture()
    def driver():
        driver_options = webdriver.ChromeOptions()
        driver_options.add_argument('--headless')
        driver = webdriver.Chrome(service=ChromeService(executable_path=ChromDriverManager().install()), options=driver_options,)

        yield driver

        driver.quit()

    #и к данному фрейфорку прикручиваем селен
    @pytest.fixture()
    def browser(driver): #зависит от браузера

        yield Browser(config(driver=driver))

    #пример использования данной фикстуры, внедрение селен
    def test_complete_todo(driver, browser):
        driver.get('///') #открываем ссылку
        driver.find_element(*by.css('element').send_key('a' + Keys.ENTER))
        browser.element('#new-todo').type('a') # замена на селен, вместо строчки выше
        driver.find_element(*by.css('element').send_key('b' + Keys.ENTER))
        driver.find_element(*by.css('element').send_key('c' + Keys.ENTER))