from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_item_is_present_in_cart(page: Page, logged_in_user):
  
  inventory_page = logged_in_user
  cart_page = CartPage(page)

  inventory_page.add_backpack_to_cart()
  inventory_page.go_to_cart()

  expect(cart_page.page_title).to_have_text("Your Cart")
  expect(cart_page.cart_item_name).to_have_text("Sauce Labs Backpack")

def test_remove_item_from_cart(page: Page, cart_with_item):
  cart_page = cart_with_item
  cart_page.remove_backpack_from_cart()

  expect(cart_page.cart_items).to_be_hidden()

def test_proceed_to_checkout_from_card(page: Page, cart_with_item):
  cart_page = cart_with_item
  cart_page.click_checkout()
  expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

