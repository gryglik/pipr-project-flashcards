from PySide6.QtWidgets import QWidget, QDialog

from lib.ui.widgets_ui.NewFlashcardWidget_ui import Ui_NewFlashcardsWidget
from lib.ui.widgets_ui.ListFlashcardsWidget_ui import Ui_ListFlashcardsWidget
from lib.ui.widgets_ui.ListSetsWidget_ui import Ui_ListSetsWidget
from lib.ui.widgets_ui.InputTextDialog_ui import Ui_InputTextDialog
from lib.ui.widgets_ui.InputUsernameDialog_ui import Ui_InputUsernameDialog


class NewFlashcardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_NewFlashcardsWidget()
        self.ui.setupUi(self)


class ListFlashcardsWidget(QWidget):
    def __init__(self, flashcard, parent=None):
        super().__init__(parent)
        self.ui = Ui_ListFlashcardsWidget()
        self.ui.setupUi(self)
        self.flashcard = flashcard
        self.ui.fld_phrase.setText(flashcard.phrase)
        self.ui.fld_definition.setText(flashcard.definition)
        self.ui.rbtn_priority.setChecked(flashcard.priority)


class ListSetsWidget(QWidget):
    def __init__(self, flashcards_set, parent=None):
        super().__init__(parent)
        self.flashcards_set = flashcards_set
        self.ui = Ui_ListSetsWidget()
        self.ui.setupUi(self)
        self.ui.fld_set_name.setReadOnly(True)
        self.ui.fld_set_name.setText(flashcards_set.name)


class InputTextDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InputTextDialog()
        self.ui.setupUi(self)


class InputSetNameDialog(InputTextDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Create new flashcards set...')
        self.ui.label.setText('Enter name: ')
        self.ui.lineEdit.setMaxLength(50)


class InputUsernameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InputUsernameDialog()
        self.ui.setupUi(self)
        self.ui.btn_username.clicked.connect(self.accept)
