from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_contains_products_title(page: Page):
  login_page = LoginPage(page)
  inventory_page = InventoryPage(page)

  login_page.open("https://www.saucedemo.com/")
  login_page.login("standard_user", "secret_sauce")

  expect(inventory_page.page_title).to_have_text("Products")
  expect(inventory_page.shopping_cart_icon).to_be_visible()

def test_add_item_to_cart(page: Page):
  login_page = LoginPage(page)
  inventory_page = InventoryPage(page)

  login_page.open("https://www.saucedemo.com/")
  login_page.login("standard_user", "secret_sauce")

  inventory_page.add_backpack_to_cart()
  expect(inventory_page.cart_badge).to_be_visible()
  expect(inventory_page.cart_badge).to_have_text('1')