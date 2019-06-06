from src.framework.elements.BaseElement import BaseElement
from selenium.webdriver.support.ui import Select


class Dropdown(BaseElement):
    """Class for Dropdown element actions"""

    def __init__(self, type, locator, name):
        super().__init__(type, locator, name)

    def get_select(self):
        """
        Return selected element
        Returns:
            Dropdown - selected element
        """
        return Select(self.get_element())

    def select_option_by_visible_text(self, text):
        """
        Select option by text
        Args:
            text: text of option
        """
        select = self.get_select()
        select.select_by_visible_text(text)

    def select_option_by_index(self, index):
        """
        Select option by index
        Args:
            index: index of option
        """
        select = self.get_select()
        select.select_by_index(index)

    def select_option_by_value(self, value):
        """
        Select option by value
        Args:
            value: value tag
        """
        select = self.get_select()
        select.select_by_value(value)

    def get_selected(self):
        """
        Get all selection option(s)
        Returns:
            selected option(s)
        """
        if self.get_select().all_selected_options > 1:
            return self.get_select().all_selected_options
        else:
            return self.get_select().first_selected_option
