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
        element = self.driver.find_element(By.CSS_SELECTOR, "span.b-header-b-personal-e-icon.b-header-b-personal-e-icon-m-profile.b-header-e-sprite-background")
        self.actions.move_to_element(element).perform()        # Навести курсор на элемент
        self.driver.find_element(By.CSS_SELECTOR, "a[data-sendto-params='auth-registration']")
        self.driver.find_element(By.CSS_SELECTOR, "a[href='#']")
        self.driver.execute_script("arguments[0].click();", element)
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.new-auth__show-soc")))
        self.driver.find_element(By.CSS_SELECTOR, "div.new-auth__show-soc")
        self.driver.find_element(By.CSS_SELECTOR, "input.full-input__input.formvalidate-error").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "div.new-auth__full-input.full-input.js-full-input.js-autofocus.js-input-email.full-input_success")
        self.driver.find_element(By.CSS_SELECTOR, "input.new-auth__button.js-submit.js-submit-by-code.new-auth__input.full-input__input.new-forms__input_size_m").click()

    def window_code(self):
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.lab-modal-container.new-auth.js-new-auth.js-new-forms.new-forms")))

        try:
            is_displayed = self.driver.find_element(By.CSS_SELECTOR, "div.lab-modal-container.new-auth.js-new-auth.js-new-forms.new-forms").is_displayed()
        except:
            is_displayed = True
        return is_displayed