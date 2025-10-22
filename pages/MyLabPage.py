from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait



class MyLabPage:

    def __init__(self, driver):
        self.driver = driver

    def get(self):
        self.driver.get("https://www.labirint.ru/cabinet/personal/")

    def window_my_lab(self):
        my_lab =self.driver.find_element(By.CSS_SELECTOR, "a.top-link-main_cabinet")
        self.actions.move_to_element(my_lab()).perform()
        self.driver.find_element(By.CSS_SELECTOR, "a.user-top-menu-link").click()
