from selenium.webdriver.common.by import By
from src.framework.BasePage import BasePage
from src.framework.elements.Label import Label
from src.models.Order import Order


class CartPage(BasePage):
    """
    Cart form
    """
    __ORDER_NAMES = "//div[@class='sc-list-item-content']//span[contains(@class,'product-title') and contains(text(),'%s')]"
    __ORDER_ELEM = __ORDER_NAMES + "/ancestor::div[contains(@class,'spacing-base')]"
    __ORDER_PRICE = __ORDER_ELEM + "//span[contains(@class,'sc-product-price')]"

    def __init__(self):
        super().__init__(type=By.ID, locator="sc-active-cart",
                         name='Cart Page')

    def search_order_by_name(self, order_name):
        """
        Search order by name
        Args:
            order_name:  order name

        Returns:
            found Order model
        """
        price = Label(By.XPATH, locator=self.__ORDER_PRICE % order_name, name='%s Price Label' % order_name[10] + '...')
        return Order(name=order_name, price=price.get_text())
