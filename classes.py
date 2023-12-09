class Flashcard():
    def __init__(self, phrase, definition, priority=False) -> None:
        """Creates an instance of a flashcard."""
        self.phrase = phrase
        self.definition = definition
        self._priority = bool(priority)

    @property
    def phrase(self):
        return self._phrase

    @phrase.setter
    def phrase(self, new_phrase):
        if not new_phrase:
            raise ValueError('Phrase field cannot be empty.')
        self._phrase = new_phrase
        return True

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, new_definition):
        if not new_definition:
            raise ValueError('Definition field cannot be empty.')
        self._definition = new_definition
        return True

    @property
    def priority(self):
        return self._priority


class FlashcardsSet():
    def __init__(self, name, flashcards) -> None:
        pass
