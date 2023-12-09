from classes import Flashcard
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
    with pytest.raises(ValueError):
        Flashcard('cat', '')
        Flashcard('', 'kot')
        Flashcard('', '')


def test_Flascard_phrase_set():
    flashcard = Flashcard('cat', 'pies')
    assert flashcard.phrase == 'cat'
    flashcard.phrase = 'dog'
    assert flashcard.phrase == 'dog'


def test_Flashcarde_phrase_set_empty():
    flashcard = Flashcard('cat', 'kot')
    assert flashcard.phrase == 'cat'
    with pytest.raises(ValueError):
        flashcard.phrase = ''


def test_Flascard_definition_set():
    flashcard = Flashcard('cat', 'pies')
    assert flashcard.definition == 'pies'
    flashcard.definition = 'kot'
    assert flashcard.definition == 'kot'


def test_Flashcarde_definition_set_empty():
    flashcard = Flashcard('cat', 'kot')
    assert flashcard.definition == 'kot'
    with pytest.raises(ValueError):
        flashcard.phrase = ''
