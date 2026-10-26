from playwright.sync_api import Page
from pages.base_page import BasePage

class CartPage(BasePage):
  def __init__(self, page):
    super().__init__(page)

    self.page_title = page.locator(".title")
    self.cart_item_name = page.locator(".inventory_item_name")
    self.checkout_button = page.locator("#checkout")
    self.remove_backpack_button = page.locator('[data-test="remove-sauce-labs-backpack"]')
    self.cart_items = page.locator(".cart_item")
    self.continue_shopping_button = page.locator ("#continue-shopping")

  def click_checkout(self):
    self.checkout_button.click()  

  def remove_backpack_from_cart(self):
    self.remove_backpack_button.click()

  def click_continue_shopping(self):
    self.continue_shopping_button.click()
