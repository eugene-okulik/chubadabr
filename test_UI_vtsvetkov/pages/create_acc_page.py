from pages.base_page import BasePage
from locators import create_acc_page_locs as loc
from playwright.sync_api import expect


class CreateAccPage(BasePage):
    rel_url = 'customer/account/create/'
    fname = 'Alex'
    lname = 'Xela'
    email = 'alex@xela.com'
    password = 'A1exxela'
    required_field_error = 'This is a required field.'
    invalid_email_error = 'Please enter a valid email address (Ex: johndoe@domain.com).'
    password_3_classes_error = (
        'Minimum of different classes of characters in password is 3. Classes of characters: '
        'Lower Case, Upper Case, Digits, Special Characters.'
    )

    def no_first_name_given(self):
        self.find(loc.last_name).fill(self.lname)
        self.find(loc.email).fill(self.email)
        self.find(loc.password).fill(self.password)
        self.find(loc.pass_confirm).fill(self.password)
        self.find(loc.submit).click()
        error_text = self.find(loc.first_name_error)
        expect(error_text).to_have_text(self.required_field_error)

    def invalid_email(self):
        self.find(loc.first_name).fill(self.fname)
        self.find(loc.last_name).fill(self.lname)
        self.find(loc.email).fill(self.email[:4])
        self.find(loc.password).fill(self.password)
        self.find(loc.pass_confirm).fill(self.password)
        self.find(loc.submit).click()
        error_text = self.find(loc.email_error)
        expect(error_text).to_have_text(self.invalid_email_error)

    def invalid_password(self):
        self.find(loc.first_name).fill(self.fname)
        self.find(loc.last_name).fill(self.lname)
        self.find(loc.email).fill(self.email)
        self.find(loc.password).fill('123456789')
        self.find(loc.pass_confirm).fill('123456789')
        self.find(loc.submit).click()
        password_error = self.find(loc.password_error)
        expect(password_error).to_have_text(self.password_3_classes_error)
