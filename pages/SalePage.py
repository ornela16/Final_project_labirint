from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy.sql.base import elements


class SalePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def get(self):
        self.driver.get("https://www.labirint.ru/best/sale/")   # перейти на страницу Лучшая покупка дня

    def find_here(self):
        self.driver.find_element(By.CSS_SELECTOR, "span.header-sprite.navisort-find-here__icon").click() # нажать Найти здесь

    def search_sale(self, title):
        self.driver.find_element(By.CSS_SELECTOR, "input.text.navisort-find-text").send_keys(title)  # в поле поиска ввести слова для поиска книги
        self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-small.btn-more.navisort-find-btn.only_desc").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "a.icon-fave.track-tooltip.js-open-deferred-block")
        self.driver.execute_script("arguments[0].click();", element)

    def get_hold_over_items(self):
        self.driver.get_hold_over_items("https://www.labirint.ru/cabinet/putorder/")
        self.driver.find_element(By.CSS_SELECTOR, "span.checkbox-ui-e-bg.b-checkbox-e-bg-m-white.b-checkbox-m-radius").click()
        self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-small.btn-invert-white.btn-pad-10.mr10.js-ap-btn-main")

        self.driver.find_element(By.CSS_SELECTOR, "button#btn btn-small btn-clear-blue btn-putorder-select").click() # выбрать книгу в отложенных
        self.driver.find_element(By.CSS_SELECTOR, "span#only_mobile-inline").click()    # добавить в корзину отложенный товар
        self.driver.find_element(By.CSS_SELECTOR, "a#buy801288.btn buy-link btn-more").click()  # оформить отложенную книгу

