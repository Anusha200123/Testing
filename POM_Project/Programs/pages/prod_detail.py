from selenium.webdriver.common.by import By


class ChemicalPage:
    def __init__(self,driver):
        self.driver = driver

    def get_label_text(self,label_text):
        label = self.driver.find_element(By.XPATH, f"//span[text()='{label_text}']")
        parent_text = label.find_element(By.XPATH, "./parent::*").text
        return parent_text.split(":")[1].strip()

    def get_synonym(self):
        return self.get_label_text("Synonyms")
    def get_cas_number(self):
        return self.get_label_text("CAS Number")
    def get_cat_number(self):
        return self.get_label_text("CAT Number")
    def get_formula(self):
        return self.get_label_text("Molecular Formula")
    def get_weight(self):
        return self.get_label_text("Molecular Weight")
    def get_purity(self):
        return self.get_label_text(" Purity")
    def get_condition(self):
        return self.get_label_text("Storage Condition")