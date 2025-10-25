import pytest
import allure
from selenium import webdriver
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage
from pages.SalePage import SalePage
from pages.AuthPage import AuthPage
from pages.MyLabPage import MyLabPage
from pages.HeaderPage import HeaderPage
from pages.HoldPage import HoldPage
from time import sleep

@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    browser = webdriver.Firefox()
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()

@allure.title("Тестирование авторизации нового пользователя по номеру телефона.")
@allure.description("Тест проверяет возможность авторизации на сайте.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.positive
def test_go_in_new_user(driver):
    """Тестирование авторизации нового пользователя по номеру телефона."""
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    auth_page = AuthPage(driver)
    auth_page.form_auth("9113186835")
    sleep(5)
    assert auth_page.window_code() is True

@allure.title("Тестирование входа авторизованного пользователя в личный кабинет.")
@allure.description("Тест проверяет возможность просмотра личных данных пользователя.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.positive
def test_window_my_lab(driver):
    """Тест проверяет наличие всплывающего окна при наведении на кнопку 'Мой Лаб' в Header, просмотр личных данных в настройках кабинета."""
    """Предусловие теста: пользователь должен пройти авторизацию."""
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    my_page = MyLabPage(driver)
    my_page.get()
    my_page.window_my_lab()


@allure.title("Тестирование входа авторизованного пользователя в личный кабинет.")
@allure.description("Тест проверяет возможность просмотра личных данных пользователя.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive
def test_cart_counter(driver):
    """Тестирование поиска книг на начальной странице сайта по ключевому слову, добавление найденных книг в корзину,
   проверка количества книг в корзине."""
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    main_page.search("Пушкин")
    result_page = ResultPage(driver)
    expected_count = result_page.add_books()
    cart_page = CartPage(driver)
    cart_page.get()
    actual_count = cart_page.get_counter()  # Текущее значение счетчика на странице

    assert actual_count == expected_count

@allure.title("Тестирование входа авторизованного пользователя в личный кабинет.")
@allure.description("Тест проверяет возможность просмотра личных данных пользователя.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.negative
def test_empty_search(driver):
    """Тест поиска книг с пустым полем поиска на начальной странице."""
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    main_page.search("")
    result_page = ResultPage(driver)
    message = result_page.get_empty_result_message()
    print(message)

    assert message == "Пока не нашли для себя ничего в Лабиринте?"

@allure.title("Тестирование входа авторизованного пользователя в личный кабинет.")
@allure.description("Тест проверяет возможность просмотра личных данных пользователя.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive
def test_hold_over(driver):
    """ Тестирование добавления книг в Отложенные, проверка количества отложенных книг."""
    main_page = MainPage(driver)
    main_page.set_cookie_policy()

    sale_page = SalePage(driver)
    sale_page.get()
    sale_page.find_here()
    sale_page.search_sale("Счастье")

    result_page = ResultPage(driver)
    expected_count = result_page.add_books_hold_over()
    hold_page = HoldPage(driver)
    hold_page.get()
    actual_count = hold_page.get_hold_counter()  # Текущее значение счетчика на странице

    assert actual_count == expected_count

@pytest.mark.positive
def test_get_best(driver):
    """Тест проверяет корректный переход по ссылке при клике по кнопке 'Главное 2025' """
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    header_page = HeaderPage(driver)
    txt = header_page.head_books()

    assert header_page.get_current_url().endswith("...")
    assert txt == "Главные книги 2025"


# Вход на сайт Лабиринт.ру с некорректным кодом
#
# Добавление товара в корзину негативный сценарий