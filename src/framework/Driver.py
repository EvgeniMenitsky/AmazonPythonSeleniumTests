from src.framework.BrowserFactory import BrowserFactory
from src.resources.selenium import DEFAULT_WAIT


class Driver(object):
    __instance = None

    def __init__(self):
        """
        Create WebDriver instance
        """
        if not Driver.__instance:
            Driver.__instance = BrowserFactory().create_browser()
            Driver.get_instance().implicitly_wait(DEFAULT_WAIT)

    @classmethod
    def get_instance(cls):
        """
        Get WebDriver instance
        Returns:
            WebDriver
        """
        if not cls.__instance:
            cls.__instance = Driver()
        return cls.__instance
