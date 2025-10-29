from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SalePage:

    def __init__(self, driver):
        self.actions = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 50)

    def get(self):
        self.driver.get("https://www.labirint.ru/best/sale/")   # перейти на страницу Лучшая покупка дня

    def find_here(self):
        self.driver.find_element(By.CSS_SELECTOR, "span.header-sprite.navisort-find-here__icon").click() # нажать Найти здесь

    def search_sale(self, title):
        self.driver.find_element(By.CSS_SELECTOR, "input.text.navisort-find-text").send_keys(title)  # в поле поиска ввести слова для поиска книги
        self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-small.btn-more.navisort-find-btn.only_desc").click()
        self.wait.until(EC.invisibility_of_element_located((By.ID, "loader")))
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "span.navisort-head-text.navisort-head-books-count")))

    def number_of_goods(self):
        element_txt = self.driver.find_element(By.CSS_SELECTOR, "span.navisort-head-text.navisort-head-books-count").text
        return element_txt