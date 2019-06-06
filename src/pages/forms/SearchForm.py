from selenium.webdriver.common.by import By
from src.framework.BasePage import BasePage
from src.framework.elements.Elements import *


class SearchForm(BasePage):
    """
    Search orders form
    """
    __SEARCH_FIELD = TextField(type=By.ID, locator='twotabsearchtextbox', name='Search Text Field')
    __CATEGORY_DROPDOWN = Dropdown(type=By.XPATH,
                                   locator="//select[contains(@aria-describedby, 'searchDropdownDescription')]",
                                   name='Category Dropdown')
    __START_SEARCH_BUTTON = Button(type=By.XPATH, locator="//input[@value='Go']", name='Go Search Button')

    def __init__(self):
        super().__init__(type=By.ID, locator='navbar', name='Search Form')

    def search_order_by_name(self, order_name):
        """
        Search order by name in system. Input search text and start search
        Args:
            name: name of order.
        """
        self.__SEARCH_FIELD.set_text(order_name)
        self.__START_SEARCH_BUTTON.click()

    def select_order_category(self, category_name):
        """
        Select order category by category name
        Args:
            category_name: category name
        """
        self.__CATEGORY_DROPDOWN.click()
        self.__CATEGORY_DROPDOWN.select_option_by_visible_text(text=category_name)
