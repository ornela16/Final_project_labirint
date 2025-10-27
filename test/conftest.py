import pytest
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