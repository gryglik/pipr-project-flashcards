from typing import TextIO
from os.path import splitext, basename
import csv

from lib.errors import InvalidFlashcardError
from flashcards_logic import FlashcardsSet, Flashcard


class Import():
    """Import object responsible for importing data from files."""
    def __init__(self) -> None:
        """Creates an instance of import object"""
        pass

    def _loadFlashcardsSetFromCsv(
            self, fp: TextIO, name: str) -> FlashcardsSet:
        """Returns flashcards set for the given file object"""
        flashcards_set = FlashcardsSet(name)
        reader = csv.DictReader(fp)
        for record in reader:
            try:
                flashcard = Flashcard(
                    record['phrase'],
                    record['definition'],
                    priority=True if record['priority'] == 'True' else False
                )
            except Exception:
                raise InvalidFlashcardError(flashcard)
            flashcards_set.add_flashcard(flashcard)
        return flashcards_set

    def load_flashcards_set_from_csv(self, path: str) -> FlashcardsSet:
        """Returns flashcards set for the given csv file."""
        with open(path) as fp:
            name, _ = splitext(basename(path))
            return self._loadFlashcardsSetFromCsv(fp, name)
