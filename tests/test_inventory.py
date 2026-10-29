import allure
from playwright.sync_api import Page, expect
from pages.cart_page import CartPage


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

  @allure.story("Multiple Items")
  @allure.title("Verify multiple items can be added to the cart")
  def test_multiple_items_in_cart(self, page: Page, logged_in_user):
   inventory_page = logged_in_user
   cart_page = CartPage(page)

   with allure.step("Add backpack and bike light to cart"):
    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_labs_to_cart()
   with allure.step("Navigate to the cart page"):
    inventory_page.go_to_cart()
   with allure.step("Verify both items are present in the cart"):
    expect(cart_page.cart_items).to_have_count(2)

  @allure.story("Sorting of Items")
  @allure.title("Verify multiple items can be sorted")
  def test_sorting_of_items(self, page: Page, logged_in_user):
   inventory_page = logged_in_user
   with allure.step("Click of the sorting dropdown"):
    inventory_page.sorting_dropdown_click()
   with allure.step("Select sorting price 'high to low' "):
    inventory_page.select_sorting("hilo")
   with allure.step("Verify the first item price is highest ($49.99)"):
    expect(inventory_page.item_price.first).to_have_text("$49.99")

  @allure.story("Navigation")
  @allure.title("Verify returting from item details  back to inventory page")
  def test_back_to_products_from_item_details(self, page: Page, logged_in_user):
   inventory_page = logged_in_user
   cart_page = logged_in_user
   with allure.step("Open the first item details page"):
    inventory_page.cart_item_name.click()
   with allure.step("Click the button 'Back to products' from the cart page"):
    cart_page.click_back_to_products()
   with allure.step("Verify we are back to inventory page"):
    expect(inventory_page.page_title).to_have_text("Products")
   

   
