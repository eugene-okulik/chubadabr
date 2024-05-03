import pytest

from playwright.sync_api import BrowserContext
# from selenium import webdriver
from pages.create_acc_page import CreateAccPage
from pages.collections_page import CollectionPage
from pages.sale_page import SalePage


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def create_acc(page):
    return CreateAccPage(page)


@pytest.fixture()
def collection_page(page):
    return CollectionPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
