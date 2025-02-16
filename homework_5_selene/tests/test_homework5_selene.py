import os.path
from selene import browser, command, have, be
import pytest

def test_Practice_Form(browser_settings):
    browser.open('/')
    #---f_name и l_name
    browser.element('[id="firstName"]').should(be.blank).type('Andrey')
    browser.element('[id="lastName"]').should(be.blank).type('Ignatov')
    #---email
    browser.element('[id="userEmail"]').should(be.blank).type('homework5@gmail.com')
    #---Gender
    browser.element('[for="gender-radio-1"]').click()
    #---Phone
    browser.element('[id="userNumber"]').should(be.blank).type('8800553535')
    #---Calendar
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="10"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="1994"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--021"]').click()
    browser.element('[id="dateOfBirthInput"]').should(have.value('21 Nov 1994'))
    #---Subjects
    browser.element('[id="subjectsInput"]').set_value('his')
    browser.element('[id="react-select-2-option-0"]').should(have.text('History')).click()
    #---Hobbies
    browser.element('[for="hobbies-checkbox-1"]').click()
    #---Picture
    browser.element('[id="uploadPicture"]').type(os.path.abspath('../test_file/test_pic.jpg'))
    #---Current Address
    browser.element('[id="currentAddress"]').should(be.blank).type('Test addres 12345')
    # ---State
    browser.element('[id="react-select-3-input"]').set_value('Hary')
    browser.element('[id="react-select-3-option-2"]').should(have.text('Haryana')).click()
    #---City
    browser.element('[id="react-select-4-input"]').set_value('Kar')
    browser.element('[id="react-select-4-option-0"]').should(have.text('Karnal')).click()
    #---submit
    browser.element('[id="submit"]').click()
    #---Complete form
    browser.element('[class="modal-content"]').should(be.visible)
    browser.element('[class="table table-dark table-striped table-bordered table-hover"]').should(have.text('Andrey Ignatov'))
    browser.element('[class="table table-dark table-striped table-bordered table-hover"]').should(have.text('homework5@gmail.com'))
    browser.element('[class="table table-dark table-striped table-bordered table-hover"]').should(have.text('Male'))
    browser.element('[class="table table-dark table-striped table-bordered table-hover"]').should(have.text('21 November,1994'))
    browser.element('[class="table table-dark table-striped table-bordered table-hover"]').should(have.text('History'))
    browser.element('[class="table table-dark table-striped table-bordered table-hover"]').should(have.text('test_pic.jpg'))
    browser.element('[class="table table-dark table-striped table-bordered table-hover"]').should(have.text('Test addres 12345'))
    browser.element('[class="table table-dark table-striped table-bordered table-hover"]').should(have.text('Haryana Karnal'))
