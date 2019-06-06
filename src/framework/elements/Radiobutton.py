from src.framework.elements.BaseElement import BaseElement


class Radiobutton(BaseElement):
    """Class for Button element actions"""

    def __init__(self, type, locator, name):
        super().__init__(type, locator, name)

    def get_state(self):
        """
        Get radiobutton state
        Returns:
            radiobutton state: check/uncheck
        """
        return self.get_element().get_attribute("value")
