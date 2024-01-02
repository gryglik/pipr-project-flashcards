from flashcards import Flashcard, FlashcardsSet
from flashcards import (
    EmptyFieldError, NotAFlashcardError, FlascardNotInSetError,
    StringTooLongError
    )
from flashcards import load_from_csv
import pytest


def test_Flascard_create_typical():
    flashcard = Flashcard('cat', 'kot', True)
    assert flashcard.phrase == 'cat'
    assert flashcard.definition == 'kot'
    assert flashcard.priority


def test_Flashcard_create_no_priority():
    flascard = Flashcard('cat', 'kot')
    assert flascard.phrase == 'cat'
    assert flascard.definition == 'kot'
    assert not flascard.priority


def test_Flascard_create_empty_phrase_or_definition():
    with pytest.raises(EmptyFieldError):
        Flashcard('cat', '')
        Flashcard('', 'kot')
        Flashcard('', '')


def test_Flashcard_phrase_set():
    flashcard = Flashcard('cat', 'pies')
    assert flashcard.phrase == 'cat'
    flashcard.phrase = 'dog'
    assert flashcard.phrase == 'dog'


def test_Flashcard_phrase_definition_set_too_long():
    string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    with pytest.raises(StringTooLongError):
        Flashcard(string, 'kot')
    with pytest.raises(StringTooLongError):
        Flashcard('cat', string)
    flashcard = Flashcard('cat', 'kot')
    with pytest.raises(StringTooLongError):
        flashcard.phrase = string
    with pytest.raises(StringTooLongError):
        flashcard.definition = string


def test_Flashcard_phrase_set_empty():
    flashcard = Flashcard('cat', 'kot')
    assert flashcard.phrase == 'cat'
    with pytest.raises(EmptyFieldError):
        flashcard.phrase = ''


def test_Flashcard_definition_set():
    flashcard = Flashcard('cat', 'pies')
    assert flashcard.definition == 'pies'
    flashcard.definition = 'kot'
    assert flashcard.definition == 'kot'


def test_Flashcard_definition_set_empty():
    flashcard = Flashcard('cat', 'kot')
    assert flashcard.definition == 'kot'
    with pytest.raises(EmptyFieldError):
        flashcard.phrase = ''


def test_FlashcardsSet_create_typical():
    flashcards = [Flashcard('cat', 'kot'),
                  Flashcard('dog', 'pies')]
    flashcards_set = FlashcardsSet('set1', flashcards)
    assert flashcards_set.name == 'set1'
    assert flashcards_set.flashcards[0].phrase == 'cat'


def test_FlashcardsSet_create_empty_name():
    flashcards = [Flashcard('cat', 'kot'),
                  Flashcard('dog', 'pies')]
    with pytest.raises(EmptyFieldError):
        FlashcardsSet('', flashcards)


def test_FlashcardsSet_too_long_name():
    string = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    with pytest.raises(StringTooLongError):
        FlashcardsSet(string)
    with pytest.raises(StringTooLongError):
        flashcards_set = FlashcardsSet('set1')
        flashcards_set.name = string


def test_FlashcardsSet_create_no_flashcards():
    flashcards_set = FlashcardsSet('empty_set')
    assert flashcards_set.name == 'empty_set'
    assert not len(flashcards_set.flashcards)


def test_FlashcardsSet_create_with_not_a_Flashcard():
    flashcards = [Flashcard('cat', 'kot'),
                  ('dog', 'pies')]
    with pytest.raises(NotAFlashcardError):
        FlashcardsSet('set1', flashcards)


def test_FlashcardsSet_add_Flashcard():
    flashcards = [Flashcard('cat', 'kot'),
                  Flashcard('dog', 'pies')]
    flashcards_set = FlashcardsSet('set1', flashcards)
    assert flashcards_set.flashcards[1].phrase == 'dog'
    assert flashcards_set.flashcards[1].definition == 'pies'
    new_flashcard = Flashcard('cow', 'krowa')
    flashcards_set.add_flashcard(new_flashcard)
    assert flashcards_set.flashcards[2].phrase == 'cow'
    assert flashcards_set.flashcards[2].definition == 'krowa'


def test_FlashcardsSet_add_not_a_Flashcard():
    flashcards = [Flashcard('cat', 'kot'),
                  Flashcard('dog', 'pies')]
    flashcards_set = FlashcardsSet('set1', flashcards)
    assert flashcards_set.flashcards[1].phrase == 'dog'
    assert flashcards_set.flashcards[1].definition == 'pies'
    new_flashcard = ('cow', 'krowa')
    with pytest.raises(NotAFlashcardError):
        flashcards_set.add_flashcard(new_flashcard)


def test_FlashcardSet_remove_Flashcard():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcards_set = FlashcardsSet('set1', [flashcard1, flashcard2])
    assert len(flashcards_set.flashcards) == 2
    flashcards_set.remove_flashcard(flashcard1)
    assert len(flashcards_set.flashcards) == 1
    assert flashcards_set.flashcards[0] == flashcard2


def test_FlascardSet_remove_not_existing_flashcard():
    flashcard1 = Flashcard('cat', 'kot')
    flashcard2 = Flashcard('dog', 'pies')
    flashcards_set = FlashcardsSet('set1', [flashcard1, flashcard2])
    assert len(flashcards_set.flashcards) == 2
    with pytest.raises(FlascardNotInSetError):
        flashcards_set.remove_flashcard(Flashcard('cow', 'krowa'))


def test_load_from_csv_typical():
    with open('tests/test.csv') as fp:
        flascards_set = load_from_csv(fp)
    assert flascards_set.flashcards[0].phrase == 'cat'
    assert flascards_set.flashcards[0].definition == 'kot'
    assert not flascards_set.flashcards[0].priority
    assert flascards_set.flashcards[1].priority
