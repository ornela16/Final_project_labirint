import requests
import allure
import pytest
from config import cookies, headers

BASE_URL = "https://www.labirint.ru"

@allure.title("Тест для просмотра содержимого корзины интернет-магазина Лабиринт.")
@pytest.mark.positive
@pytest.mark.api
def test_basket_contents():
    payload = {}
    response = requests.request("GET", BASE_URL + '/ajax/basket/', cookies=cookies,headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200


@allure.title("Тест для добавления книги в корзину интернет-магазина Лабиринт.")
@pytest.mark.positive
@pytest.mark.api
def test_add_book_to_basket():
    book_id = "796310"
    payload = f"id={book_id}&s=1&charity=0"
    response = requests.request("POST", BASE_URL + '/buy.php?JsHttpRequest=0-xml', cookies=cookies, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200


@allure.title("Тест для удаления книги из корзины на сайте Лабиринт.")
@pytest.mark.positive
@pytest.mark.api
def test_remove_book_from_cart():
    """Тест удаления книги из корзины"""
    book_id = 90376
    payload = {"del_goods": str(book_id)}  # параметр удаления
    response = requests.request("POST", BASE_URL + '/ajax/basket/', cookies=cookies, headers=headers, data=payload)
    assert response.status_code == 200, f"Ошибка при удалении: {response.text}"


@allure.title("Тест для получения страницы книги по id на сайте Лабиринт.")
@pytest.mark.positive
@pytest.mark.api
def test_get_book_by_id():
    payload = {}
    response = requests.request("POST", BASE_URL + "/books/763115/", headers=headers, data=payload)
    assert response.status_code == 200


@allure.title("Тест для поиска книг по названию, автору или ключевому слову")
@allure.feature("Поиск книг")
@pytest.mark.api
def test_search_books():
    """Проверка поиска по ключевому слову"""
    payload = {"searchKeyword": "Гиляровский"}
    response = requests.request("POST", BASE_URL + "/search/searchKeyword/?stype=0", headers=headers, data=payload)
    assert response.status_code == 200


@allure.title("Негативный тест для поиска книг с пустым полем запроса.")
@allure.feature("Поиск книг")
@pytest.mark.negative
@pytest.mark.api
def test_search_empty_query():
    payload = {"searchKeyword": ""}
    response = requests.request("POST", BASE_URL + "/search/searchKeyword/?stype=0", headers=headers, data=payload)
    assert response.status_code == 200

@allure.title("Негативный тест для авторизации с Невалидными данными")
@allure.feature("Авторизация")
@pytest.mark.negative
@pytest.mark.api
def test_login_invalid_credentials():
    """Авторизация с неверными данными"""
    payload = {"email": "fake@example.com", "pwd": "wrongpassword"}
    response = requests.request("POST", BASE_URL + "/cabinet/login/", headers=headers, data=payload)
    assert response.status_code == 401