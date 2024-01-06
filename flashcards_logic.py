import lib.errors as error


class Flashcard():
    """Stores information about flashcard: phrase, definition and priority"""
    def __init__(self, phrase: str, definition: str,
                 priority: bool = False) -> None:
        """Creates an instance of a flashcard."""
        self.phrase: str = phrase
        self.definition: str = definition
        self.priority: bool = priority

    @property
    def phrase(self) -> str:
        return self._phrase

    @phrase.setter
    def phrase(self, new_phrase: str) -> None:
        """Sets flashcard's phrase, max 50 chars."""
        if not new_phrase:
            raise error.EmptyStringError('Phrase field cannot be empty.')
        elif len(new_phrase) > 50:
            raise error.StringTooLongError("Phrase is too long. Max 50 chars.")
        self._phrase = str(new_phrase)

    @property
    def definition(self) -> str:
        return self._definition

    @definition.setter
    def definition(self, new_definition: str) -> None:
        """Sets flashcard's definition, max 50 chars."""
        if not new_definition:
            raise error.EmptyStringError('Definition field cannot be empty.')
        elif len(new_definition) > 50:
            raise error.StringTooLongError(
                'Definition is too long. Max 50 chars.')
        self._definition = str(new_definition)

    @property
    def priority(self) -> bool:
        return self._priority

    @priority.setter
    def priority(self, new_priority: bool) -> None:
        """Sets flashcard's priority."""
        self._priority = bool(new_priority)


class FlashcardsSet():
    """Stores flashcards."""
    def __init__(self, name: str,
                 flashcards: list[Flashcard] | None = None) -> None:
        """Creates an instance of flashcards set which keeps flashcards."""
        self.name = name
        self._flashcards = []
        if flashcards:
            for flashcard in flashcards:
                self.add_flashcard(flashcard)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Sets flashcards set name. Max 25 chars."""
        if not new_name:
            raise error.EmptyStringError('Set name cannot be empty.')
        elif len(new_name) > 25:
            raise error.StringTooLongError('Set name too long. Max 25 chars.')
        self._name = str(new_name)

    @property
    def flashcards(self) -> list[Flashcard]:
        return self._flashcards

    def add_flashcard(self, flashcard: Flashcard) -> None:
        """Adds given flashcard to the set."""
        self._flashcards.append(flashcard)

    def remove_flashcard(self, flashcard: Flashcard) -> None:
        """Removes given flashcard from the set."""
        if flashcard in self._flashcards:
            self._flashcards.remove(flashcard)
        else:
            raise error.FlascardNotInSetError(
                'Cannot find flashcard to delete.')

    def flashcard_index(self, flashcard: Flashcard) -> int:
        """Returns index of the given flashcard in the set. Counting from 0"""
        if flashcard in self._flashcards:
            return self._flashcards.index(flashcard)
        raise error.FlascardNotInSetError('Cannot find flashcard in the set.')

    def len(self) -> int:
        """Returns number of flashcards in set."""
        return len(self._flashcards)

    def is_empty(self) -> bool:
        """Returns True if no flashcards in the set"""
        return False if len(self._flashcards) else True


class Session():
    """Stores information about current learning session."""
    def __init__(self, username: str) -> None:
        self.username: str = username
        self._flashcards_sets: list[FlashcardsSet | None] = []
        self._opened_set: FlashcardsSet | None = None
        self._opened_flashcard: Flashcard | None = None

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, new_username: str) -> None:
        """Sets username. Max 25 chars."""
        if not new_username:
            raise error.EmptyStringError('Username cannot be empty.')
        elif len(new_username) > 25:
            raise error.StringTooLongError(
                'Username is too long. Max 25 chars.')
        self._username = str(new_username)

    @property
    def flashcards_sets(self) -> list[FlashcardsSet | None]:
        return self._flashcards_sets

    @property
    def opened_set(self) -> FlashcardsSet:
        return self._opened_set

    @property
    def opened_flashcard(self) -> Flashcard:
        return self._opened_flashcard

    def add_set(self, flashcards_set: FlashcardsSet) -> None:
        """Adds given flashcards set to session."""
        self._flashcards_sets.append(flashcards_set)

    def remove_set(self, flashcards_set: FlashcardsSet) -> None:
        """Removes given set from the session"""
        if flashcards_set not in self.flashcards_sets:
            raise error.SetNotInSessionError('Given set is not in the session.')
        self._flashcards_sets.remove(flashcards_set)

    def open_set(self, flashcards_set: FlashcardsSet) -> None:
        """Opens given flashcards set"""
        if flashcards_set not in self._flashcards_sets:
            raise error.SetNotInSessionError("Given set is not in the session.")
        self._opened_set = flashcards_set

    def close_set(self) -> None:
        """Closes opened set."""
        self._opened_set = None

    def open_flashcard(self, index: int) -> None:
        """Opens flashcard of given index from the opened flashcards set."""
        if not self._opened_set:
            raise error.NotOpenedSetError('No set is opened.')
        elif index >= self._opened_set.len():
            raise error.IndexOutOfRangeError()
        self._opened_flashcard = self.opened_set.flashcards[index]

    def close_flashcard(self) -> None:
        """Closes opened flashcard."""
        self._opened_flashcard = None

    def flashcard_index(self) -> int:
        """Returns opened flashcard's index in the flashcards set."""
        if self.opened_flashcard:
            return self._opened_set.flashcard_index(self.opened_flashcard)
        raise error.NotOpenedFlashcardError("No flashcard is opened.")

    def next_flashcard(self) -> None:
        """Opens next flashcard in the current opened set.
           If it is the last flashcard, opens the first one."""
        if not self.opened_flashcard:
            raise error.NotOpenedFlashcardError('No flashcard is opened.')
        new_index = (self.flashcard_index() + 1) % self.opened_set.len()
        self._opened_flashcard = self._opened_set.flashcards[new_index]

    def previous_flashcard(self) -> None:
        """Opens previous flashcard in the current opened set.
           If it is the first flashcard, opens the last one."""
        if not self.opened_flashcard:
            raise error.NotOpenedFlashcardError('No flashcard is opened.')
        new_index = (self.flashcard_index() - 1) % self.opened_set.len()
        self._opened_flashcard = self._opened_set.flashcards[new_index]

    def flashcard_counter_info(self) -> str:
        """Returns string with information about the index of opened flashcard
            in the form of:
           '{opened flashcard index + 1} / {number of flashcards in set}' """
        if not self._opened_set:
            return '0 / 0'
        elif not self._opened_flashcard:
            return f'0 / {self._opened_set.len()}'
        return f'{self.flashcard_index() + 1} / {self._opened_set.len()}'
        # self.flashcard_index() + 1 to count from 1
