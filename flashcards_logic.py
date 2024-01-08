from __future__ import annotations
import random
import time
from datetime import date

import lib.errors as error


class Flashcard():
    """Stores information about flashcard: phrase, definition,
    and current learning cup."""
    def __init__(
            self, phrase: str, definition: str, priority: bool = False,
            learning_cup: int = 0) -> None:
        """Creates an instance of a flashcard.

        Args:
            phrase (str): phrase of the flashcard
            definition (str): definition of the flashcard
            priority (bool, optional): priority mode of the flashcard.
            Defaults to False.
            learning_cup (int, optional): learning cup to which
            flashcard belongs to. From 0 (not learnt at all)
            to 3 (lernt perfectely). Defaults to 0.
        """
        self.phrase: str = phrase
        self.definition: str = definition
        self.priority: bool = priority
        self.learning_cup: int = learning_cup

    @property
    def phrase(self) -> str:
        """Returns flashcard's phrase

        Returns:
            str: flashcard's phrase
        """
        return self._phrase

    @phrase.setter
    def phrase(self, new_phrase: str) -> None:
        """Sets flashcard's phrase, max 50 chars.

        Args:
            new_phrase (str): new phrase of the flashcard

        Raises:
            error.EmptyStringError: if new_phrase is empty
            error.StringTooLongError: if new_phrase has more than 50 chars
        """        """"""
        if not new_phrase:
            raise error.EmptyStringError('Phrase field cannot be empty.')
        elif len(new_phrase) > 50:
            raise error.StringTooLongError("Phrase is too long. Max 50 chars.")
        self._phrase = str(new_phrase)

    @property
    def definition(self) -> str:
        """Returns flashcard's definition

        Returns:
            str: flashcard's definition
        """
        return self._definition

    @definition.setter
    def definition(self, new_definition: str) -> None:
        """Sets flashcard's definition, max 50 chars.

        Args:
            new_definition (str): new definition of the flashcard

        Raises:
            error.EmptyStringError: if new_definition is empty
            error.StringTooLongError: if new_definition has more than 50 chars
        """        """"""
        if not new_definition:
            raise error.EmptyStringError('Definition field cannot be empty.')
        elif len(new_definition) > 50:
            raise error.StringTooLongError(
                'Definition is too long. Max 50 chars.')
        self._definition = str(new_definition)

    @property
    def priority(self) -> bool:
        """Returns flashcard's priority

        Returns:
            bool: flashcard's priority
        """
        return self._priority

    @priority.setter
    def priority(self, new_priority: bool) -> None:
        """Sets flashcard's priority.

        Args:
            new_priority (bool): flashcard's new priority
        """        """"""
        self._priority = bool(new_priority)

    @property
    def learning_cup(self) -> int:
        """Returns to which learning cup flashcards belongs to

        Returns:
            int: learning cup, from 0 (not learnt at all)
            to 3 (lernt perfectely)
        """
        return self._learning_cup

    @learning_cup.setter
    def learning_cup(self, new_learning_cup: int) -> None:
        """Set's flashcard's learning cup

        Args:
            new_learning_cup (int): new learning cup, from 0
            (not learnt at all) to 3 (lernt perfectely)

        Raises:
            error.InvalidLearningCupError: if new learning cup is out
            of range
        """
        if int(new_learning_cup) not in [0, 1, 2, 3]:
            raise error.InvalidLearningCupError(
                'Cannot set learning cup. Learning cup has to be an integer '
                and 'from range 0 - 3')
        self._learning_cup = int(new_learning_cup)

    def next_learning_cup(self) -> None:
        """Moves flashcard to higher learning cup.
        """
        if self._learning_cup < 3:
            self._learning_cup += 1

    def previous_learning_cup(self) -> None:
        """Moves flashcard to the lower learning cup.
        """
        if self._learning_cup > 0:
            self._learning_cup -= 1

    def is_learned(self) -> bool:
        """Returns True if flashcard is learned.

        Returns:
            bool: True if flashcard is in 3rd learning cup.
        """
        return self._learning_cup == 3


class FlashcardsSet():
    """Stores flashcards.
    """
    def __init__(self, name: str,
                 flashcards: list[Flashcard] | None = None) -> None:
        """Creates an instance of flashcards set which keeps flashcards.

        Args:
            name (str): name of the flashcards set
            flashcards (list[Flashcard] | None, optional): list of Flashcards
            objects. Defaults to None.
        """
        self.name = name
        self._flashcards = []
        if flashcards:
            for flashcard in flashcards:
                self.add_flashcard(flashcard)
        self._last_learned = None

    @property
    def name(self) -> str:
        """Returns name of the flashcards set

        Returns:
            str: name of the FlashcardsSet
        """
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Sets flashcards set name. Max 25 chars.

        Args:
            new_name (str): new name of the flashcards set

        Raises:
            error.EmptyStringError: if new_name is empty
            error.StringTooLongError: if new_name has more than 25 chars
        """        """"""
        if not new_name:
            raise error.EmptyStringError('Set name cannot be empty.')
        elif len(new_name) > 25:
            raise error.StringTooLongError('Set name too long. Max 25 chars.')
        self._name = str(new_name)

    @property
    def flashcards(self) -> list[Flashcard]:
        """Returns list of flashcards

        Returns:
            list[Flashcard]: list of Flashcards objects
        """
        return self._flashcards

    def set_learned_today(self):
        """Sets that today was conducted learning test.
        """
        self._last_learned = date.today()

    def is_learned_today(self) -> bool:
        """Returns true if today was conducted learning test.

        Returns:
            bool: True if today was conducted learning test
        """
        return self._last_learned == date.today()

    def add_flashcard(self, flashcard: Flashcard) -> None:
        """Adds given flashcard to the set."

        Args:
            flashcard (Flashcard): Flashcard object to be added to set.
        """
        self._flashcards.append(flashcard)

    def remove_flashcard(self, flashcard: Flashcard) -> None:
        """Removes given flashcard from the set.

        Args:
            flashcard (Flashcard): Flashcard object to be removed from the Set

        Raises:
            error.FlashcardNotInSetError: if flashcard is not in the
            flashcard set
        """
        if flashcard in self._flashcards:
            self._flashcards.remove(flashcard)
        else:
            raise error.FlashcardNotInSetError(
                'Cannot find flashcard to delete.')

    def flashcard_index(self, flashcard: Flashcard) -> int:
        """Returns index of the given flashcard in the set. Counting from 0.

        Args:
            flashcard (Flashcard): Flashcard to get index of

        Raises:
            error.FlashcardNotInSetError: if flashcard is not in the set

        Returns:
            int: index of the flashcard in the set
        """
        if flashcard in self._flashcards:
            return self._flashcards.index(flashcard)
        raise error.FlashcardNotInSetError('Cannot find flashcard in the set.')

    def len(self) -> int:
        """Returns number of flashcards in set.

        Returns:
            int: number of flashcards in the set
        """
        return len(self._flashcards)

    def is_empty(self) -> bool:
        """Returns True if no flashcards in the set

        Returns:
            bool: True if flashcards set is empty
        """
        return False if len(self._flashcards) else True

    def draw_flashcards(self, count: int) -> FlashcardsSet:
        """Returns new flashcards set with drawn given quantity flashcards.

        Args:
            count (int): count of flashcards from the set to be drawn

        Raises:
            error.IndexOutOfRangeError: if given count is out of range

        Returns:
            FlashcardsSet: drawn flashcards
        """
        if self.is_empty():
            raise error.IndexOutOfRangeError(
                'Cannot draw flashcards. Set is empty.')
        elif count > self.len() or count <= 0:
            raise error.IndexOutOfRangeError(
                'Cannot draw cards. Invalid count.')
        draw_result = random.sample(self.flashcards, count)
        return FlashcardsSet(f'{self.name}', flashcards=draw_result)

    def create_learning_set(self) -> FlashcardsSet:
        """Returns learning flashcards sets, which consist of
        proposed to revision flashcards, according to the learning cup
        they are placed in.

        Methods returns Flashcards set acording to the algotihm:
        1. if flashcards set counts less than 15 flashcards
        learning set is flashcards set itself except 3rd cup

        2. if flashcards set counts 15 or more flashcards
        flashcards from 0 and 1st cup count is defined by formula
            [cups_0_and_1] = [all flashcards in the set] // 3 + 1
        and maximum count for flashcards in 0 cup is defined by formula
            [max_cup_0] = [cups_0_and_1] // 3 + 1
        learning set is firsly filled up with up to [max_cup_0] flashcards
        from 0 cup and then filled up with flashcards from 1st cup
        until [cups_0_and_1] flashcards in learning set. Rest of the learning
        set is filled up with flashcards from 2nd cup.

        Raises:
            error.EmptySetError: if flashcards set is empty
            error.EmptySetError: if all flashcards are learnt

        Returns:
            FlashcardsSet: learning set
        """
        if self.is_empty():
            raise error.EmptySetError(
                'Cannot create learning set. Set is empty.')
        elif self.get_learning_status() == self.len():
            raise error.EmptySetError(
                'Cannot create learning set.'
                and 'All flashcards are in learnt status'
            )

        # Accessing number of flashcard in the set
        flashcards_count = self.len()

        if flashcards_count < 15:
            # If flashcards set counts less than 15 flashcards
            # learning set is flashcards set itself except 3rd cup
            cup_3 = self.get_flashcards_cup(3)
            learning_set = FlashcardsSet(
                '[Learning set]',
                [
                    flashcard for flashcard in self.flashcards
                    if flashcard not in cup_3
                ])
            return learning_set
        else:
            # Creating learning set
            learning_set = FlashcardsSet('[Learning set]')
            # Defining count for flashcards from 0 and 1st cups
            cups_0_1_count = flashcards_count // 3 + 1
            # Defining max count of 0 cup
            cup_0_count_max = cups_0_1_count // 3 + 1

            # 1. Filling learning set up to max count with flashcards
            #    that are in zero cup
            cup_0 = self.get_flashcards_cup(0)
            if len(cup_0) < cup_0_count_max:
                for flashcard in cup_0:
                    learning_set.add_flashcard(flashcard)
            else:
                for flashcard in random.sample(cup_0, cup_0_count_max):
                    learning_set.add_flashcard(flashcard)

            # 2. Filling learning set up to 2/3 with flashcards
            #    that are in 1st cup
            cup_1 = self.get_flashcards_cup(1)
            # - Defining cup 2 count
            cup_2_count = cups_0_1_count - learning_set.len()
            if len(cup_1) < cup_2_count:
                for flashcard in cup_1:
                    learning_set.add_flashcard(flashcard)
            else:
                for flashcard in random.sample(cup_1, cup_2_count):
                    learning_set.add_flashcard(flashcard)

            # 3. Filling rest of the learning set with flashcards that are in
            #    2nd cup
            cup_2 = self.get_flashcards_cup(2)
            for flashcard in cup_2:
                learning_set.add_flashcard(flashcard)

            return learning_set

    def get_flashcards_cup(self, learning_cup: int) -> list[Flashcard]:
        """Returns list of flashcards that are in given cup.

        Args:
            learning_cup (int): number of cup

        Returns:
            list[Flashcard]: list of flashcards from given learning cup
        """
        flashcards_cup = [
            flashcard for flashcard in self.flashcards
            if flashcard.learning_cup == learning_cup
        ]
        return flashcards_cup

    def get_learning_status(self) -> int:
        """Returns number of already lernt flashcards
        from opened flashcards set.

        Returns:
            int: number of lernt flashcards
        """
        learnt_fladhcards_count = sum(
            [flashcard.is_learned() for flashcard in self.flashcards])
        return learnt_fladhcards_count

    def get_learning_progress(self) -> tuple[int, int]:
        """Returns learning progress computed according to the algorihm:

        [current number of progress points] =
            [one progress point for every flashcard in first cup ]+
            [two progress points for every flashcard in second cup]+
            [three progress point for every flashcard in first cup]

       [all possible points] = 3 * [flashcards count]

        Returns:
            tuple[int, int]: ([current number of progress points],
                [all possible points])
        """
        all_points = 3 * self.len()
        three_points = 3 * len(self.get_flashcards_cup(3))
        two_points = 2 * len(self.get_flashcards_cup(2))
        one_point = 1 * len(self.get_flashcards_cup(1))
        return (one_point + two_points + three_points, all_points)

    def is_learned(self) -> bool:
        """Returns True if set is learned

        Returns:
            bool: True if set is learned
        """
        return self.get_learning_status() == self.len()

    def reset_learning_progress(self) -> None:
        """Resets learning progress"""
        for flashcard in self.flashcards:
            flashcard.learning_cup = 0


class TestItem():
    """Test Item used for checking knowledge about one flashcard.
    """
    def __init__(self, flashcard: Flashcard, mode: int = 0) -> None:
        """Creates an instance of test item which tests knowledge about one
        flashcard.

        Args:
            flashcard (Flashcard): _description_
            mode (int, optional): mode = 0 - expected answer is flashcard's
            definition, mode = 1 - expected answer is flashcard's phrase.
            Defaults to 0.
        """

        self._flashcard: Flashcard = flashcard
        self._opened: bool = False
        self._question: str | None = None
        self._answer: str | None = None
        self._setup(mode)
        self._user_answer: str | None = None

    def _setup(self, mode: int) -> None:
        """Setups mode of the test item

        Args:
            mode (int): mode = 0 - expected answer is flashcard's
            definition, mode = 1 - expected answer is flashcard's phrase.

        Raises:
            error.InvalidTestItemMode: if mode not integer in range [0, 1]
        """
        if mode not in [0, 1]:
            raise error.InvalidTestItemMode(
                'Cannot create test item. Incorrect mode.')
        match mode:
            case 0:
                self._question = self._flashcard.phrase
                self._answer = self._flashcard.definition

            case 1:
                self._question = self._flashcard.definition
                self._answer = self._flashcard.phrase

    def get_flashcard(self) -> Flashcard:
        """Returns flashcard used to create test item

        Returns:
            Flashcard: flashcard
        """
        return self._flashcard

    def open(self) -> None:
        """Opens test item
        """
        self._opened = True

    def is_opened(self) -> bool:
        """Returns true if test item is opened.

        Returns:
            bool: True if test item is opened
        """
        return self._opened

    def get_question(self) -> str:
        """Returns question if test item is opened

        Raises:
            error.ClosedTestItemError: if test is not opened

        Returns:
            str: question
        """
        if self._opened:
            return self._question
        else:
            raise error.ClosedTestItemError(
                'Cannot access question. Test item is closed.')

    def set_answer(self, answer: str) -> None:
        """If test item is opened sets answer.

        Args:
            answer (str): answer to the question

        Raises:
            error.ClosedTestItemError: if test is not opened
        """
        if self._opened:
            self._user_answer = answer
        else:
            raise error.ClosedTestItemError(
                'Cannot change the answer. Test item is closed.')

    def result(self) -> bool:
        """Closes test item and return true if answear is correct
        and false if incorrect.

        Returns:
            bool: True if answear is correct
            and False if incorrect.
        """
        self._opened = False
        return self._answer == self._user_answer


class Test():
    """Represents test that consists of test items
    """
    def __init__(self, flashcards_set: FlashcardsSet, mode: int = 0) -> None:
        """Creates an instance of a test for given flashcards set

        Args:
            flashcards_set (FlashcardsSet): _description_
            mode (int, optional): mode = 0 - expected answer is flashcard's
            definition, mode = 1 - expected answer is flashcard's phrase.
            Defaults to 0.

        Raises:
            error.EmptySetError: if given flashcards set is empty
        """
        if flashcards_set.is_empty():
            raise error.EmptySetError(
                'Cannot create a test. Empty flashcards set.')
        self._flashcards_set: FlashcardsSet = flashcards_set
        self._mode: int = mode
        self._test_items: list[TestItem] = self._generateTestItems()
        self._running: bool = None
        self._start_time: float | None = None
        self._end_time: float | None = None

    def _generateTestItems(self) -> list[TestItem]:
        """Returns list of test items (list of excecises).

        Returns:
            list[TestItem]: test items
        """
        test_items = []
        for flashcard in self._flashcards_set._flashcards:
            test_items.append(TestItem(flashcard, mode=self._mode))
        return test_items

    def name(self) -> str:
        """Returns name of the flashcard set used to create test.

        Returns:
            str: name of the flashcards set
        """
        return self._flashcards_set.name

    def start(self) -> None:
        """Starts the test and starts timer
        """
        self._running = True
        self._start_time = time.time()
        for test_item in self._test_items:
            test_item.open()

    def close(self) -> None:
        """Closes the test and stops timer.
        """
        self._running = False
        self._end_time = time.time()

    def is_started(self) -> bool:
        """Returns True if test is running.

        Returns:
            bool: True if test is running
        """
        return self._running

    def is_finished(self) -> bool:
        """Returns True if test has start time and is not running

        Returns:
            bool: True if test is finished
        """
        if self._start_time and not self._running:
            return True

    def get_test(self) -> list[TestItem]:
        """Returns list of test items.

        Returns:
            list[TestItem]: test items
        """

        return self._test_items

    def result(self) -> TestResult:
        """Closes test and returns TestResult object.

        Returns:
            TestResult: results of the test
        """
        self.close()
        return TestResult(self)

    def time(self) -> float:
        """If test is running returns seconds since the test has started.
        If test has finished returns duration of the test.

        Raises:
            error.TestNotStartedError: it test has not started ever

        Returns:
            float: time since the test has started (if not finished)
            or duration of the test (if finished)
        """
        if not self._start_time:
            raise error.TestNotStartedError(
                'Cannot get test time. Test has not started yet.')

        if self._running:
            return time.time() - self._start_time
        else:
            return self._end_time - self._start_time


class TestResult():
    """Provides information about test result.
    """
    def __init__(self, test: Test) -> None:
        """Creates an isntance of TestResult

        Args:
            test (Test): obiekt testu

        Raises:
            error.TestNotFinishedError: if test is not finished
        """
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
        """Computes count of correct, incorrect and all answers
        """
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
        """Computes duration of the test and average time spent on question.
        """
        # Accessing duration of the test
        self._duration = self._test.time()
        # Computing acerage time spent on question
        self._time_per_question = self._duration / self._questions_count

    def get_correct_answers_count(self) -> int:
        """Returns count of correct answers

        Returns:
            int: correct answers count
        """
        return self._correct_answers

    def get_incorrect_answers_count(self) -> int:
        """Returns count of incorrect answers

        Returns:
            int: incorrect answers count
        """
        return self._incorrect_answers

    def get_questions_count(self) -> int:
        """Returns count of all questions

        Returns:
            int: all questions in test count
        """
        return self._questions_count

    def get_accuracy(self) -> float:
        """Returns accuracy of test in %.

        Returns:
            float: accuracy in test [0.0, 100.0]
        """
        return self._accuracy

    def get_duration(self) -> float:
        """Returs duration of the test in seconds.

        Returns:
            float: duration of the test (seconds)
        """
        return self._duration

    def get_time_per_question(self) -> float:
        """Returns average time spent on one question

        Returns:
            float: average time spent on question (seconds)
        """
        return self._time_per_question


class Session():
    """Stores information about current learning session.
    """
    def __init__(self, username: str) -> None:
        """Creates an instace of Session object

        Args:
            username (str): user name
        """
        self.username: str = username
        self._flashcards_sets: list[FlashcardsSet | None] = []
        self._opened_set: FlashcardsSet | None = None
        self._opened_flashcard: Flashcard | None = None
        self._session_stats: SessionStats = SessionStats(self)

    @property
    def username(self) -> str:
        """Returns name of user which created the session.

        Returns:
            str: username
        """
        return self._username

    @username.setter
    def username(self, new_username: str) -> None:
        """Sets username. Max 25 chars.

        Args:
            new_username (str): new username
        Raises:
            error.EmptyStringError: if new_username is empty
            error.StringTooLongError: if new_username has more than 25 chars
        """
        if not new_username:
            raise error.EmptyStringError('Username cannot be empty.')
        elif len(new_username) > 25:
            raise error.StringTooLongError(
                'Username is too long. Max 25 chars.')
        self._username = str(new_username)

    @property
    def flashcards_sets(self) -> list[FlashcardsSet | None]:
        """Returns list of flashcards sets opened in the session

        Returns:
            list[FlashcardsSet | None]: list of flashcards sets
        """
        return self._flashcards_sets

    @property
    def opened_set(self) -> FlashcardsSet:
        """Returns currently opened flashcards set

        Returns:
            FlashcardsSet: opened flashcards set
        """
        return self._opened_set

    @property
    def opened_flashcard(self) -> Flashcard:
        """Returns currently opened flashcars

        Returns:
            Flashcard: opened flashcard
        """
        return self._opened_flashcard

    def get_stats(self) -> SessionStats:
        """Returns SessionStats object with statistics
            about current session.

        Returns:
            SessionStats: statistics about session
        """
        return self._session_stats

    def add_set(self, flashcards_set: FlashcardsSet) -> None:
        """Adds given flashcards set to session.

        Args:
            flashcards_set (FlashcardsSet): flashcards set
        """
        self._flashcards_sets.append(flashcards_set)

    def remove_set(self, flashcards_set: FlashcardsSet) -> None:
        """If open closes and removes flashcards set from the session
        or removes from the session.

        Args:
            flashcards_set (FlashcardsSet): flashcards set

        Raises:
            error.SetNotInSessionError: if flashcards_set is not in the
            session
        """
        if flashcards_set not in self.flashcards_sets:
            raise error.SetNotInSessionError(
                'Given set is not in the session.')
        elif flashcards_set == self._opened_set:
            self.close_set()
        self._flashcards_sets.remove(flashcards_set)

    def open_set(self, flashcards_set: FlashcardsSet) -> None:
        """Opens given flashcards set

        Args:
            flashcards_set (FlashcardsSet): flashcards set

        Raises:
            error.SetNotInSessionError: if flashcards_set is not in the
            session
        """
        if flashcards_set not in self._flashcards_sets:
            raise error.SetNotInSessionError(
                'Given set is not in the session.')
        self._opened_set = flashcards_set

    def close_set(self) -> None:
        """Closes opened set and flashcard
        """
        self._opened_flashcard = None
        self._opened_set = None

    def open_flashcard(self, index: int) -> None:
        """Opens flashcard of given index from the opened flashcards set.

        Args:
            index (int): index of flashcard in opened set to be opened

        Raises:
            error.NotOpenedSetError: if no flashcards set is opened
            error.IndexOutOfRangeError: if given index is out of range of
            [0, flashcards count-1]
        """

        if not self._opened_set:
            raise error.NotOpenedSetError('No set is opened.')
        elif index >= self._opened_set.len() or index < 0:
            raise error.IndexOutOfRangeError()
        self._opened_flashcard = self.opened_set.flashcards[index]

    def close_flashcard(self) -> None:
        """Closes opened flashcard.
        """
        self._opened_flashcard = None

    def remove_flashcard(self, flashcard: Flashcard) -> None:
        """If flashcard is open, closes it and removes from the opened set else
        removes from the opened set.

        Args:
            flashcard (Flashcard): flashcard to be removed from opened set

        Raises:
            error.NotOpenedSetError: if no set is opened
        """
        if not self._opened_set:
            raise error.NotOpenedSetError(
                'Cannot remove flashcard. Not set is opened.')
        if flashcard == self._opened_flashcard:
            self.close_flashcard()
        self._opened_set.remove_flashcard(flashcard)

    def flashcard_index(self) -> int:
        """Returns opened flashcard's index in the flashcards set.

        Raises:
            error.NotOpenedFlashcardError: if no flashcar is opened

        Returns:
            int: index of opened flashcard
        """
        if self.opened_flashcard:
            return self._opened_set.flashcard_index(self.opened_flashcard)
        raise error.NotOpenedFlashcardError("No flashcard is opened.")

    def next_flashcard(self) -> None:
        """Opens next flashcard in the current opened set.
           If it is the last flashcard, opens the first one.

        Raises:
            error.NotOpenedFlashcardError: if no flashcard is opened
        """
        if not self.opened_flashcard:
            raise error.NotOpenedFlashcardError('No flashcard is opened.')
        new_index = (self.flashcard_index() + 1) % self.opened_set.len()
        self._opened_flashcard = self._opened_set.flashcards[new_index]

    def previous_flashcard(self) -> None:
        """Opens previous flashcard in the current opened set.
           If it is the first flashcard, opens the last one.

        Raises:
            error.NotOpenedFlashcardError: if no flashcard is opened
        """
        if not self.opened_flashcard:
            raise error.NotOpenedFlashcardError('No flashcard is opened.')
        new_index = (self.flashcard_index() - 1) % self.opened_set.len()
        self._opened_flashcard = self._opened_set.flashcards[new_index]

    def flashcard_counter_info(self) -> str:
        """Returns string with information about the index of opened flashcard
        in the form of:
        '{opened flashcard index + 1} / {number of flashcards in set}'

        Returns:
            str: '{opened flashcard index + 1} / {number of flashcards in set}'
        """
        if not self._opened_set:
            return '0 / 0'
        elif not self._opened_flashcard:
            return f'0 / {self._opened_set.len()}'
        return f'{self.flashcard_index() + 1} / {self._opened_set.len()}'
        # self.flashcard_index() + 1 to count from 1

    def generate_test(self, count: int, test_mode: int = 0) -> Test:
        """Generates a test in given mode with given count of flashcards
        from the opened flashcards set.

        Args:
            count (int): _description_
            test_mode (int, optional): mode = 0 - expected answer
            is flashcard's definition, mode = 1 - expected answer
            is flashcard's phrase. Defaults to 0.

        Raises:
            error.NotOpenedSetError: if no set is opened

        Returns:
            Test: object with generated test
        """
        if not self._opened_set:
            raise error.NotOpenedSetError(
                'Cannot generate test. No set is open.')
        # Generating flashcards set with predefined questions count
        random_set = self.opened_set.draw_flashcards(count)
        return Test(random_set, mode=test_mode)

    def learning_test(self, test_mode=0) -> Test:
        """Returns test with created learning set
        from the opened flashcards set.

        Args:
            test_mode (int, optional): mode = 0 - expected answer
            is flashcard's definition, mode = 1 - expected answer
            is flashcard's phrase. Defaults to 0.

        Raises:
            error.NotOpenedSetError: if no set is opened

        Returns:
            Test: Test object with exercises from learning set
        """
        if not self.opened_set:
            raise error.NotOpenedSetError(
                'Cannot create learning test. No set is opened.')
        learning_set = self.opened_set.create_learning_set()
        return Test(learning_set, mode=test_mode)

    def analyse_learning_result(self, learning_test: Test) -> None:
        """Analyses learning test conducted on opened flashcards set.
        Moves flashcards to new cups.

        Args:
            test (Test): test to be analysed
        """
        test_items = learning_test.get_test()
        for test_item in test_items:
            flashcard = test_item.get_flashcard()
            if test_item.result():
                flashcard.next_learning_cup()
            else:
                flashcard.previous_learning_cup()


class SessionStats():
    """Keeps information about statistics of current session.
    """
    def __init__(self, session: Session) -> None:
        """Creates an instance of SessionStats.

        Args:
            session (Session): session to be followed
        """
        self._session: Session = session
        self._start_time = time.time()

    def get_time(self) -> float:
        """Returns time in seconds since starting session.

        Returns:
            float: duration of the session in seconds
        """
        return time.time() - self._start_time

    def flashcards_sets_count(self) -> int:
        """Returns count of flashcards sets in the session.

        Returns:
            int: count of flashcards sets in session
        """
        return len(self._session.flashcards_sets)

    def flashcard_count(self) -> int:
        """Returns count of all flashcards in the session

        Returns:
            int: all flashcards in session count
        """
        flashcards_sets: list[FlashcardsSet] = self._session.flashcards_sets
        return sum([flascards_set.len() for flascards_set in flashcards_sets])
