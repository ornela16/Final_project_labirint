import pytest
from selenium import webdriver
from Final_project_labirint.pages.MainPage import MainPage
from Final_project_labirint.pages.ResultPage import ResultPage
from Final_project_labirint.pages.CartPage import CartPage
from Final_project_labirint.pages.SalePage import SalePage
from Final_project_labirint.pages.AuthPage import AuthPage
from Final_project_labirint.pages.MyLabPage import MyLabPage

cookie = {"name": "cookie_policy", "value": "1"}

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.labirint.ru/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.smoke
@pytest.mark.positive
def test_go_in_new_user():
    """Тестирование авторизации нового пользователя по номеру телефона."""
    browser = webdriver.Firefox()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    auth_page = AuthPage(browser)
    auth_page.form_auth("9113186835")
    auth_page.window_code()

    # assert auth_page.window_code().is_displayed() is True       проблема с проверкой!!!

@pytest.mark.smoke
@pytest.mark.positive
def test_window_my_lab():
    """Тест проверяет наличие всплывающего окна при наведении на кнопку 'Мой Лаб' в Header, просмотр личных данных в настройках кабинета."""
    """Предусловие теста: пользователь должен пройти авторизацию."""
    browser = webdriver.Firefox()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    my_page = MyLabPage(browser)
    my_page.get()
    my_page.window_my_lab()


@pytest.mark.positive
def test_cart_counter():
    """Тестирование поиска книг на начальной странице сайта по ключевому слову, добавление найденных книг в корзину,
   проверка количества книг в корзине."""
    browser = webdriver.Firefox()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search("Пушкин")
    result_page = ResultPage(browser)
    expected_count = result_page.add_books()
    cart_page = CartPage(browser)
    cart_page.get()                         # Переход на страницу с корзиной
    actual_count = cart_page.get_counter()  # Текущее значение счетчика на странице

    assert actual_count == expected_count

@pytest.mark.negative
def test_empty_search():
    """Тест поиска книг с пустым полем поиска на начальной странице."""
    browser = webdriver.Firefox()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    main_page.search("")
    result_page = ResultPage(browser)
    message = result_page.get_empty_result_message()
    print(message)

    assert message == "Пока не нашли для себя ничего в Лабиринте?"

@pytest.mark.positive
def test_hold_over():
    """ Тестирование добавления книг в Отложенные, проверка количества отложенных книг."""
    browser = webdriver.Firefox()
    main_page = MainPage(browser)
    main_page.set_cookie_policy()

    sale_page = SalePage(browser)
    sale_page.get()
    sale_page.find_here()
    sale_page.search_sale("Счастье")

    result_page = ResultPage(browser)
    expected_count = result_page.add_books_hold_over()

    # недоделан!!!

