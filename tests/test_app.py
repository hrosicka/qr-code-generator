# This file contains Playwright tests for a simple calculator web application.
"""
Performs the calculation based on the initialized numbers and operation.
pytest --snapshot-update
"""

import pytest
from playwright.sync_api import Page

BASE_URL = "http://127.0.0.1:5000"

def test_generator_layout(page: Page, snapshot):
    """Test the initial layout of the QR code generator homepage."""
    # Navigate to the homepage of the QR code generator
    page.goto(BASE_URL)
    screenshot = page.screenshot()
    snapshot.assert_match(screenshot, "generator_initial_layout.png")

def test_homepage_contains_form(page: Page):
    """Test if the homepage contains the form for QR code generation."""
    # Navigate to the homepage of the QR code generator
    page.goto(BASE_URL)
    # Check if the title is correct and the form is present
    assert page.title() == "QR Code Generator"
    assert page.locator("form input[name='url']").is_visible()

def test_qr_generation(page: Page):
    """Test if the QR code is generated correctly when a URL is submitted."""
    # Navigate to the homepage of the QR code generator
    page.goto(BASE_URL)
    # Fill the form with a URL and submit it
    page.fill("input[name='url']", "https://example.com")
    # Submit the form
    page.click("button[type='submit']")
    # Wait for the QR code image to be generated and displayed
    assert page.locator("img").is_visible()

def test_qr_image_src_is_data_url(page: Page):
    """Test if the QR code image source is a data URL."""
    page.goto(BASE_URL)
    # Fill the form with a URL and submit it
    page.fill("input[name='url']", "https://example.com")
    # Submit the form
    page.click("button[type='submit']")
    # Wait for the QR code image to be generated
    page.wait_for_selector("img")
    # Check if the image is visible and its source is a data URL
    img = page.locator("img")
    assert img.is_visible()
    # Verify that the image source starts with "data:image/png"
    src = img.get_attribute("src")
    assert src.startswith("data:image/png")