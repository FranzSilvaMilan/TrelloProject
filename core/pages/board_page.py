from selenium.webdriver.common.by import By
from core.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

import time


class BoardPage(BasePage):

    ADD_TO_LIST_LINK = (By.CSS_SELECTOR, "a.open-add-list.js-open-add-list span")
    INPUT_lIST_NAME = (By.CSS_SELECTOR, "input.list-name-input")
    ADD_LIST_BUTTON = (By.CSS_SELECTOR, "input.primary.mod-list-add-button.js-save-edit")
    BOARD_NAME_SPAN = (By.CSS_SELECTOR, "span.js-board-editing-target.board-header-btn-text")
    BOARD_MAME_DIV = (By.CSS_SELECTOR, "div.board-header-btn.mod-board-name.inline-rename-board.js-rename-board")
    BOARD_NAME_INPUT = (By.CSS_SELECTOR, "input.board-name-input.js-board-name-input")
    BOARD_MAIN_CONTENT = (By.CSS_SELECTOR, "div.board-main-content")
    MEMBER_SPAN = (By.CSS_SELECTOR, "a span.member-initials")
    MEMBER_NAME = (By.CSS_SELECTOR, "a.mini-profile-info-title-link.js-profile")
    MEMBER_ROL = (By.CSS_SELECTOR, "span.quiet.u-font-weight-normal")

    def __init__(self):
        super().__init__()
        try:
            self.wait.until(ec.presence_of_element_located(self.ADD_TO_LIST_LINK))
        finally:
            print("error Load Board Page")

    def click_add_to_list(self):
        self.wait.until(ec.visibility_of_element_located(self.ADD_TO_LIST_LINK))
        self.browser.find_element(*self.ADD_TO_LIST_LINK).click()

    def set_list_name(self, list_name):
        self.wait.until(ec.visibility_of_element_located(self.INPUT_lIST_NAME))
        self.browser.find_element(*self.INPUT_lIST_NAME).send_keys(list_name)

    def click_add_list_button(self):
        self.wait.until(ec.visibility_of_element_located(self.ADD_LIST_BUTTON))
        self.browser.find_element(*self.ADD_LIST_BUTTON).click()

    def update_board_name(self, new_update_name):
        element = self.browser.find_element(*self.BOARD_MAME_DIV)
        self.browser.execute_script("arguments[0].setAttribute('class','board-header-btn mod-board-name "
                                    "inline-rename-board js-rename-board is-editing')", element)
        self.browser.find_element(*self.BOARD_NAME_INPUT).click()
        self.browser.find_element(*self.BOARD_NAME_INPUT).clear()
        self.browser.find_element(*self.BOARD_NAME_INPUT).send_keys(new_update_name)
        self.browser.find_element(*self.BOARD_MAIN_CONTENT).click()

    def click_member_info(self):
        self.wait.until(ec.visibility_of_element_located(self.MEMBER_SPAN))
        self.click_element(self.MEMBER_SPAN)

    def get_member_name(self):
        self.wait.until(ec.visibility_of_element_located(self.MEMBER_NAME))
        return self.browser.find_element(*self.MEMBER_NAME).text

    def get_member_rol(self):
        self.wait.until(ec.visibility_of_element_located(self.MEMBER_ROL))
        return self.browser.find_element(*self.MEMBER_ROL).text

    def get_board_name(self):
        self.wait.until(ec.visibility_of_element_located(self.BOARD_NAME_SPAN))
        return self.browser.find_element(*self.BOARD_NAME_SPAN).text
