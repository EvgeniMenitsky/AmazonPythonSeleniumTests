from selenium.webdriver.common.by import By
from src.framework.BasePage import BasePage


class MainPage(BasePage):
    """
    Main Page
    """

    def __init__(self):
        super().__init__(type=By.XPATH, locator="//div[@class= 'a-carousel-row-inner']", name='Main Page')
