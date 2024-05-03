def test_collection_text(collection_page):
    collection_page.visit_page()
    collection_page.check_category_text()


def test_collection_title(collection_page):
    collection_page.visit_page()
    collection_page.check_category_title()


def test_add_to_cart(collection_page):
    collection_page.visit_page()
    collection_page.add_to_cart()
