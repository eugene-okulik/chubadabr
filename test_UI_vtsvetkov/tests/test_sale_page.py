def test_check_sale_blocks(sale_page):
    sale_page.visit_page()
    sale_page.check_sale_blocks()


def test_check_top_menu(sale_page):
    sale_page.visit_page()
    sale_page.check_top_menu()


def test_check_side_menu(sale_page):
    sale_page.visit_page()
    sale_page.check_side_menu()
