from PySide6.QtWidgets import QWidget

from NewFlashcardWidget_ui import Ui_NewFlashcardsWidget
from ListFlashcardsWidget_ui import Ui_ListFlashcardsWidget
from ListSetsWidget_ui import Ui_ListSetsWidget


class NewFlashcardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewFlashcardsWidget()
        self.ui.setupUi(self)


class ListFlashcardsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ListFlashcardsWidget()
        self.ui.setupUi(self)


class ListSetsWidget(QWidget):
    def __init__(self, flashcards_set, parent=None):
        super().__init__(parent)
        self.flashcards_set = flashcards_set
        self.ui = Ui_ListSetsWidget()
        self.ui.setupUi(self)
        self.ui.lbl_set_name.setText(flashcards_set.name)
