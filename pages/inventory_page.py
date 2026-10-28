from playwright.sync_api import Page
from pages.base_page import BasePage

class InventoryPage(BasePage):
  def __init__(self, page):
    super().__init__(page)

    self.page_title = page.locator(".title")
    self.shopping_cart_icon = page.locator(".shopping_cart_link")
    self.add_to_cart_backpack_button = page.locator("#add-to-cart-sauce-labs-backpack")
    self.cart_badge = page.locator(".shopping_cart_badge")
    self.add_to_cart_bike_light = page.locator("#add-to-cart-sauce-labs-bike-light")
    self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
    self.item_price = page.locator('[data-test="inventory-item-price"]')

  def add_backpack_to_cart(self):
    self.add_to_cart_backpack_button.click()

  def add_bike_labs_to_cart(self):
    self.add_to_cart_bike_light.click()

  def go_to_cart(self):
    self.shopping_cart_icon.click()

  def sorting_dropdown_click(self):
    self.sort_dropdown.click()

  def select_sorting(self, option_value : str):
    self.sort_dropdown.select_option(option_value)

 
  



