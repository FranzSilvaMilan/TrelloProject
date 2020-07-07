from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
        self.driver.get("https://trello.com/login")

    def set_user(self, user):
        self.driver.find_element_by_id("user").send_keys(user)

    def set_password(self, password):
        self.driver.find_element_by_id("password").send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id("login").click()
