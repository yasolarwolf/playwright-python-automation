from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page):
  login_page = LoginPage(page)
  login_page.open("https://www.saucedemo.com/")
  login_page.login("standard_user", "secret_sauce")

  expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_login(page: Page):
  login_page = LoginPage(page)
  login_page.open("https://www.saucedemo.com/")
  login_page.login("standard_user", "wrong_sauce1")

  expect(login_page.error_message).to_be_visible()
  expect(login_page.error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")

