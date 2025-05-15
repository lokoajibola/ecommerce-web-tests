import pytest
import time
import allure
from selenium import webdriver
from pages.login_page import LoginPage
# from ecommerce_web_tests.pages.login_page import LoginPage  # Assuming your package is named 'ecommerce'
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Automatically download and install matching chromedriver


@pytest.fixture
def driver():
    chromedriver_autoinstaller.install()

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@allure.title("Invalid Login Test")
@allure.description("Tests login with invalid credentials.")
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("invalid_user", "wrong_password")
    error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Username and password do not match" in error
    print("Invalid login test passed!")


@allure.title("E-Commerce Flow Test")
@allure.description("Tests login and adding an item to the cart on SauceDemo.")
def test_ecommerce_flow(driver):
    wait = WebDriverWait(driver, 20)
    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    try:
        assert wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), "Products"))
    except AssertionError:
        driver.save_screenshot("error.png")
        raise

    # Add item to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()
    time.sleep(20)
    try:
        assert wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cart_quantity"), "2"))
    except AssertionError:
        allure.attach(driver.get_screenshot_as_png(), name="cart_error", attachment_type=allure.attachment_type.PNG)
    raise
    # assert driver.find_element(By.XPATH, "//div[contains(@class, 'cart_quantity')]").text == "1"
    print("E-commerce flow test passed!")
