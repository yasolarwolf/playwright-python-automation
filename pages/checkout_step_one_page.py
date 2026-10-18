from playwright.sync_api import Page
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):
  def __init__(self, page):
    super().__init__(page)

    self.first_name_input = page.locator("#first-name")
    self.last_name_input = page.locator("#last-name")
    self.postal_code_input = page.locator("#postal-code")
    self.continue_button = page.locator("#continue")

  def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
    self.first_name_input.fill(first_name)
    self.last_name_input.fill(last_name)
    self.postal_code_input.fill(postal_code)
    self.continue_button.click()