import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.set_window_size(2500, 1600)
    yield chrome_driver


def test_new_tab(driver):
    alert = Alert(driver)
    wait = WebDriverWait(driver, 3)
    action = ActionChains(driver)
    driver.get('https://www.demoblaze.com/index.html')
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-title')))
    action.key_down(Keys.CONTROL).perform()
    driver.find_element(By.CLASS_NAME, 'card-title').click()
    action.key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[@onclick="addToCart(1)"]'))).click()
    wait.until(EC.alert_is_present())
    alert.accept()
    product_name = driver.find_element(By.TAG_NAME, 'h2').text
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, 'cartur').click()
    cart_product_name = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'td')))[1].text
    assert product_name == cart_product_name


def test_comparing_stuff(driver):
    wait = WebDriverWait(driver, 4)
    action = ActionChains(driver)
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    product = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'product-item-link')))[0]
    product_text = product.text
    action.move_to_element(product).perform()
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="action tocompare"]'))).click()
    compare_product_name = wait.until(
        EC.presence_of_element_located((By.XPATH, '//strong[@class="product-item-name"]'))).text
    assert product_text == compare_product_name
