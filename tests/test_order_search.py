from src.framework.BaseTest import BaseTest
from src.pages.forms.SearchForm import SearchForm
from src.pages.SearchResultPage import SearchResultPage
import pytest


class TestSearchOrder(BaseTest):
    @pytest.mark.parametrize("category_name,order_name, lang, condition, sort_name",
                             [("Books", "The Great Gatsby", "English", "New", "Price: Low to High"),
                              ("Computers", "Macbook pro", "English", "New", "Price: Low to High")])
    def test_search_order(self, category_name, order_name, lang, condition, sort_name):
        self.logger.log_step(1, 'Search Order')
        search_form = SearchForm()
        search_form.select_order_category(category_name=category_name)
        search_form.search_order_by_name(order_name=order_name)

        self.logger.log_step(2, 'Customise results')
        results_page = SearchResultPage()
        results_page.select_language(language=lang)
        results_page.select_condition(condition=condition)
        results_page.select_sort_results(sort_value_name=sort_name)

        self.logger.log_step(3, 'Check Results')
        results = results_page.get_order_names_in_list()
        assert False not in [order_name in order for order in
                             results], "List has not relevant results! - %s" % [order for order in results if
                                                                                order_name not in order]
