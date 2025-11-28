# Import Page class from Playwright sync API for typing and features
from playwright.sync_api import Page, expect


# BasePage = parent class for all page objects (LoginPage, HomePage, etc.)
class BasePage:

    # Constructor that receives the Playwright page instance
    def __init__(self, page: Page):
        # Save the page object so all methods inside this class can use it
        self.page = page

    # Reusable method to navigate to any URL
    def goto(self, url: str):
        # Playwright loads the provided URL
        self.page.goto(url)

    # Reusable click wrapper
    def click(self, locator: str):
        # Clicks on the element located by 'locator'
        self.page.click(locator)

    # Reusable text fill function
    def fill(self, locator: str, value: str):
        # Enters the value inside the textbox represented by locator
        self.page.fill(locator, value)

    # Reusable function to get visible text of any element
    def get_text(self, locator: str):
        # Return visible string from the element
        return self.page.text_content(locator)

    # Wait until element appears
    def wait_for_element(self, locator: str):
        # Playwright waits until selector is found in DOM
        self.page.wait_for_selector(locator)

    # Check if element is visible on screen
    def is_visible(self, locator: str):
        # Returns True/False based on visibility
        return self.page.locator(locator).is_visible()

    # Capture screenshot utility
    def take_screenshot(self, path: str):
        # Saves the screenshot to provided path
        self.page.screenshot(path=path)
