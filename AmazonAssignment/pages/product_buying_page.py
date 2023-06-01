import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class Product_page(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS-----------------------
    ADD_TO_CART_BUTTON = "//span[text()='Add to Cart']/preceding-sibling::input"

    def Get_add_to_cart(self):
        return self.wait_for_element_to_be_clickable(By.XPATH, self.ADD_TO_CART_BUTTON)



    def enter_add_product_to_cart(self):
        self.Get_add_to_cart().click()
        time.sleep(2)



