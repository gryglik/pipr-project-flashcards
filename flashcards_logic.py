from __future__ import annotations
import lib.errors as error
import random
import time


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
            raise error.FlashcardNotInSetError(
                'Cannot find flashcard to delete.')

    def flashcard_index(self, flashcard: Flashcard) -> int:
        """Returns index of the given flashcard in the set. Counting from 0"""
        if flashcard in self._flashcards:
            return self._flashcards.index(flashcard)
        raise error.FlashcardNotInSetError('Cannot find flashcard in the set.')

    def len(self) -> int:
        """Returns number of flashcards in set."""
        return len(self._flashcards)

    def is_empty(self) -> bool:
        """Returns True if no flashcards in the set"""
        return False if len(self._flashcards) else True

    def draw_flashcards(self, count: int) -> FlashcardsSet:
        """Returns new flashcards set with drawn given quantity flashcards."""
        if self.is_empty():
            raise error.IndexOutOfRangeError(
                'Cannot draw flashcards. Set is empty.')
        elif count > self.len() or count <= 0:
            raise error.IndexOutOfRangeError(
                'Cannot draw cards. Invalid count.')
        draw_result = random.sample(self.flashcards, count)
        return FlashcardsSet(f'{self.name}', flashcards=draw_result)


class TestItem():
    def __init__(self, flashcard: Flashcard, mode: int = 0) -> None:
        """Creates an instance of test item which tests knowledge about one
           flashcard.
           mode = 0 - expected answer is flashcard's definition
           mode = 1 - expected answer is flashcard's phrase"""
        self._flashcard: Flashcard = flashcard
        self._opened: bool = False
        self._question: str | None = None
        self._answer: str | None = None
        self._setup(mode)
        self._user_answer: str | None = None

    def _setup(self, mode: int) -> None:
        """Setups mode of the test item"""
        match mode:
            case 0:
                self._question = self._flashcard.phrase
                self._answer = self._flashcard.definition

            case 1:
                self._question = self._flashcard.definition
                self._answer = self._flashcard.phrase

    def open(self) -> None:
        """Opens test item"""
        self._opened = True

    def is_opened(self) -> bool:
        """Returns true if test item is opened."""
        return self._opened

    def get_question(self) -> str:
        """Returns question if test item is opened"""
        if self._opened:
            return self._question
        else:
            raise error.ClosedTestItemError(
                'Cannot access question. Test item is closed.')

    def set_answer(self, answer: str) -> None:
        """If test item is opened sets answer."""
        if self._opened:
            self._user_answer = answer
        else:
            raise error.ClosedTestItemError(
                'Cannot change the answer. Test item is closed.')

    def result(self) -> bool:
        """Closes test item and return true if answear is correct
        and false if incorrect."""
        self._opened = False
        return self._answer == self._user_answer


class Test():
    def __init__(self, flashcards_set: FlashcardsSet) -> None:
        """Creates an instance of a test for given flashcards set."""
        if flashcards_set.is_empty():
            raise error.FlashcardNotInSetError(
                'Cannot create a test. Empty flashcards set.')
        self._flashcards_set: FlashcardsSet = flashcards_set
        self._test_items: list[TestItem] = self._generateTestItems()
        self._running: bool = None
        self._start_time: float | None = None
        self._end_time: float | None = None

    def _generateTestItems(self) -> list[TestItem]:
        """Returns list of test items for test's flashcards set."""
        test_items = []
        for flashcard in self._flashcards_set._flashcards:
            test_items.append(TestItem(flashcard))
        return test_items

    def name(self) -> str:
        """Returns name of the flashcard set used to create test."""
        return self._flashcards_set.name

    def start(self) -> None:
        """Starts the test and starts timer"""
        self._running = True
        self._start_time = time.time()
        for test_item in self._test_items:
            test_item.open()

    def close(self) -> None:
        """Closes the test and stops timer."""
        self._running = False
        self._end_time = time.time()

    def is_started(self) -> bool:
        """Returns True if test is running."""
        return self._running

    def is_finished(self) -> bool:
        """Returns True if test has start time and is not running"""
        if self._start_time and not self._running:
            return True

    def get_test(self) -> list[TestItem]:
        """Returns list of test items."""
        return self._test_items

    def result(self) -> TestResult:
        """Closes test and returns TestResult object."""
        self.close()
        return TestResult(self)

    def time(self) -> float:
        """If test is running returns seconds since the test has started.
        If test has finished returns duration of the test."""
        if not self._start_time:
            raise error.TestNotStartedError(
                'Cannot get test time. Test has not started yet.')

        if self._running:
            return time.time() - self._start_time
        else:
            return self._end_time - self._start_time


class TestResult():
    """Provides information about test result."""
    def __init__(self, test: Test) -> None:
        """Creates an isntance of TestResult"""
        if not test.is_finished():
            raise error.TestNotFinishedError(
                'Cannot get test result. Test has not finished yet.'
            )
        self._test: Test = test
        self._correct_answers: int
        self._incorrect_answers: int
        self._questions_count: int
        self._accuracy: float
        self._duration: float
        self._time_per_question: float
        self._computeResults()
        self._computeTime()

    def _computeResults(self):
        """Computes count of correct, incorrect and all answers"""
        # Accessing TestItems
        test_items = self._test.get_test()
        # Computing questions count
        self._questions_count = len(test_items)
        # Computing correct answers
        self._correct_answers = sum(
            [True for test_item in test_items if test_item.result()])
        # Computing incorrect answers
        self._incorrect_answers = self._questions_count - self._correct_answers
        # Computing accuracy in %
        self._accuracy = (self._correct_answers / self._questions_count * 100)

    def _computeTime(self):
        """Computes duration of the test and average time spent on question."""
        # Accessing duration of the test
        self._duration = self._test.time()
        # Computing acerage time spent on question
        self._time_per_question = self._duration / self._questions_count

    def get_correct_answers_count(self) -> int:
        """Returns count of correct answers"""
        return self._correct_answers

    def get_incorrect_answers_count(self) -> int:
        """Returns count of incorrect answers"""
        return self._incorrect_answers

    def get_questions_count(self) -> int:
        """Returns count of all questions"""
        return self._questions_count

    def get_accuracy(self) -> float:
        """Returns accuracy of test in %.
        {correct_answers_count} / {questions_count}"""
        return self._accuracy

    def get_duration(self) -> float:
        """Returs duration of the test in seconds."""
        return self._duration

    def get_time_per_question(self) -> float:
        """Returns average time spent on one question"""
        return self._time_per_question


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
            raise error.SetNotInSessionError(
                'Given set is not in the session.')
        self._flashcards_sets.remove(flashcards_set)

    def open_set(self, flashcards_set: FlashcardsSet) -> None:
        """Opens given flashcards set"""
        if flashcards_set not in self._flashcards_sets:
            raise error.SetNotInSessionError(
                'Given set is not in the session.')
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

    def generate_test(self, count: int) -> Test:
        """Generates a test with given count of flashcards from the opened
        flashcards set."""
        if not self._opened_set:
            raise error.NotOpenedSetError(
                'Cannot generate test. No set is open.')
        # Generating flashcards set with predefined questions count
        random_set = self.opened_set.draw_flashcards(count)
        return Test(random_set)
