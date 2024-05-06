from playwright.sync_api import Page
import allure


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    base_url = 'https://magento.softwaretestingboard.com/'
    rel_url = None

    @allure.step('Open page')
    def visit_page(self):
        if self.rel_url:
            self.page.goto(f'{self.base_url}{self.rel_url}', timeout=0)
        else:
            raise Exception('No rel_url given')

    def find(self, locator):
        return self.page.locator(locator)
