from selenium.webdriver.common.by import By
from core.core_ui.web_driver_manager import SingletonWebDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from core.pages.base_page import BasePage

import time


class TeamPage(BasePage):
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Nombre del equipo')]/following-sibling::input")
    TYPE_TEAM_LIST = (By.CSS_SELECTOR, "div.css-dmzcl._1T1MG_BX1zeaq8")
    OPTION_TYPE_TEAM = (By.XPATH, "//li[contains(text(), 'Otro')]")
    BUTTON_CONTINUE = (By.XPATH, "//button[contains(text(), 'Continuar')]")

    def __init__(self):
        super().__init__()
        try:
            self.wait.until(ec.visibility_of_element_located(self.NAME_INPUT))
        finally:
            print("error Team Page")

    def select_type_team(self):
        self.wait.until(ec.visibility_of_element_located(self.TYPE_TEAM_LIST))
        self.browser.find_element(*self.TYPE_TEAM_LIST).click()
        self.wait.until(ec.visibility_of_element_located(self.OPTION_TYPE_TEAM))
        self.browser.find_element(*self.OPTION_TYPE_TEAM).click()

    def set_team_name(self, team_name):
        self.wait.until(ec.visibility_of_element_located(self.NAME_INPUT))
        self.browser.find_element(*self.NAME_INPUT).send_keys(team_name)

    def click_continue_button(self):
        self.wait.until(ec.visibility_of_element_located(self.BUTTON_CONTINUE))
        self.browser.find_element(*self.BUTTON_CONTINUE).click()
