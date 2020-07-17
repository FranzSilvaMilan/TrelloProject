from selenium.webdriver.common.by import By
from core.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class WelcomePage(BasePage):
    INPUT_BOARD_NAME = (By.CSS_SELECTOR, "input.subtle-input")
    CREATE_BOARD = (By.CSS_SELECTOR, "div.board-tile.mod-add")
    CREATE_BOARD_BUTTON = (By.CSS_SELECTOR, "button.button.primary")
    CREATE_TEAM_SPAN = (By.CSS_SELECTOR, "button span._12-5x14JSgUact span")

    def __init__(self):
        super().__init__()

    def click_create_board(self,):
        self.wait.until(ec.visibility_of_element_located(self.CREATE_BOARD))
        self.browser.find_element(*self.CREATE_BOARD).click()

    def set_board_name(self, board_name):
        self.wait.until(ec.presence_of_element_located(self.INPUT_BOARD_NAME))
        self.browser.find_element(*self.INPUT_BOARD_NAME).send_keys(board_name)

    def click_create_board_button(self):
        self.wait.until(ec.visibility_of_element_located(self.CREATE_BOARD_BUTTON))
        self.browser.find_element(*self.CREATE_BOARD_BUTTON).click()

    def click_create_team(self):
        self.wait.until(ec.visibility_of_element_located(self.CREATE_TEAM_SPAN))
        self.click_element(self.CREATE_TEAM_SPAN)
