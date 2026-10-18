from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage

def test_complete_checkout(page: Page):
  login_page = LoginPage(page)
  inventory_page = InventoryPage(page)
  cart_page = CartPage(page)
  checkout_one_page = CheckoutStepOnePage(page)
  checkout_two_page = CheckoutStepTwoPage(page)

  login_page.open("https://www.saucedemo.com/")
  login_page.login("standard_user", "secret_sauce")

  inventory_page.add_backpack_to_cart()
  inventory_page.go_to_cart()

  cart_page.click_checkout()
  checkout_one_page.fill_checkout_info("John", "Morgan", "15344")
  checkout_two_page.finish_checkout()

  expect(checkout_two_page.complete_header).to_have_text("Thank you for your order!")
