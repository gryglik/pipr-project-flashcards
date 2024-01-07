import time
from PySide6.QtWidgets import QWidget

from lib.ui.widgets_ui.NewFlashcardWidget_ui import Ui_NewFlashcardsWidget
from lib.ui.widgets_ui.ListFlashcardsWidget_ui import Ui_ListFlashcardsWidget
from lib.ui.widgets_ui.ListSetsWidget_ui import Ui_ListSetsWidget
from lib.ui.widgets_ui.ListTestWidget_ui import Ui_ListTestWidget
from lib.ui.widgets_ui.TestSummaryWidget_ui import Ui_TestSummaryWidget

from flashcards_logic import Flashcard, FlashcardsSet, Test, TestItem


class NewFlashcardWidget(QWidget):
    """Widget providing data to create new flashcard."""
    def __init__(self, parent: QWidget | None = None) -> None:
        """Creates an instance of NewFlashcardWidget."""
        super().__init__(parent)
        # Setuping ui
        self.ui = Ui_NewFlashcardsWidget()
        self.ui.setupUi(self)


class ListSetsWidget(QWidget):
    """Widget representing flashcards set"""
    def __init__(
            self, flashcards_set: FlashcardsSet,
            parent: QWidget | None = None) -> None:
        """Creates an instance of ListSetsWidget"""
        super().__init__(parent)
        # Asigning flashcards set to the widget
        self.flashcards_set: FlashcardsSet = flashcards_set
        # Setuping ui
        self.ui = Ui_ListSetsWidget()
        self.ui.setupUi(self)
        # Loading data
        self.ui.fld_set_name.setReadOnly(True)
        self.ui.fld_set_name.setText(flashcards_set.name)


class ListFlashcardsWidget(QWidget):
    """Widget representing flashcard data."""
    def __init__(
            self, flashcard: Flashcard, parent: QWidget | None = None) -> None:
        """Creates an instace of ListFlashcardsWidget"""
        super().__init__(parent)
        # Asigning flashcard to the widget
        self.flashcard: Flashcard = flashcard
        # Setuping ui
        self.ui: Ui_ListFlashcardsWidget = Ui_ListFlashcardsWidget()
        self.ui.setupUi(self)
        # Loading data
        self.ui.fld_phrase.setText(flashcard.phrase)
        self.ui.fld_definition.setText(flashcard.definition)
        self.ui.rbtn_priority.setChecked(flashcard.priority)


class ListTestWidget(QWidget):
    """Widget representing test item data"""
    def __init__(
            self, test_item: TestItem, parent: QWidget | None = None) -> None:
        """Creates an instance of ListTestWidget"""
        super().__init__(parent)
        # Asigning test item to the widget
        self.test_item: TestItem = test_item
        # Setuping ui
        self.ui = Ui_ListTestWidget()
        self.ui.setupUi(self)
        # Loading data
        self.ui.fld_question.setText(test_item.get_question())


class TestSummaryWidget(QWidget):
    """Widget representing test summary"""
    def __init__(self, test: Test, parent: QWidget | None = None) -> None:
        """Creates test summary widget from given Test object."""
        super().__init__(parent)
        # Setuping ui
        self.ui = Ui_TestSummaryWidget()
        self.ui.setupUi(self)
        # Loading data
        test_results = test.result()
        # Setuping widget - results
        self.ui.fld_accuracy.setText(
            f'{test_results.get_accuracy():.2f} %')
        self.ui.fld_question_count.setText(
            f'{test_results.get_questions_count()}')
        self.ui.fld_correct_answers.setText(
            f'{test_results.get_correct_answers_count()}')
        self.ui.fld_incorrect_answers.setText(
            f'{test_results.get_incorrect_answers_count()}')
        # - Converting duration to str
        duration = test_results.get_duration()
        duration_str = time.strftime('%H:%M:%S', time.gmtime(duration))
        # - Converting time per question to str
        time_per_question = test_results.get_time_per_question()
        time_per_question_str = time.strftime(
            '%H:%M:%S', time.gmtime(time_per_question))
        # Setuping widget - time
        self.ui.fld_time.setText(f'{duration_str}')
        self.ui.fld_average_time.setText(f'{time_per_question_str}')
