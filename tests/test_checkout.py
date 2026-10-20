import allure
from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage

@allure.epic("Saucedemo Testing")
@allure.feature("Checkout Workflow")
@allure.story("Complele End-to-End Purchase")
@allure.title("Verify sucessfull complete checkout flow from inventory to order confirmation")
class TestCheckout:

  def test_complete_checkout(self, page: Page, logged_in_user ):
    inventory_page = logged_in_user
    cart_page = CartPage(page)
    checkout_one_page = CheckoutStepOnePage(page)
    checkout_two_page = CheckoutStepTwoPage(page)

    with allure.step("Add backpack to cart and navigate to the cart page"):
     inventory_page.add_backpack_to_cart()
     inventory_page.go_to_cart()

    with allure.step("Fill in personal information on checkout step one"):
     cart_page.click_checkout()
    checkout_one_page.fill_checkout_info("John", "Morgan", "15344")

    with allure.step("Finish checkout on checkout step two"):
     checkout_two_page.finish_checkout()

    with allure.step("Verify that the order completion header shows 'Thankyou for your order!'"):
     expect(checkout_two_page.complete_header).to_have_text("Thank you for your order!")
