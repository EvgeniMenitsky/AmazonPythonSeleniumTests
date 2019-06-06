from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.framework.Logger import Logger
from src.framework.Driver import Driver
from src.resources.selenium import DEFAULT_WAIT


class WaitUtils(object):

    driver = Driver().get_instance()
    logger = Logger.get_instance()

    def __init__(self):
        pass

    @classmethod
    def is_clickable(cls, type, locator):
        return WebDriverWait(WaitUtils.driver, DEFAULT_WAIT).until(EC.element_to_be_clickable((type, locator)))

    @classmethod
    def is_clickable(cls, element):
        return WebDriverWait(WaitUtils.driver, DEFAULT_WAIT).until(EC.element_to_be_clickable((element.get_type(), element.get_locator())))

    @classmethod
    def presence_of_element(cls, element):
        return WebDriverWait(WaitUtils.driver, DEFAULT_WAIT).until(
            EC.element_to_be_clickable((element.get_type(), element.get_locator())))

    @classmethod
    def invisibility_of_element(cls, element):
        return WebDriverWait(WaitUtils.driver, DEFAULT_WAIT).until(
            EC.invisibility_of_element((element.get_type(), element.get_locator())))

