import os.path
from selene import browser, command, have, be
import pytest

def test_practice_form(browser_settings):
    browser.open('/')
    browser.driver.execute_script("$('#RightSide_Advertisement').remove()")
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")
    browser.element('[id="firstName"]').should(be.blank).type('Andrey')
    browser.element('[id="lastName"]').should(be.blank).type('Ignatov')
    browser.element('[id="userEmail"]').should(be.blank).type('homework5@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type('8800553535')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="10"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="1994"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--021"]').click()
    browser.element('[id="subjectsInput"]').set_value('his').element('//*[contains(text(),"History")]').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[id="uploadPicture"]').type(os.path.abspath('../test_file/test_pic.jpg'))
    browser.element('[id="currentAddress"]').should(be.blank).type('Test addres 12345')
    browser.element('[id="react-select-3-input"]').set_value('Hary').element('//*[contains(text(),"Haryana")]').click()
    browser.element('[id="react-select-4-input"]').set_value('Kar').element('//*[contains(text(),"Karnal")]').click()
    browser.element('[id="submit"]').click()
    browser.element('[class="modal-content"]').should(be.visible)
    browser.element('[class="modal-content"]').should(have.text('Andrey Ignatov')) #Student Name
    browser.element('[class="modal-content"]').should(have.text('homework5@gmail.com')) #Student Email
    browser.element('[class="modal-content"]').should(have.text('Male')) #Gender
    browser.element('[class="modal-content"]').should(have.text('8800553535')) #Mobile
    browser.element('[class="modal-content"]').should(have.text('21 November,1994')) #Date of Birth
    browser.element('[class="modal-content"]').should(have.text('History')) #Subjects
    browser.element('[class="modal-content"]').should(have.text('Sport')) #Hobbies
    browser.element('[class="modal-content"]').should(have.text('test_pic.jpg'))
    browser.element('[class="modal-content"]').should(have.text('Test addres 12345'))
    browser.element('[class="modal-content"]').should(have.text('Haryana Karnal'))