from src.framework.BaseTest import BaseTest
from src.pages.forms.SearchForm import SearchForm
from src.pages.forms.MainMenuForm import MainMenuForm
from src.pages.SearchResultPage import SearchResultPage
from src.pages.OrderPage import OrderPage
from src.pages.CartPage import CartPage
from src.models.Order import Order
import pytest


class TestShopCart(BaseTest):
    def test_put_order_to_shopcart(self):
        self.logger.log_step(1, 'Search Order')
        search_form = SearchForm()
        search_form.select_order_category(category_name='Books')
        search_form.search_order_by_name(order_name='Harry Potter')

        self.logger.log_step(2, 'Open random order from result')
        results_page = SearchResultPage()
        results_page.select_amazon_global_store()
        random_order = results_page.select_random_order()
        results_page.open_order(order=random_order)

        self.logger.log_step(3, 'Save order data')
        orderPage = OrderPage()
        order = Order(name=orderPage.get_order_name(), price=orderPage.get_order_price())
        orderPage.add_order_to_cart()

        self.logger.log_step(4, 'Check order in order cart')
        mainMenuForm = MainMenuForm()
        mainMenuForm.open_cart()
        cardPage = CartPage()
        order_on_cart = cardPage.search_order_by_name(order_name=order.get_name())
        assert order == order_on_cart
