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


class Export():
    """Export object responsible for exporting data from file"""
    def __init__(self) -> None:
        """Creates an instance of Export object"""
        pass

    def _writeFlashcardsSetToCsv(
            self, flashcards_set: FlashcardsSet, fp: TextIO) -> None:
        """Writes flashcards set to the given csv file object"""
        writer = csv.DictWriter(fp, ['phrase', 'definition', 'priority'])
        writer.writeheader()
        for flashcard in flashcards_set.flashcards:
            writer.writerow({
                'phrase': flashcard.phrase,
                'definition': flashcard.definition,
                'priority': flashcard.priority
            })

    def write_flashcards_set_to_csv(
            self, flashcards_set: FlashcardsSet, directory: str) -> None:
        """Saves flashcards set to csv file in given path"""
        with open(f'{directory}/{flashcards_set.name}.csv', 'w') as fp:
            self._writeFlashcardsSetToCsv(flashcards_set, fp)
