from csv import DictReader


class EmptyFieldError(Exception):
    pass


class NotAFlashcardError(Exception):
    pass


class FlascardNotInSetError(Exception):
    pass


class StringTooLongError(Exception):
    pass


class Flashcard():
    def __init__(self, phrase: str, definition: str, priority=False):
        """Creates an instance of a flashcard."""
        self.phrase = phrase
        self.definition = definition
        self.priority = bool(priority)

    @property
    def phrase(self):
        return self._phrase

    @phrase.setter
    def phrase(self, new_phrase: str):
        if not new_phrase:
            raise EmptyFieldError('Phrase field cannot be empty.')
        elif len(new_phrase) > 50:
            raise StringTooLongError("Phrase is too long. Max 50 chars.")
        self._phrase = str(new_phrase)
        return True

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, new_definition: str):
        if not new_definition:
            raise EmptyFieldError('Definition field cannot be empty.')
        elif len(new_definition) > 50:
            raise StringTooLongError('Definition is too long. Maz 50 chars.')
        self._definition = str(new_definition)
        return True


class FlashcardsSet():
    """Creates an instance of flashcards set which keeps Flashcards objects."""
    def __init__(self, name: str, flashcards=None):
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
        elif len(new_name) > 50:
            raise StringTooLongError('Set name too long. Max 50 chars.')
        self._name = str(new_name)
        return True

    @property
    def flashcards(self):
        return self._flashcards

    def add_flashcard(self, flashcard: Flashcard):
        if isinstance(flashcard, Flashcard):
            self._flashcards.append(flashcard)
            return True
        else:
            raise NotAFlashcardError(f'Object {flashcard} is not a Flashcard.')

    def remove_flashcard(self, flashcard: Flashcard):
        try:
            self._flashcards.remove(flashcard)
            return True
        except Exception as e:
            raise FlascardNotInSetError(f'Cannot find flashcard to delete {e}')


class Session():
    """Stores information about current learning session."""
    def __init__(self, username: str):
        self.username = username
        self._flashcards_sets = []

        self.opened_set: FlashcardsSet

    @property
    def flashcards_sets(self):
        return self._flashcards_sets

    def add_set(self, flashcard_set: FlashcardsSet):
        self._flashcards_sets.append(flashcard_set)
        return True


def load_from_csv(fp):
    """Returns an instance of FlashcardsSet for given file object"""
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
