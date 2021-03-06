from screenplay import Actor
from abilities import browse_the_web
from actions_selenium import navigate_to, find_element, enter_text, value_of
from os import path
from selenium.webdriver.common.by import By


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_the_value_of_a_stored_element_is_returned():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'fourth_text')).and_store_as('textbox'),
        value_of().stored_element('textbox')
    )

    assert returned_value == 'fourth textbox'


def test_a_whitespace_stripped_value_of_a_stored_element_is_returned():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    locator = (By.ID, 'third_text')

    returned_value = user.attempts_to(
        navigate_to(test_page),
        enter_text('  text  ').into_element(locator),
        find_element(locator).and_store_as('textbox'),
        value_of().stored_element('textbox').stripped_of_whitespace()
    )

    assert returned_value == 'text'
