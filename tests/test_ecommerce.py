import pytest
from selenium import webdriver
# from ..pages.login_page import LoginPage
from ecommerce_web_tests.pages.login_page import LoginPage  # Assuming your package is named 'ecommerce'
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_ecommerce_flow(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

    # Add item to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()
    assert driver.find_element(By.CLASS_NAME, "cart_quantity").text == "1"
    print("E-commerce flow test passed!")
