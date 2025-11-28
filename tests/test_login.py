# Import LoginPage so tests can use the POM object
import pytest
from pages.login_page import LoginPage


@pytest.fixture
# Test case for valid login
def test_valid_login(setup, config):
    # The 'setup' fixture returns a Playwright page instance
    page = setup

    # Create LoginPage object with the page instance
    login = LoginPage(page)

    # Open login page using base URL from config.yaml
    login.open_login_page(config["base_url"])

    # Perform login using valid credentials from config.yaml
    login.login(config["valid_user"]["email"], config["valid_user"]["password"])

    # Assertion: After successful login, the user should be redirected to /dashboard
    assert page.url.endswith("/inventory.html")


# Test case for invalid login attempt
def test_invalid_login(setup, config):
    # Setup fixture returns page instance
    page = setup

    # LoginPage object created for interacting with login elements
    login = LoginPage(page)

    # Open login page
    login.open_login_page(config["base_url"])

    # Try logging in with wrong credentials
    login.login("wrong@mail.com", "wrongpass")

    # Assertion: error message should contain text indicating invalid login
    assert "Epic sadface: Username and password do not match any user in this service" in login.get_error_message()
