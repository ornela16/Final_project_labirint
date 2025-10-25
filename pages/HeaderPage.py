import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HeaderPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def head_books(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/best/']"))         # Ожидаем, что ссылка станет кликабельной
        )
        self.driver.execute_script("arguments[0].click();", element)         # Далее ожидаем, что появится нужный блок контента
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.content-block")))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

        #txt = self.driver.find_element(By.CSS_SELECTOR, "div.content-block").text
        print(txt)