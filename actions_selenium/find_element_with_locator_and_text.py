from screenplay import Action, Actor, log_message
from abilities.browse_the_web import waiting_browser_for
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException


class find_element_with_locator_and_text(Action):
    def __init__(self, locator: str, text: str):
        super().__init__()
        self._locator = locator
        self._text = text
        self._id = None

    def and_store_as(self, id: str):
        self._id = id
        return self

    @log_message('Finding element {self._locator} with text "{self._text}"')
    def perform_as(self, actor: Actor):
        elements = []
        try:
            elements = waiting_browser_for(actor, (StaleElementReferenceException, NoSuchElementException)) \
                .find_elements(*self._locator)
        except TimeoutException:
            pass

        element = next((e for e in elements if e.text.strip() == self._text), None)

        if self._id is not None:
            actor.state[self._id].set(element)

        return element
