from selenium.webdriver.common.by import By
from src.framework.BasePage import BasePage
from src.framework.elements.Label import Label


class OrderPage(BasePage):
    """
    Order Info Page
    """
    __ORDER_NAME = Label(type=By.ID, locator='productTitle', name='Order Name Label')
    __ORDER_PRICE = Label(type=By.XPATH, locator="//div[@id='buyNewSection']//span[contains(@class, 'offer-price')]",
                          name='Order Price')
    __ADD_TO_CART_BUTTON = Label(type=By.ID, locator='add-to-cart-button', name='Add to Cart Button')

    def __init__(self):
        super().__init__(type=By.ID, locator="instantOrderUpdate_feature_div",
                         name='Order Page')

    def add_order_to_cart(self):
        """
        Click on Add order to cart button
        """
        self.__ADD_TO_CART_BUTTON.click()

    def get_order_name(self):
        """
        Get order name
        Returns:
            string: order name
        """
        return self.__ORDER_NAME.get_text()

    def get_order_price(self):
        """
        Get order price
        Returns:
            string: order price
        """
        return self.__ORDER_PRICE.get_text()
