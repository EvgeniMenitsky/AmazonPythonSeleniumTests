from src.framework.elements.BaseElement import BaseElement


class CheckBox(BaseElement):
    """Class for CheckBox element actions"""

    def __init__(self, type, locator, name):
        super().__init__(type, locator, name)
