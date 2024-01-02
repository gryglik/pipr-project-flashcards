from PySide6.QtWidgets import QWidget, QPushButton

from NewFlashcardWidget_ui import Ui_NewFlashcardsWidget
from ListFlashcardsWidget_ui import Ui_ListFlashcardsWidget


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
