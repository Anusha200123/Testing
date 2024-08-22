import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class product_tab:
    def __init__(self,driver):
        self.driver = driver
        self.product_link =(By.LINK_TEXT,"Products")

    def click_product(self):
        self.driver.find_element(*self.product_link).click()

    def get_product_element(self):
        return self.driver.find_element(*self.product_link)


class product_detail:
    def __init__(self,driver):
        self.driver = driver
        time.sleep(3)
        self.prod_button =(By.XPATH,"//button[@class='product-button']")
        time.sleep(3)
        self.prod_name = (By.TAG_NAME,"h1")

    def prod_button_click(self):
        return self.driver.find_element(*self.prod_button).click()

    def get_prod_name(self):
        return self.driver.find_element(*self.prod_name).text
