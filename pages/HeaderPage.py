from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HeaderPage:
    
    def __init__(self, driver):
        self.actions = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def head_books(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/books/']")
        # self.actions.move_to_element(element).perform()        # Навести курсор на элемент
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/best/']").click()
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.content-block")))
        txt = self.driver.find_element(By.CSS_SELECTOR, "div.content-block").text
        return txt

    # def get_url(self, url: str):
    #     self.driver.get(url)