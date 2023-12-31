from csv import DictReader


class EmptyFieldError(Exception):
    pass


class NotAFlashcardError(Exception):
    pass


class FlascardNotInSetError(Exception):
    pass


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
            raise EmptyFieldError('Phrase field cannot be empty.')
        self._phrase = str(new_phrase)
        return True

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, new_definition):
        if not new_definition:
            raise EmptyFieldError('Definition field cannot be empty.')
        self._definition = str(new_definition)
        return True

    @property
    def priority(self):
        return self._priority


class FlashcardsSet():
    def __init__(self, name, flashcards=None):
        self.name = name
        self._flashcards = []
        if flashcards:
            for flashcard in flashcards:
                self.add_flashcard(flashcard)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise EmptyFieldError('Set name cannot be empty.')
        self._name = str(new_name)

    @property
    def flashcards(self):
        return self._flashcards

    def add_flashcard(self, flashcard):
        if isinstance(flashcard, Flashcard):
            self._flashcards.append(flashcard)
            return True
        else:
            raise NotAFlashcardError(f'Object {flashcard} is not a Flashcard.')

    def remove_flashcard(self, flashcard):
        try:
            self._flashcards.remove(flashcard)
            return True
        except Exception as e:
            raise FlascardNotInSetError(f'Cannot find flashcard to delete {e}')


class Session():
    def __init__(self):
        self.user_name = None


def load_from_csv(fp):
    flashcards_set = FlashcardsSet('[imported set]')
    reader = DictReader(fp)
    for record in reader:
        flashcard = Flashcard(
            record['phrase'],
            record['definition'],
            priority=True if record['priority'] == 'True' else False
        )
        flashcards_set.add_flashcard(flashcard)
    return flashcards_set
