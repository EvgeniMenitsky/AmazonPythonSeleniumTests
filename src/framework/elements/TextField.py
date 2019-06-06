from src.framework.elements.BaseElement import BaseElement


class TextField(BaseElement):
    """Class for TextField element actions"""

    def __init__(self, type, locator, name):
        super().__init__(type, locator, name)

    def set_text(self, text):
        """
        Set text to textfield
        Args:
            text: string text
        """
        self.get_element().send_keys(text)

    def get_text(self):
        """
        Get current text into textfield
        Returns:
            string: text into textfield
        """
        return self.get_element().text

    def clear(self):
        """
        Clear text into textfield
        """
        return self.get_element().clear()
