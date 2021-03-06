import pytest
from screenplay import Actor
from abilities import browse_the_web
from actions_selenium import navigate_to, find_element_with_locator_and_text
from os import path
from selenium.webdriver.common.by import By


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_an_element_found_by_locator_and_text_is_stored_and_returned():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element_with_locator_and_text((By.CSS_SELECTOR, '#list li'), 'fourth_li').and_store_as('fourth')
    )

    assert returned_value.text == 'fourth_li'

    stored_value = user.state['fourth'].value

    assert stored_value.text == 'fourth_li'


def test_an_element_found_by_locator_and_text_can_by_just_returned():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element_with_locator_and_text((By.CSS_SELECTOR, '#list li'), 'fourth_li')
    )

    assert returned_value.text == 'fourth_li'


@pytest.mark.slow
def test_trying_to_find_an_element_that_does_not_exist_stores_and_returns_None():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element_with_locator_and_text((By.CSS_SELECTOR, '#does_not_exist'), 'fourth_li').and_store_as('fourth')
    )

    assert returned_value is None

    stored_value = user.state['fourth'].value

    assert stored_value is None
