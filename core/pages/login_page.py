from selenium.webdriver.common.by import By
from core.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    INPUT_USER = (By.ID, "user")
    INPUT_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")

    def __init__(self):
        super().__init__()
        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "login"))
            )
        finally:
            print("error login")

    def set_user(self, user):
        self.set_input_text(self.INPUT_USER, user)

    def set_password(self, password):
        self.browser.find_element(*self.INPUT_PASSWORD).send_keys(password)

    def click_login(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()