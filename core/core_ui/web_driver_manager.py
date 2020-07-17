import selenium.webdriver

from core.core_ui.config import Config


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonWebDriverManager(object, metaclass=Singleton):

    def __init__(self):
        self.config = Config.config()
        self.browser = ""

    def start_browser(self):
        # Initialize the WebDriver instance
        if self.config['browser'] == 'Firefox':
            self.browser = selenium.webdriver.Firefox()
        elif self.config['browser'] == 'Chrome':
            self.browser = selenium.webdriver.Chrome(executable_path= "C:\\ChromeDriver\\chromedriver.exe")

        self.browser.implicitly_wait(self.config['implicit_wait'])
        self.browser.get("https://trello.com/login")

    def get_browser(self):
        return self.browser

    def quit_browser(self):
        self.browser.quit()
