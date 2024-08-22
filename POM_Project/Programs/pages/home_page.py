from selenium.webdriver.common.by import By


class PageElements:
    def __init__(self,driver):
        self.driver = driver
        self.latest_product = (By.CSS_SELECTOR,".h22")
        self.promise_card = (By.CSS_SELECTOR, ".promise-card-title")
        self.title = (By.CSS_SELECTOR, ".form-text-div")
        self.product_name = (By.XPATH, "//span[starts-with(text(),'A-Factor')]")
        self.location = (By.XPATH, "//p[contains(text(),'Location')]")

    def get_text(self):
        return self.driver.find_element(*self.latest_product).text


    def get_latest_product_text(self):
        return self.driver.find_element(*self.latest_product).text

    def get_promise_card_text(self):
        return self.driver.find_element(*self.promise_card).text


    def query_title(self):
        return self.driver.find_element(*self.title).text


    def Pname(self):
        return self.driver.find_element(*self.product_name).text


    def locate_location(self):
        return self.driver.find_element(*self.location).text
