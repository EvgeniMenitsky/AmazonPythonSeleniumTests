from src.framework.BaseEntity import BaseEntity


class BaseElement(BaseEntity):
    """
    Base class to describe elements actions
    """

    def __init__(self, type, locator, name):
        super().__init__(type, locator, name)

    def click(self):
        """
        Click on element
        """
        self.get_element().click()

    def right_click(self):
        """
        Right click on elemetn
        """
        pass

    def get_text(self):
        """
        Get text from elemet
        Returns:
            string - element text
        """
        return self.get_element().text

    def hover(self):
        """
        Mouse hover on element
        """
        pass

    def is_selected(self):
        """
        Check is selected element or not
        Returns:
            bool - select state
        """
        return self.get_element().is_selected()

    def is_displayed(self):
        """
        Check is displayed element or not
        Returns:
            bool - display state
        """
        return self.get_element().is_displayed()
