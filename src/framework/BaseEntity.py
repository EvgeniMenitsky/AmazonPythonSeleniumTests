from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.framework.Logger import Logger
from src.framework.Driver import Driver
from src.resources.selenium import DEFAULT_WAIT


class BaseEntity(object):
    driver = Driver().get_instance()
    logger = Logger.get_instance()

    def __init__(self, type, locator, name=None):
        self.type = type
        self.locator = locator
        self.name = name

    def get_locator(self):
        """Get locator"""
        return self.locator

    def get_type(self):
        """Get type of locator"""
        return self.type

    def get_element(self):
        """
        Get element
        Returns:
            web element
        """
        try:
            element = self.driver.find_element(by=self.type, value=self.locator)
        except StaleElementReferenceException:
            WebDriverWait(self.driver, DEFAULT_WAIT).until(EC.StaleElementReferenceException)
        finally:
            element = WebDriverWait(self.driver, DEFAULT_WAIT).until(
                EC.presence_of_element_located(locator=(self.type, self.locator)))
            return element

    def get_list_elements(self):
        """
        Get list of elements
        Returns:
            web elements
        """
        try:
            elements = self.driver.find_elements(by=self.type, value=self.locator)
        except StaleElementReferenceException:
            WebDriverWait(self.driver, DEFAULT_WAIT).until(EC.StaleElementReferenceException)
        return elements
