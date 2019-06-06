from src.framework.elements.BaseElement import BaseElement


class Button(BaseElement):
    """Class for Button element actions"""

    def __init__(self, type, locator, name):
        super().__init__(type, locator, name)
