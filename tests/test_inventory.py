import allure
from playwright.sync_api import Page, expect


@allure.epic("Saucedemo Testing")
@allure.feature("Inventory Testing")

class TestInventory:

  @allure.story("Catalog Display")
  @allure.title("Verify inventory page title and shopping cart icon  are visible")
  def test_inventory_contains_products_title(self, page: Page, logged_in_user):
    
    inventory_page = logged_in_user

    with allure.step("Verify inventory page title shows 'Products'"):
     expect(inventory_page.page_title).to_have_text("Products")

    with allure.step("Verify shopping cart icon is visible"):
     expect(inventory_page.shopping_cart_icon).to_be_visible()

  @allure.story("Add Item to Cart")
  @allure.title("Verify adding an item to the cart updates the cart badge")
  def test_add_item_to_cart(self, page: Page, logged_in_user):
    
    inventory_page = logged_in_user

    with allure.step("Add backpack ti the card from inventory page"):
     inventory_page.add_backpack_to_cart()

    with allure.step("Verify cart badge is visible and distpays count '1'"):
     expect(inventory_page.cart_badge).to_be_visible()
     expect(inventory_page.cart_badge).to_have_text('1')