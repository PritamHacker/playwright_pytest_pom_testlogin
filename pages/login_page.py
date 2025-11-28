# Import Page class for typing and BasePage for inherited common methods
from playwright.sync_api import Page
from pages.base_page import BasePage


# LoginPage extends BasePage and contains login screen elements & actions
class LoginPage(BasePage):

    # Locators for the login page elements
    USERNAME_INPUT = "#user-name"            # Email textbox selector
    PASSWORD_INPUT = "#password"      # Password textbox selector
    LOGIN_BUTTON = "#login-button"        # Login button selector
    ERROR_MESSAGE = ".error-message-container"  # Error message selector

    # Constructor receives Playwright 'page'
    def __init__(self, page: Page):
        # Call BasePage constructor with the page object
        super().__init__(page)

    # Method to open login page using base URL from config.yaml
    def open_login_page(self, base_url: str):
        # Use BasePage.goto() to navigate to "<base_url>/login"
        self.goto(f"{base_url}")

    # Enter email into input field
    def enter_email(self, username: str):
        # Use BasePage.fill() to type email address
        self.fill(self.USERNAME_INPUT, username)

    # Enter password into input field
    def enter_password(self, password: str):
        # Fill password textbox
        self.fill(self.PASSWORD_INPUT, password)

    # Click login button
    def click_login_button(self):
        # Use BasePage.click() to click login button
        self.click(self.LOGIN_BUTTON)

    # Fetch error message text (for failed login)
    def get_error_message(self):
        # Return visible error message text
        return self.get_text(self.ERROR_MESSAGE)

    # Composite login method (steps combined)
    def login(self, username: str, password: str):
        # Step 1: enter email
        self.enter_email(username)
        # Step 2: enter password
        self.enter_password(password)
        # Step 3: click login button
        self.click_login_button()
