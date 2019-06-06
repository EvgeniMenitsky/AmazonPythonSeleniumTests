import os
from selenium import webdriver
from src.resources.selenium import BROWSER
from src.resources.constants import DRIVERS_DIR


class BrowserFactory(object):
    @classmethod
    def create_browser(cls):
        """
        Create browser instance by browser
        Returns:
            webdriver instance
        """
        if BROWSER == 'chrome':
            return webdriver.Chrome(executable_path=os.path.join(DRIVERS_DIR, 'chromedriver.exe'))
        elif BROWSER == 'firefox':
            return webdriver.Firefox(executable_path=os.path.join(DRIVERS_DIR, 'geckodriver.exe'))
        elif BROWSER == 'edge':
            return webdriver.Edge(executable_path=os.path.join(DRIVERS_DIR, 'msedgedriver.exe'))
        else:
            return webdriver.Chrome(executable_path=os.path.join(DRIVERS_DIR, 'chromedriver.exe'))
