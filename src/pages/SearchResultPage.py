from selenium.webdriver.common.by import By
from src.framework.BasePage import BasePage
from src.framework.elements.CheckBox import CheckBox
from src.framework.elements.Dropdown import Dropdown
from src.framework.elements.Label import Label
from src.framework.waits.WaitUtils import WaitUtils
import random


class SearchResultPage(BasePage):
    """
    Search Result Page
    """
    __SORT_DROPDOWN = Dropdown(type=By.ID, locator='s-result-sort-select', name='Sort Dropdown')
    __CONDITION_LOCATOR = "//ul[contains(@aria-labelledby,'condition-type-title')]//span[contains(@class,'color-base')and text()='%s']"
    __ORDER_NAMES_LOCATOR = "//div[contains(@class,'s-search-results')]//h2//span"
    __CHECKBOX_CONDITION = "//span[text()='%s']/parent::span/parent::label/input[@type='checkbox']/following-sibling::i"
    __PAGINATION = Label(type=By.XPATH, locator="//span[@data-component-type='s-pagination']", name='Pagination')

    def __init__(self):
        super().__init__(type=By.XPATH, locator="//span[contains(@data-component-type, 'result-info-bar')]",
                         name='Search Result Page')

    def select_language(self, language='English'):
        """
        Select language condition
        Args:
            language: name of language
        """
        CheckBox(By.XPATH, self.__CHECKBOX_CONDITION % language, '%s language condition' % language).click()

    def select_condition(self, condition='New'):
        """
        Select condition of novelty
        Args:
            condition: name condition of novelty
        """
        Label(By.XPATH, self.__CONDITION_LOCATOR % condition, ' %s Condition' % condition).click()

    def select_sort_results(self, sort_value_name='Featured'):
        """
        Select sort condition
        Args:
            sort_value_name: sort name
        """
        self.__SORT_DROPDOWN.select_option_by_visible_text(text=sort_value_name)

    def select_amazon_global_store(self):
        """
        Select Amazon global store
        """
        CheckBox(By.XPATH, self.__CHECKBOX_CONDITION % 'Amazon Global Store',
                 'Amazon Global Store language condition').click()

    def get_order_names_in_list(self):
        """
        Get order names from result page
        Returns:
            list of order names
        """
        WaitUtils.presence_of_element(element=self.__PAGINATION)
        order_names = Label(type=By.XPATH, locator=self.__ORDER_NAMES_LOCATOR, name='Orders').get_list_elements()
        return [i.text for i in order_names]

    def select_random_order(self):
        """
        Select random order
        Returns:
            random order element from result page
        """
        WaitUtils.presence_of_element(element=self.__PAGINATION)
        order_names = Label(type=By.XPATH, locator=self.__ORDER_NAMES_LOCATOR, name='Orders').get_list_elements()
        return random.choice(order_names)

    def open_order(self, order):
        """
        Click on order. Open order info page
        Args:
            order: order element
        """
        order.click()
