import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@allure.epic("Saucedemo Testing")
@allure.feature("Login Testing")
class TestLogin:

  @allure.story("Sucessfull Login")
  @allure.title("Verify sucessfull login with valid credentials")
  def test_successful_login(self, page: Page):
    login_page = LoginPage(page)

    with allure.step("Open login page and autentificate with valid user"):
     login_page.open("https://www.saucedemo.com/")
     login_page.login("standard_user", "secret_sauce")

    with allure.step("Verify redirection to the inventory page"):
     expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

  @allure.story("Invalid Login")
  @allure.title("Verify error message then logging in with incorrect password")
  def test_invalid_login(self, page: Page):
    login_page = LoginPage(page)

    with allure.step("Open login page and enter invalid password"):
     login_page.open("https://www.saucedemo.com/")
     login_page.login("standard_user", "wrong_sauce1")

    with allure.step("Verify error message about mismatched credentials is visible"):
     expect(login_page.error_message).to_be_visible()
     expect(login_page.error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")

  @allure.story("Empty Credentials Login")
  @allure.title("Verify error message when submitting empty username and password")
  def test_empty_login(self, page: Page):
    login_page = LoginPage(page)

    with allure.step("Open login page and enter empty credentials"):
     login_page.open("https://www.saucedemo.com/")
     login_page.login("","")

    with allure.step("Verify that error message about required username is visible"):
     expect(login_page.error_message).to_be_visible()
     expect(login_page.error_message).to_contain_text("Epic sadface: Username is required")

  @allure.story("Locked Out User Login")
  @allure.title("Verify error message when submitting locked out user login")
  def test_locked_user_login(self, page: Page):
    login_page = LoginPage(page)

    with allure.step("Open login in and log in with locked out credentials"):
     login_page.open("https://www.saucedemo.com/")
     login_page.login("locked_out_user", "secret_sauce")

    with allure.step("Verify that error message about locked user is visible"):
     expect(login_page.error_message).to_be_visible()
     expect(login_page.error_message).to_contain_text("Epic sadface: Sorry, this user has been locked out")
