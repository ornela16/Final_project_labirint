import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера в браузере Firefox.
    """
    browser = webdriver.Firefox()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера в браузере Chrome.
    """
    browser = webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()