from playwright.sync_api import Page
from pages.base_page import BasePage

class CheckoutStepTwoPage(BasePage):
  def __init__(self, page):
    super().__init__(page)

    self.finish_button = page.locator("#finish")
    self.complete_header = page.locator('[data-test="complete-header"]')

  def finish_checkout(self):
    self.finish_button.click()