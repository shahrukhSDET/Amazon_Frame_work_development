import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from pages.product_buying_page import Product_page


class HomePage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS----------------------

    SEARCH_FIELD = "//input[@id='twotabsearchtextbox']"
    BUTTON = "//input[@id='nav-search-submit-button']"
    PRODUCT_URL = "//a[text()='Aurélien Géron']/parent::div/parent::div/preceding-sibling::h2/parent::div"

    def Getsearchfield(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.SEARCH_FIELD)

    def Getbutton_click(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.BUTTON)

    def Getproduct_url(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.PRODUCT_URL)


    def enter_product_details(self, product):
        self.Getsearchfield().click()
        self.Getsearchfield().send_keys(product)
        time.sleep(3)
        self.Getbutton_click().click()
        time.sleep(3)

    def enter_select_required_product(self):
        self.Getproduct_url().click()
        time.sleep(3)


    """Wrapping up  all the above methods of the class in single method and also created object of Product_page at 
    trigger point(i.e at the linkage of the two pages of same application)"""

    def search_product(self, product):
        self.enter_product_details(product)
        self.enter_select_required_product()
        product_buying = Product_page(self.driver)
        return product_buying


