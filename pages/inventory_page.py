from pages.locators import InventoryLocators


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = InventoryLocators.ADD_TO_CART_BUTTON
        self.cart_link = InventoryLocators.CART_LINK

    def add_item_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()