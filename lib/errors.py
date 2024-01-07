class EmptyStringError(Exception):
    """Raised when trying to set string empty."""
    pass


class FlashcardNotInSetError(Exception):
    """Raised when trying to access the flashcard that is not in the set."""
    pass


class StringTooLongError(Exception):
    """Raised when string extends char limit."""
    pass


class SetNotInSessionError(Exception):
    """Raised when trying to access the set that is not in the session."""
    pass


class NotOpenedSetError(Exception):
    """Raised when trying to access the opened set, but no set is opened."""
    pass


class NotOpenedFlashcardError(Exception):
    """Raised when trying to access the opened flashcard
       but no flashcard is opened."""


class IndexOutOfRangeError(IndexError):
    """Raised when trying to access an an ivalid index of the list."""
    pass


class InvalidFlashcardError(Exception):
    """Raised when trying to load invalid flashcard from the file."""
    pass


class ClosedTestItemError(Exception):
    """Raised when trying to get question or set answer of closed
       test item."""
    pass


class TestNotStartedError(Exception):
    """Raised when trying to access data that is available
    only after test start."""
    pass


class TestNotFinishedError(Exception):
    """Raised when trying to access data from Test that is available
    only when test is finished."""
    pass