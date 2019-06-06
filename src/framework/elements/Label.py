from src.framework.elements.BaseElement import BaseElement


class Label(BaseElement):
    """Class for Button element actions"""

    def __init__(self, type, locator, name):
        super().__init__(type, locator, name)
