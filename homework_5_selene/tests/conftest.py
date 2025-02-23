import pytest
from selene import browser, be, have
from selenium import webdriver


@pytest.fixture(scope="session")
def browser_settings():
    driver_options = webdriver.ChromeOptions()
    #driver_options.add_argument('--headless')  #скрыть браузер
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options  # сам запуск|
    browser.config.window_height = 1920  # высота браузера
    browser.config.window_width = 1080  # ширина браузера
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 5.0  # ЭТО ожидание селена, по умолчанию 4 сек


    yield

    browser.quit()