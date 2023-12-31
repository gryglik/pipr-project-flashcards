from typing import Optional
from os.path import basename, splitext
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QListWidgetItem, QWidget,
    QFileDialog)
import sys

from flashcards_ui import Ui_MainWindow
from flashcards import Session, FlashcardsSet, load_from_csv
from dialogs.DialogInput_ui import Ui_DialogInput
from ListRecord_ui import Ui_ListRecord


class DialogInput(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogInput()
        self.ui.setupUi(self)

class ListRecord(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ListRecord()
        self.ui.setupUi(self)

class FlashcardWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.session = Session()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mainstack.setCurrentIndex(0)
        self._initialiseUser()

    def _initialiseUser(self):
        self.ui.btn_name.clicked.connect(self._setupUsername)

    def _initialiseSession(self):
        self.ui.lbl_greet.setText(f'Hi {self.session.user_name}.')
        self.ui.btn_new_set.clicked.connect(self._createNewSet)
        self.ui.list_sets.itemClicked.connect(self._setupFlashcards)
        self.ui.btn_import_set.clicked.connect(self._importSet)

    def _setupUsername(self):
        if self.ui.fld_name.text():
            self.session.user_name = self.ui.fld_name.text()
            self.ui.mainstack.setCurrentIndex(1)
            self._initialiseSession()

    def _setupSet(self, name=None, flashcards_set=None):
        if not flashcards_set:
            flashcards_set = FlashcardsSet(name if name else 'new set')
        item = QListWidgetItem(flashcards_set.name)
        item.flashcards_set = flashcards_set
        self.ui.list_sets.addItem(item)

    def _setupFlashcards(self, item):
        self.ui.listFlashcards.clear()
        for flashcard in item.flashcards_set.flashcards:
            new_record = QListWidgetItem()
            widget = ListRecord()
            widget.ui.fld_phrase.setText(flashcard.phrase)
            widget.ui.fld_definition.setText(flashcard.definition)
            widget.ui.rbtn_priority.setChecked(flashcard.priority)
            self.ui.listFlashcards.addItem(new_record)
            self.ui.listFlashcards.setItemWidget(new_record, widget)
            new_record.setSizeHint(widget.sizeHint())

    def _createNewSet(self):
        dlg_set_name = DialogInput(self)
        dlg_set_name.setWindowTitle('Create new flashcards set...')
        dlg_set_name.ui.label.setText('Enter name: ')
        dlg_set_name.ui.lineEdit.setMaxLength(25)
        dlg_set_name.exec()
        name = dlg_set_name.ui.lineEdit.text()
        self._setupSet(name)

    def _importSet(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open set', '~', 'Data (*.csv)')
        with open(file) as fp:
            set = load_from_csv(fp)
        set.name = splitext(basename(file))[0]
        self._setupSet(flashcards_set=set)


def guiMain(args):
    app = QApplication(args)
    window = FlashcardWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)