from selenium.webdriver.common.by import By

class HoldPage:
    def __init__(self, driver):
        self.driver = driver

    def get(self):
        self.driver.get("https://www.labirint.ru/cabinet/putorder/")

    def get_hold_counter(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-small.btn-clear-blue.btn-putorder-select").click()     # выбрать все книги в отложенных
        txt = self.driver.find_element(By.CSS_SELECTOR, 'span.b-action-panel-e-counter').text
        number_str = txt.split()[0]  # Забираем только число из строки "Выбрано .. товара"
        return int(number_str)