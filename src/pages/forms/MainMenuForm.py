from selenium.webdriver.common.by import By
from src.framework.BasePage import BasePage
from src.framework.elements.Elements import *


class MainMenuForm(BasePage):
    """
    Main menu form
    """
    __CART_BUTTON = Button(type=By.ID, locator='#nav-cart', name='Cart Button')

    def __init__(self):
        super().__init__(type=By.ID, locator='nav-main', name='Main Menu Form')

    def open_cart(self):
        """
        Click Open Cart button. Open Cart page
        """
        self.__CART_BUTTON.click()
