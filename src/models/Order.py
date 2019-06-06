import re


class Order(object):
    """
    Amazon order model
    """

    def __init__(self, name, price):
        self.__name = name
        self.__price = float(re.search(r'\d+', price).group())

    def get_name(self):
        """
        Get order name
        Returns:
            string - order name
        """
        return self.__name

    def get_price(self):
        """
        Get order price
        Returns:
            float - order price without currency
        """
        return self.__price

    def __eq__(self, other):
        return self.__name == other and self.get_price() == other
