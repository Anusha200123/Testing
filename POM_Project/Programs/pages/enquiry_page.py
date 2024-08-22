from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self,driver):
        self.driver = driver
        self.product_link =(By.LINK_TEXT,"Products")
        self.enquiry =(By.XPATH,"//button[text()='Add to Enquiry']")
        self.quantity_input =(By.XPATH,"//input[@placeholder='Quantity in Mg*']")
        self.add_button =(By.XPATH,"//span[text()='Add']")
        self.screenshot_path =r"C:\screenshots\Enquiry.png"

    def navigate_to_product_page(self):
        self.driver.find_element(*self.product_link).click()
    def add_product_to_enquiry(self):
        element = self.driver.find_element(*self.enquiry)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
    def enter_quantity(self,quantity):
        self.driver.find_element(*self.quantity_input).send_keys(quantity)
    def submit_enquiry(self):
        self.driver.find_element(*self.add_button).click()
    def take_screenshot(self):
        self.driver.save_screenshot(self.screenshot_path)
    def refresh_page(self):
        self.driver.refresh()