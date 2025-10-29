import pytest
import allure
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
from pages.CartPage import CartPage
from pages.SalePage import SalePage
from pages.AuthPage import AuthPage
from pages.HeaderPage import HeaderPage


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
    is_clicable = auth_page.form_auth("9113186835")
    assert is_clicable is True


@allure.title("Тестирование работы второго хедера на начальной странице сайта Лабиринт.")
@allure.description("Тест проверяет кликабельность кнопок разделов и переход между страницами во втором хедере.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.positive
def test_second_header(driver):
    """Тест проверяет работу второго хедера на начальной странице сайта Лабиринт: кликабельность кнопок разделов и переход между страницами."""
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    header_page = HeaderPage(driver)
    header_page.second_header()
    assert header_page.get_current_url().endswith("support/")


@allure.title("Тестирование поиска книг на начальной странице сайта по ключевому слову и добавление в корзину.")
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


@allure.title("Тестирование поиска книг с пустым полем поиска на начальной странице.")
@allure.description("Тест проверяет возможность поиска книг с пустым полем поиска.")
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


@allure.title("Тестирование поиска книг в разделе скидок, проверка количества найденных книг.")
@allure.description("Тест проверяет возможность найти книги в разделе скидок Лучшая покупка дня.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive
def test_hold_over(browser):
    """ Тестирование добавления книг в Отложенные, проверка количества отложенных книг."""
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    sale_page = SalePage(browser)
    sale_page.get()
    sale_page.find_here()
    sale_page.search_sale("Счастье")
    element_txt =  sale_page.number_of_goods()
    assert "17 товаров" in element_txt


@allure.title("Тестирование загрузки страницы 'Главные книги 2025'.")
@allure.description("Тест проверяет загрузку страницы при клике по кнопке 'Главное 2025' в хедере.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.positive
def test_get_best(browser):
    """Тест проверяет корректный переход по ссылке при клике по кнопке 'Главное 2025' """
    main_page = MainPage(browser)
    main_page.set_cookie_policy()
    header_page = HeaderPage(browser)
    txt = header_page.head_books()
    assert header_page.get_current_url().endswith("best/")
    assert txt == "Главные книги 2025"