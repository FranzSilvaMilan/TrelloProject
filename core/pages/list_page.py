from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

from core.pages.base_page import BasePage
import time


class ListPage(BasePage):
    ADD_TO_CARD_LINK = (By.CSS_SELECTOR, "span.js-add-a-card")
    INPUT_CARD_NAME = (By.CSS_SELECTOR, "textarea.list-card-composer-textarea.js-card-title")
    ADD_CARD_BUTTON = (By.CSS_SELECTOR, "input.primary.confirm.mod-compact.js-add-card")
    CARD_NAME_SPAN = (By.CSS_SELECTOR, "span.list-card-title.js-card-name")
    # LIST_NAME_LOCATOR = (By.CSS_SELECTOR, "h2.list-header-name-assist.js-list-name-assist")
    LIST_NAME_LOCATOR = (By.CSS_SELECTOR, "div.list-header-target.js-editing-target")
    LIST_NAME_TEXT_AREA = (By.CSS_SELECTOR, "textarea.list-header-name,mod-list-name.js-list-name-input")
    LIST_NAME_TEXT_AREA_EDIT = (By.CSS_SELECTOR, "textarea.list-header-name,mod-list-name.js-list-name-input.is-editing")

    def __init__(self):
        super().__init__()

    def click_add_to_card_link(self):
        self.click_element(self.ADD_TO_CARD_LINK)

    def set_card_name(self, card_name):
        self.browser.find_element(*self.INPUT_CARD_NAME).send_keys(card_name)

    def click_add_card_button(self):
        self.click_element(self.ADD_CARD_BUTTON)

    def get_text_card_name(self):
        self.wait.until(ec.visibility_of_element_located(self.CARD_NAME_SPAN))
        return self.browser.find_element(*self.CARD_NAME_SPAN).text

    def get_list_name(self):
        self.wait.until(ec.visibility_of_element_located(self.LIST_NAME_LOCATOR))
        return self.browser.find_element(*self.LIST_NAME_LOCATOR).text

    def update_list_name(self, new_update_name):
        element = self.browser.find_element(*self.LIST_NAME_TEXT_AREA)
        self.browser.execute_script("arguments[0].setAttribute('class','list-header-name mod-list-name "
                                    "js-list-name-input is-editing')", element)
        self.browser.find_element(*self.LIST_NAME_TEXT_AREA_EDIT).click()
        self.browser.find_element(*self.LIST_NAME_TEXT_AREA_EDIT).clear()
        self.browser.find_element(*self.LIST_NAME_TEXT_AREA_EDIT).send_keys(new_update_name)
