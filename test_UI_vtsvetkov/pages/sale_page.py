from pages.base_page import BasePage
from locators import sale_page_locs as loc
from playwright.sync_api import expect


class SalePage(BasePage):
    rel_url = 'sale.html'
    category_text = 'Sale'

    def check_sale_blocks(self):
        sale_blocks = self.find(loc.sale_block)
        # assert len(sale_blocks) == 6
        expect(sale_blocks).to_have_count(6)

    def check_top_menu(self):
        top_menu = self.find(loc.top_menu)
        expect(top_menu).to_have_count(6)
        # assert len(top_menu) == 6

    def check_side_menu(self):
        side_menu = self.find(loc.side_menu)
        expect(side_menu).to_be_visible()
        # assert side_menu.is_displayed()
