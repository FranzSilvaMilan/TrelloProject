from core.logger.singleton_logger import SingletonLogger
from core.core_ui.web_driver_manager import SingletonWebDriverManager

logger = SingletonLogger().get_logger()


def before_scenario(context, scenario):
    logger.info("Start browser")
    context.web = SingletonWebDriverManager()
    context.web.start_browser()


def after_scenario(context, scenario):
    logger.info("Quit browser")
    context.web.quit_browser()
