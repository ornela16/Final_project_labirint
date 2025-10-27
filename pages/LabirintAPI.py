import requests


class LabirintAPI:
    """Класс для работы с API"""
    def __init__(self, BASE_URL):          # Инициализация
        self.url = BASE_URL

    # Получить начальную страницу сайта Лабиринт
    def get_open(self):
        resp = requests.get(self.url)
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



