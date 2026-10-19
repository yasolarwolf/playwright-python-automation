import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.fixture
def logged_in_user(page: Page):
  login_page = LoginPage(page)
  inventory_page = InventoryPage(page)

  login_page.open("https://www.saucedemo.com/")
  login_page.login("standard_user", "secret_sauce")

  return inventory_page

@pytest.fixture
def cart_with_item(page: Page, logged_in_user):
  inventory_page = logged_in_user
  cart_page = CartPage(page)

  inventory_page.add_backpack_to_cart()
  inventory_page.go_to_cart()

  return cart_page
