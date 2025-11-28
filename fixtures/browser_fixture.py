# Import pytest to create fixtures
import pytest

# Import Playwright sync API to launch the browser
from playwright.sync_api import sync_playwright


# Fixture responsible for launching browser and returning a page object
@pytest.fixture()
def setup():
    # Start Playwright in synchronous mode
    with sync_playwright() as p:

        # Launch Chromium browser (visible window because headless=False)
        browser = p.chromium.launch(headless=False)

        # Create a new isolated browser context (like a new clean browser profile)
        context = browser.new_context()

        # Open a fresh page (tab) inside this context
        page = context.new_page()

        # Yield keyword returns the page to the test function
        yield page

        # After the test completes, close the browser context
        context.close()

        # Close the browser instance
        browser.close()
