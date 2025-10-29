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
        return self.driver.find_elements(By.TAG_NAME, "h1")[0].text


    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    def second_header(self):
        self.driver.find_element(By.CSS_SELECTOR, "a.b-header-b-sec-menu-e-link").click()                               # Доставка и оплата
        self.driver.find_element(By.CSS_SELECTOR, "div.b-header-b-sec-menu.col-md-12>div>ul>li:nth-child(2)").click()   # Сертификаты
        self.driver.find_element(By.CSS_SELECTOR, "div.b-header-b-sec-menu.col-md-12>div>ul>li:nth-child(3)").click()   # Рейтинги
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/novelty/']").click()                                        # Новости
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/sale/']").click()                                           # Скидки
        self.driver.find_element(
            By.CSS_SELECTOR, "a.b-header-b-sec-menu-e-link.geotarget-block-phone.geotarget-block-phone-1.dropdown-link.have-dropdown-touchlink.no-select.pointer").click()
        self.driver.find_element(By.CSS_SELECTOR, "div.b-header-b-sec-menu.col-md-12>div>ul>li:nth-child(9)").click()   # Контакты
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/support/']").click()                                        # Поддержка