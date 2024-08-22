import time

import pytest
from selenium import webdriver
from Programs.pages.prgm_1 import product_tab
from Programs.pages.prgm_1 import product_detail
from Programs.pages.home_page import PageElements
from Programs.pages.prod_detail import ChemicalPage
from Programs.pages.enquiry_page import ProductPage

#Go to Bio-Organics UI and Go to products page, confirm that your on  product page
def test_first_case(setup,base_url):
    driver = setup
    product = product_tab(driver)
    product.click_product()
    time.sleep(5)
    expected_url = f"{base_url}/products"
    current_title = driver.current_url
    print(current_title)
    assert expected_url == current_title, "You are not in the Product Page"
    print("You are on the Product page")

#On product page, click on one product detail get print details of it. Repeat it with using different locator with different product. Locators to be used : Id, Name, ClassName, Tag-Name, linktext, partiallinktext, Css Selector and Xpath
def test_chemical_components_detail(prod_setup):
    driver = prod_setup
    prod_info = ChemicalPage(driver)
    product_det = product_detail(driver)
    product_det.prod_button_click()
    time.sleep(3)
    details_text = {
        "Synonym": prod_info.get_synonym(),
        "CAS Number": prod_info.get_cas_number(),
        "CAT Number": prod_info.get_cat_number(),
        "Formula": prod_info.get_formula(),
        "Weight": prod_info.get_weight(),
        "Purity": prod_info.get_purity(),
        "Storage Condition": prod_info.get_condition()
    }
    for key, value in details_text.items():
        print(f"{key}:{value}")



#On product page, click on one product detail it has to open it new tab, print the url of new tab and close it.
def test_third_case(setup, driver):
    driver = setup
    open_new_tab = product_tab(driver)
    open_new_tab.click_product()
    element = open_new_tab.get_product_element()
    driver.execute_script("window.open(arguments[0].href, '_blank');", element)
    new_tab = driver.window_handles[-1]
    driver.switch_to.window(new_tab)
    time.sleep(5)
    print(driver.current_url)
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print(driver.title)


#Go to Bio-Organics web site >> Go to products >> Add enquiry >> Take screen shot and store >> Close the browser tab
def test_product_enquiry(navigate,base_url,driver):
    navigate(f"{base_url}/")
    prod_page = ProductPage(driver)
    prod_page.navigate_to_product_page()
    prod_page.add_product_to_enquiry()
    prod_page.enter_quantity(4)
    prod_page.submit_enquiry()
    time.sleep(3)
    prod_page.take_screenshot()
    prod_page.refresh_page()
    time.sleep(3)

def test_validation_positive(navigate,base_url,driver):

    navigate(f"{base_url}/products")
    expected_url =(f"{base_url}/products")
    current_url =driver.current_url
    assert expected_url == current_url ,"You are currently not in the Product Page"


#demonstration of all assertion types
def test_assert_Equal(prod_setup):
    driver = prod_setup
    prod_detail1 = product_detail(driver)
    expected_name= "A-Factor"
    prod_detail1.prod_button_click()
    time.sleep(3)
    actual_name = prod_detail1.get_prod_name()
    assert actual_name == expected_name
    print("Chemical name is same ")

def test_assert_NotEqual(prod_setup):
    driver = prod_setup
    prod_detail2 = product_detail(driver)
    expected_name = "AB-Factor"
    prod_detail2.prod_button_click()
    time.sleep(3)
    actual_name = prod_detail2.get_prod_name()
    assert actual_name != expected_name, "Chemical name is not matching"

def test_assert_true(prod_setup):
    driver = prod_setup
    prod_detail3 = product_detail(driver)
    expected_name = "A-Factor"
    prod_detail3.prod_button_click()
    time.sleep(3)
    actual_name = prod_detail3.get_prod_name()
    if actual_name == expected_name:
        assert True

def test_assert_false(prod_setup):
    driver = prod_setup
    prod_detail4 = product_detail(driver)
    expected_name = "A-Factor"
    prod_detail4.prod_button_click()
    time.sleep(3)
    actual_name = prod_detail4.get_prod_name()
    if actual_name != expected_name:
        assert False

def test_assert_In():
    expected_name = "A-Factor"
    assert ("Factor" in expected_name)

def test_assert_Not_In():
    expected_name = "A-Factor"
    assert ("AB-Factor" not in expected_name)

#Automate 5 testcases of your own for Home, Corporate, Services, contact and Products pages one testcase for each page of Bio Organics Application using page object model and Pytest framework

def test_all_pages(driver,navigate,base_url):
    # Test Home Page

    navigate(f"{base_url}/")
    home = PageElements(driver)
    driver.implicitly_wait(5)
    expected_text_home = home.get_latest_product_text()
    actual_text_home = "Latest Products"
    assert expected_text_home in actual_text_home, "Home page text does not match"
    print("Home page text matches expected value")

    # Test Corporate Page

    navigate(f"{base_url}/corporate")
    corporate = PageElements(driver)
    expected_text_corporate = corporate.get_promise_card_text()
    actual_name_corporate = "Confidentiality"
    assert expected_text_corporate == actual_name_corporate, "Corporate page text does not match"
    print("Corporate page text matches expected value")

    # Test Service Page

    navigate(f"{base_url}/services")
    service = PageElements(driver)
    title = service.query_title()
    og_title = "Have any queries? Write to us"
    assert title in og_title, "Service page title does not match"
    print("Service page title matches expected value")

    # Test Product Page
    navigate(f"{base_url}/products")
    product = PageElements(driver)
    expected_title_product = product.Pname()
    actual_title_product = "A-Factor"
    assert expected_title_product == actual_title_product, "Product page title does not match"
    print("Product page title matches expected value")

    # Test Contact Page
    navigate(f"{base_url}/contact")
    contact = PageElements(driver)
    time.sleep(4)
    expected_result_contact = contact.locate_location()
    actual_result_contact = "Location"
    assert expected_result_contact == actual_result_contact, "Contact page location does not match"
    print("Contact page location matches expected value")
















