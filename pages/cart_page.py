from playwright.sync_api import Page
from pages.base_page import BasePage

class CartPage(BasePage):
  def __init__(self, page):
    super().__init__(page)

    self.page_title = page.locator(".title")
    self.cart_item_name = page.locator(".inventory_item_name")
    self.checkout_button = page.locator("#checkout")

    
