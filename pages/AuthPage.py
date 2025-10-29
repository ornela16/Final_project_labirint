from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthPage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(self.driver, 20)

    def form_auth(self, phone):
        element = self.driver.find_element(
            By.CSS_SELECTOR, "span.b-header-b-personal-e-icon.b-header-b-personal-e-icon-m-profile.b-header-e-sprite-background") # Значок Мой Лабиринт
        self.actions.move_to_element(element).perform()        # Навести курсор на элемент
        self.driver.find_element(By.CSS_SELECTOR, "a[data-sendto-params='auth-registration']")       # Всплывающее окно Вход или регистрация в Лабиринте
        self.driver.find_element(By.CSS_SELECTOR, "a[href='#']")
        self.driver.execute_script("arguments[0].click();", element)                                # Нажать на Вход или регистрация в Лабиринте
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.new-auth__show-soc")))
        self.driver.find_element(By.CSS_SELECTOR, "div.new-auth__show-soc")                          # Окно для ввода номера телефона, email или кода скидки
        self.driver.find_element(By.CSS_SELECTOR, "input.full-input__input.formvalidate-error").send_keys(phone)      # Ввести номер телефона
        self.driver.find_element(
            By.CSS_SELECTOR, "input.new-auth__button.js-submit.js-submit-by-code.new-auth__input.full-input__input.new-forms__input_size_m").click()   # Кнопка Войти
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.lab-modal-container.new-auth.js-new-auth.js-new-forms.new-forms")))  # Поле ввода кода - 4 цифры
        try:                                                                                                                             # входящего звонка
            is_displayed = self.driver.find_element(By.CSS_SELECTOR, "div.lab-modal-container.new-auth.js-new-auth.js-new-forms.new-forms").is_displayed()
        except:
            is_displayed = True
        return is_displayed