from selenium.webdriver.support.wait import WebDriverWait

from core.core_ui.web_driver_manager import SingletonWebDriverManager


class BasePage:

    def __init__(self):
        self.browser = SingletonWebDriverManager().get_browser()
        self.wait = WebDriverWait(self.browser, 10)

    def click_element(self, element):
        self.browser.find_element(*element).click()

    def set_input_text(self, element, text):
        self.browser.find_element(*element).send_keys(text)
