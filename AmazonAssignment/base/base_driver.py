import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver():

    def __init__(self, driver):
        self.driver = driver


    # List of all generic methods which are most commonly used


    def page_scroll(self):
        # scrolling page dynamically using javascript executor
        pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength = document.body.scrollHeight")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            pageLength = self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var pageLength = document.body.scrollHeight")
            if lastCount == pageLength:
                match = True
        time.sleep(2)


    def wait_for_presence_of_all_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        direct_flights_count = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return  direct_flights_count


    def wait_for_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return elements
