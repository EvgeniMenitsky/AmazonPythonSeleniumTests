import pytest
from src.framework.Driver import Driver
from src.resources.selenium import URL
from src.framework.Logger import Logger


class BaseTest(object):
    driver = None
    logger = Logger.get_instance()

    def setup(self):
        """
        Test setup. Open test url and maximize window
        """
        self.logger.info(msg='OPEN BROWSER')
        self.driver = Driver().get_instance()
        self.logger.info(msg='Go to {0}'.format(URL))
        self.driver.get(URL)
        self.driver.maximize_window()

    def teardown(self):
        """
        Test teardown. Close browser, clear driver
        """
        self.logger.info(msg='CLOSE BROWSER')
        self.driver.close()
        self.driver.quit()
