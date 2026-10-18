from playwright.sync_api import Page
from pages.base_page import BasePage

class InventoryPage(BasePage):
  def __init__(self, page):
    super().__init__(page)

    self.page_title = page.locator(".title")
    self.shopping_cart_icon = page.locator(".shopping_cart_link")
    self.add_to_cart_backpack_button = page.locator("#add-to-cart-sauce-labs-backpack")
    self.cart_badge = page.locator(".shopping_cart_badge")

  def add_backpack_to_cart(self):
    self.add_to_cart_backpack_button.click()



