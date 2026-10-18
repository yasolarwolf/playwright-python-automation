from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_item_is_present_in_cart(page: Page):
  login_page = LoginPage(page)
  inventory_page = InventoryPage(page)
  cart_page = CartPage(page)

  login_page.open("https://www.saucedemo.com/")
  login_page.login("standard_user", "secret_sauce")

  inventory_page.add_backpack_to_cart()

  inventory_page.go_to_cart()

  expect(cart_page.page_title).to_have_text("Your Cart")
  expect(cart_page.cart_item_name).to_have_text("Sauce Labs Backpack")