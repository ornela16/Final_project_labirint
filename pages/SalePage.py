from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.icon-fave.track-tooltip.js-open-deferred-block")))
        sleep(10)
        wait = WebDriverWait(self.driver, 20)
        icon_fave = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.icon-fave.track-tooltip.js-open-deferred-block")))
        icon_fave.click()
        # element = self.driver.find_element(By.CSS_SELECTOR, "[data-tooltip_title='Отложить']")




