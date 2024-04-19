import pytest

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.set_window_size(2500, 1600)
    yield chrome_driver


# Part 1
def test_send_text(driver):
    input_text = 'abracadabra'
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input = driver.find_element(By.NAME, 'text_string')
    input.send_keys(input_text)
    input.submit()
    result_text = driver.find_element(By.ID, 'result-text').text
    print('prompt:', result_text)
    assert result_text == input_text


# Part 2
def test_fill_form(driver):
    wait = WebDriverWait(driver, 2)
    first_name = 'John'
    last_name = 'Smith'
    email = 'smthing@gmail.com'
    mobile = '7902777777'
    birthdate = '29 Feb 2000'
    hobbies = ['Sports', 'Reading', 'Music']
    address = 'Solar system, Moon'
    state = 'Haryana'
    city = 'Karnal'

    driver.get('https://demoqa.com/automation-practice-form')
    driver.find_element(By.ID, 'firstName').send_keys(first_name)
    driver.find_element(By.ID, 'lastName').send_keys(last_name)
    driver.find_element(By.ID, 'userEmail').send_keys(email)
    driver.find_element(By.XPATH, '//label[@for="gender-radio-3"]').click()
    driver.find_element(By.ID, 'userNumber').send_keys(mobile)
    driver.execute_script("window.scrollTo(0, 500)")
    date_field = driver.find_element(By.ID, 'dateOfBirthInput')
    date_field.click()
    date_field.send_keys(Keys.CONTROL, 'a')
    date_field.send_keys(birthdate)
    date_field.send_keys(Keys.ENTER)
    subject_field = driver.find_element(By.XPATH, '//div[contains(@class, "subjects-auto-complete__input")]/input')
    subject_field.click()
    subject_field.send_keys('o')
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'subjects-auto-complete__option')))
    subjects = driver.find_elements(By.CLASS_NAME, 'subjects-auto-complete__option')
    subjects[2].click()
    for el in hobbies:
        driver.find_element(By.XPATH, f'//label[contains(text(), "{el}")]').click()
    driver.find_element(By.ID, 'currentAddress').send_keys(address)
    driver.find_element(By.ID, 'state').click()
    driver.find_element(By.XPATH, f'//div[contains(text(), "{state}")]').click()
    driver.find_element(By.ID, 'city').click()
    driver.find_element(By.XPATH, f'//div[contains(text(), "{city}")]').click()
    driver.find_element(By.ID, 'submit').click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'table-responsive')))
    sended_data = driver.find_elements(By.XPATH, '//tr')
    for el in sended_data:
        print(el.text)


# Part 3
def test_single_select(driver):
    wait = WebDriverWait(driver, 3)
    lang = 'Ruby'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select = driver.find_element(By.ID, 'id_choose_language')
    options = Select(select)
    options.select_by_visible_text(lang)
    result = options.first_selected_option
    assert result.text == lang
    driver.find_element(By.ID, 'submit-id-submit').click()
    wait.until(EC.presence_of_element_located((By.ID, 'result')))
    result = driver.find_element(By.ID, 'result-text')
    assert result.text == lang


def test_hatiko_mode(driver):
    wait = WebDriverWait(driver, 10)
    expected_text = 'Hello World!'
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.TAG_NAME, 'button').click()
    wait.until(EC.presence_of_element_located((By.ID, 'finish')))
    text = driver.find_element(By.XPATH, '//h4[contains(text(), "Hello World!")]').text
    assert text == expected_text
