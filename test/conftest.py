import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from time import sleep

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

@pytest.fixture(scope="session")
def login_session():
    """
    Фикстура для авторизации по номеру телефона.
    Запускается один раз на всю сессию тестов.
    """
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")                              # URL формы логина

    phone_input = driver.find_element(By.ID, "phone_input")        # Вводим номер телефона
    phone_input.send_keys("+79998887766")
    driver.find_element(By.ID, "get_code_btn").click()             # Жмем кнопку "Получить код"

    code = input("Введите код из SMS или звонка: ")                      # Ввод кода вручную
    code_input = driver.find_element(By.ID, "code_input")          # Вводим код
    code_input.send_keys(code)
    driver.find_element(By.ID, "submit_code_btn").click()
    sleep(3)

    assert "Личный кабинет" in driver.page_source, "Авторизация не выполнена"        # Проверяем, что вошли успешно

    yield driver                                                            # Возвращаем драйвер для повторного использования
    driver.quit()                                                           # После всех тестов закрываем браузер


