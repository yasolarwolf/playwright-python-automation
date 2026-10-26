import allure
from playwright.sync_api import Page, expect
from pages.cart_page import CartPage

@allure.epic("Saucedemo Testing")
@allure.feature("Cart Functionality")

class TestCart:

  @allure.story("Add Item to Сart")
  @allure.title("Verify item is present in the cart after adding from inventory")
  def test_item_is_present_in_cart(self, page: Page, logged_in_user):
    inventory_page = logged_in_user
    cart_page = CartPage(page)

    with allure.step("Add backpack to card from inventory page"):
     inventory_page.add_backpack_to_cart()

    with allure.step("Navigate to the cart page"):
     inventory_page.go_to_cart()

    with allure.step("Verify cart title and item name in the cart"):
     expect(cart_page.page_title).to_have_text("Your Cart")
     expect(cart_page.cart_item_name).to_have_text("Sauce Labs Backpack")

  @allure.story("Remove Item from Cart")
  @allure.title("Verify item can be removed from the cart")
  def test_remove_item_from_cart(self, page: Page, cart_with_item):
    cart_page = cart_with_item

    with allure.step("Remove backpack from the cart"):
     cart_page.remove_backpack_from_cart()

    with allure.step("Verify that cart is empty"):
     expect(cart_page.cart_items).to_be_hidden()

  @allure.story("Checkout Process")
  @allure.title("Verify navigation from cart to checkout step one")
  def test_proceed_to_checkout_from_card(self, page: Page, cart_with_item):
    cart_page = cart_with_item

    with allure.step("Click checkout button in the cart"):
     cart_page.click_checkout()

    with allure.step("Verify redirection to checkout step one"):
     expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

  @allure.story("Cart Navigation")
  @allure.title("Verify user can return to inventory via 'Continue shopping' button")
  def test_continue_shopping_from_cart(self, page: Page, cart_with_item):
   cart_page = cart_with_item
   with allure.step("Click continue shopping button"):
    cart_page.click_continue_shopping()
   with allure.step("Verify redirection back to inventory page"):
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

  
    

