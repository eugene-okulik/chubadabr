import re

from playwright.sync_api import Page, expect, BrowserContext


def test_one(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm#')
    page.locator('//a[@href="#"]').click()
    result = page.locator('#result-text')
    expect(result).to_have_text('Ok')


def test_two(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    button = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        button.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(button).to_be_enabled()


def test_three(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    expect(button).to_have_class(re.compile('text-danger'))
    button.click()
