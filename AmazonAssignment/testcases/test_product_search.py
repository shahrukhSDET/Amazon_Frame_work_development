import time
import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class Test_search_product():


    def test_product_search_and_addtocart(self):

        home_page = HomePage(self.driver)
        product_buying = home_page.search_product("O'REILLY MACHINE LEARNING") #product-book_name
        home_page.page_scroll()
        window_handle = self.driver.window_handles
        self.driver.switch_to.window(window_handle[1])
        product_buying.enter_add_product_to_cart()


