import json
from playwright.sync_api import Page, expect, Route


def test_one(page: Page):
    def name_changer(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = "яблокофон 15 про"
        body = json.dumps(body)
        route.fulfill(response=response, body=body)

    page.route('**/shop/api/digital-mat?path=library/**', name_changer)
    page.goto('https://www.apple.com/shop/buy-iphone')
    card = page.locator('//h3[contains(text(), "iPhone 15 Pro")]')
    card.click()
    popup_title = page.locator("[data-autom='DigitalMat-overlay-header-0-0']")
    expect(popup_title).to_have_text('яблокофон 15 про')
