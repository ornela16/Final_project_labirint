import requests
from config import BASE_URL, headers


class LabirintAPI:
    """Класс для работы с API"""
    def __init__(self, url: str, headers: str):          # Инициализация
        self.url = BASE_URL
        self.headers = headers
        self.get_cart()
        self.get_open()


    # Получить начальную страницу сайта Лабиринт
    def get_open(self):
        resp = requests.get(self.url, self.headers)
        return resp.json()

    # Получить раздел каталога Главное 2025
    def get_best(self):
        resp = requests.get(self.url + '/best/')
        return resp.json()

    # Получить раздел Корзина
    def get_cart(self):
        resp = requests.get(self.url + '/ajax/basket/')
        return resp.json()

    # Получить раздел Товары в корзине
    def get_product_cart(self):
        resp = requests.get(self.url + '/cart/ajaxmainorder/')
        return resp.json()

    def add_book_to_cart(self, book_id: str):
        """Тест добавления книги в корзину"""
        resp = requests.get(self.url + '/buy.php?JsHttpRequest=0-xml')
        return resp.json()