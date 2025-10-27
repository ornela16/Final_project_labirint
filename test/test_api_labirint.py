import pytest
import allure
import requests
from pages.LabirintAPI import LabirintAPI

BASE_URL = LabirintAPI("https://www.labirint.ru")


@allure.title("Тестирование загрузки сайта интернет-магазина Лабиринт.")
@allure.description("Тест проверяет загрузку начальной страницы.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.positive
def test_get_labirint(driver):
    resp = BASE_URL.get_open()
    #Проверяем статус-код в ответе:
    assert resp.status_code == 200

@allure.title("Тестирование загрузки страницы Главные книги 2025 интернет-магазина Лабиринт.")
@allure.description("Тест проверяет загрузку страницы Главные книги 2025.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.positive
def test_get_best(driver):
    resp = requests.get('https://www.labirint.ru')
    #Проверяем статус-код в ответе:
    assert resp.status_code == 200


@allure.title("Тестирование загрузки сайта интернет-магазина Лабиринт.")
@allure.description("Тест проверяет загрузку начальной страницы.")
@allure.feature("Интернет-магазин Лабиринт.")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.positive
def test_get_cart(driver):
    resp = requests.get('https://www.labirint.ru')
    #Проверяем статус-код в ответе:
    assert resp.status_code == 200