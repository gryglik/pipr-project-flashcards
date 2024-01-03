from PySide6.QtWidgets import QWidget, QDialog

from lib.ui.widgets_ui.NewFlashcardWidget_ui import Ui_NewFlashcardsWidget
from lib.ui.widgets_ui.ListFlashcardsWidget_ui import Ui_ListFlashcardsWidget
from lib.ui.widgets_ui.ListSetsWidget_ui import Ui_ListSetsWidget
from lib.ui.widgets_ui.InputTextDialog_ui import Ui_InputTextDialog


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


class InputTextDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InputTextDialog
        self.ui.setupUi(self)
