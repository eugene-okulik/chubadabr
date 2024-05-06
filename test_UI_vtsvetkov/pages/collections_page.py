from pages.base_page import BasePage
from locators import collections_page_locs as loc
from playwright.sync_api import expect


class CollectionPage(BasePage):
    rel_url = 'collections/eco-friendly.html'
    category_text = 'Eco Friendly'
    category_title = 'Eco Friendly'
    product_name = 'Ana Running Short'

    def check_category_text(self):
        category_text = self.find(loc.category)
        expect(category_text).to_have_text(self.category_text)

    def check_category_title(self):
        expect(self.page).to_have_title(self.category_title)

    def add_to_cart(self):
        size_btn = self.find(loc.short_28_size).first
        size_btn.hover()
        size_btn.click()
        clr_btn = self.find(loc.short_28_color).first
        clr_btn.click()
        add_btn = self.find(loc.short_add_to_cart).first
        add_btn.hover()
        add_btn.click()
        added_text = self.find(loc.added_to_cart_alert)
        expect(added_text).to_contain_text(self.product_name)
        cart_num = self.find(loc.cart_counter)
        expect(cart_num).to_have_text('1')
