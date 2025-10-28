import pytest
import requests
from selenium import webdriver

@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser

    browser.quit()

@pytest.fixture
def session():
    """Фикстура для сессии пользователя с данными cookies"""
    ses = requests.Session()
    ses.cookies.update(COOKIES)
    ses.headers.update(HEADERS)
    return ses


