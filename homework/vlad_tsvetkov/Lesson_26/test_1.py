from playwright.sync_api import Page, expect


def test_one(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='username').fill('tomsmith')
    page.get_by_role('textbox', name='password').fill('SuperSecretPassword!')
    page.get_by_role('button').click()
    expect(page).to_have_url('https://the-internet.herokuapp.com/secure')


def test_two(page: Page):
    first_name = 'John'
    last_name = 'Smith'
    email = 'smthing@gmail.com'
    mobile = '7902777777'
    birthdate = '29 Feb 2000'
    hobbies = 'Reading'
    address = 'Solar system, Moon'
    state = 'Haryana'
    city = 'Karnal'
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill(first_name)
    page.get_by_placeholder('Last Name').fill(last_name)
    page.get_by_placeholder('name@example.com').fill(email)
    page.locator('//label[@for="gender-radio-3"]').check()
    page.get_by_placeholder('Mobile Number').fill(mobile)
    date_field = page.locator('//input[@id="dateOfBirthInput"]')
    date_field.click()
    date_field.press('Control+a')
    date_field.fill(birthdate)
    subject_field = page.locator('//div[contains(@class, "subjects-auto-complete__input")]/input')
    subject_field.fill('o')
    page.locator('//div[@id="react-select-2-option-2"]').click()
    page.locator(f'//label[contains(text(), "{hobbies}")]').click()
    page.get_by_placeholder('Current Address').fill(address)
    page.get_by_text('Select State').click()
    page.locator(f'//div[contains(text(), "{state}")]').click()
    page.get_by_text('Select City').click()
    page.locator(f'//div[contains(text(), "{city}")]').click()
    page.get_by_role('button').click()
