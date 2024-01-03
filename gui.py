from typing import Optional
from os.path import basename, splitext
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QListWidgetItem, QWidget,
    QFileDialog, QPushButton)
import sys

from flashcards_ui import Ui_MainWindow
from flashcards_logic import Session, FlashcardsSet, Flashcard, load_from_csv
from dialogs.DialogInput_ui import Ui_DialogInput
from widgets import ListFlashcardsWidget, ListSetsWidget


class DialogInput(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogInput()
        self.ui.setupUi(self)


class FlashcardWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.session = None
        # ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mainstack.setCurrentIndex(0)
        # starting program
        self._initialiseUser()

    def _initialiseUser(self):
        """Gather information to initialise session"""
        self.ui.btn_name.clicked.connect(self._setupUsername)

    def _setupUsername(self):
        username = self.ui.fld_name.text()
        if username:
            self._initialiseSession(username)

    def _initialiseSession(self, username):
        """Initialises session, handle creating/importing
           new sets, setups Flashcards list."""
        self.session = Session(username)
        self.ui.mainstack.setCurrentIndex(1)
        self.ui.lbl_greet.setText(f'Hi {self.session.username}.')
        self.ui.btn_flashcard.setText('Create/choose a set first')
        self.ui.btn_new_set.clicked.connect(self._createNewSet)
        self.ui.list_sets.itemClicked.connect(lambda item: self._initialiseSet(item.flashcards_set))
        self.ui.btn_import_set.clicked.connect(self._importSet)
        self.ui.btn_flashcard.clicked.connect(self._loadFlashcard)
        self.ui.btn_next_flashcard.clicked.connect(self._nextFlashcard)
        self.ui.btn_previous_flashcard.clicked.connect(self._previousFlashcard)
        self.ui.widget_new_flashcard.ui.btn_add_flashcard.clicked.connect(self._createNewFlashcard)
        self.ui.widget_new_flashcard.ui.btn_cancel_flashcard.clicked.connect(self._eraseNewFlashcard)

    def _createNewSet(self):
        """Responsible for creating new set."""
        dlg_set_name = DialogInput(self)
        dlg_set_name.setWindowTitle('Create new flashcards set...')
        dlg_set_name.ui.label.setText('Enter name: ')
        dlg_set_name.ui.lineEdit.setMaxLength(50)
        dlg_set_name.exec()
        name = dlg_set_name.ui.lineEdit.text()
        self.session.add_set(FlashcardsSet(name))
        self._setupListSets()

    def _importSet(self):
        """Responsible for importing set from csv file."""
        file, _ = QFileDialog.getOpenFileName(self, 'Open set', '~', 'Data (*.csv)')
        with open(file) as fp:
            set = load_from_csv(fp)
        set.name = splitext(basename(file))[0]
        self.session.add_set(set)
        self._setupListSets()

    def _setupListSets(self):
        """Updates sets list"""
        self.ui.list_sets.clear()
        for flashcards_set in self.session.flashcards_sets:
            widget = ListSetsWidget(flashcards_set)
            list_sets_item = QListWidgetItem()
            self.ui.list_sets.addItem(list_sets_item)
            self.ui.list_sets.setItemWidget(list_sets_item, widget)
            list_sets_item.setSizeHint(widget.sizeHint())
            list_sets_item.setFlags(list_sets_item.flags() ^ Qt.ItemFlag.ItemIsSelectable)
            list_sets_item.flashcards_set = flashcards_set

    def _initialiseSet(self, flashcards_set):
        """Opens set"""
        self.ui.list_flashcards.clear()
        # reference to opened flashcards set
        self.session.opened_set: FlashcardsSet = flashcards_set

        # 1. Initialising flashcard slider
        self.ui.flashcard.index = 0
        if len(self.session.opened_set.flashcards):
            self.ui.btn_flashcard.setEnabled(True)
            self.ui.btn_previous_flashcard.setEnabled(True)
            self.ui.btn_next_flashcard.setEnabled(True)
            self._loadFlashcard()

        # 2. Initialising new flashcard widget
        self.ui.widget_new_flashcard.ui.fld_phrase.setEnabled(True)
        self.ui.widget_new_flashcard.ui.fld_definition.setEnabled(True)
        self.ui.widget_new_flashcard.ui.rbtn_priority.setEnabled(True)
        self.ui.widget_new_flashcard.ui.btn_add_flashcard.setEnabled(True)
        self.ui.widget_new_flashcard.ui.btn_cancel_flashcard.setEnabled(True)

        # 3. Initialising list of flashcards
        for flashcard in flashcards_set.flashcards:
            # creating set list item
            list_flashcards_item = QListWidgetItem()
            widget = ListFlashcardsWidget()
            widget.flashcard = flashcard
            widget.ui.fld_phrase.setText(flashcard.phrase)
            widget.ui.fld_definition.setText(flashcard.definition)
            widget.ui.rbtn_priority.setChecked(flashcard.priority)
            self.ui.list_flashcards.addItem(list_flashcards_item)
            self.ui.list_flashcards.setItemWidget(list_flashcards_item, widget)
            list_flashcards_item.setSizeHint(widget.sizeHint())
            list_flashcards_item.setFlags(list_flashcards_item.flags() ^ Qt.ItemFlag.ItemIsSelectable)
            # binding actions to buttons
            widget.ui.btn_edit_flashcard.clicked.connect(self._editFlashcard)
            widget.ui.btn_delete_flashcard.clicked.connect(self._deleteFlashcard)

    def _loadFlashcard(self, clicked=False):
        flashcard_index = self.ui.flashcard.index
        self.ui.lbl_flashcard_count.setText(f'{flashcard_index+1} / {len(self.session.opened_set.flashcards)}')
        if not clicked:
            self.ui.btn_flashcard.setChecked(clicked)
            self.ui.btn_flashcard.setText(self.session.opened_set.flashcards[flashcard_index].phrase)
        else:
            self.ui.btn_flashcard.setChecked(clicked)
            self.ui.btn_flashcard.setText(self.session.opened_set.flashcards[flashcard_index].definition)

    def _nextFlashcard(self):
        index = self.ui.flashcard.index
        self.ui.flashcard.index = (index + 1) % len(self.session.opened_set.flashcards)
        self._loadFlashcard()

    def _previousFlashcard(self):
        index = self.ui.flashcard.index
        self.ui.flashcard.index = (index - 1) % len(self.session.opened_set.flashcards)
        self._loadFlashcard()

    def _createNewFlashcard(self):
        btn_create_new_flashcard = self.sender()
        widget = btn_create_new_flashcard.parent()
        try:
            flashcard = Flashcard(
                widget.ui.fld_phrase.text(),
                widget.ui.fld_definition.text(),
                widget.ui.rbtn_priority.isChecked()
            )
            self.session.opened_set.add_flashcard(flashcard)
        except Exception as e:
            print(e)
        self._eraseNewFlashcard()
        self._initialiseSet(self.session.opened_set)

    def _eraseNewFlashcard(self):
        self.ui.widget_new_flashcard.ui.fld_definition.setText('')
        self.ui.widget_new_flashcard.ui.fld_phrase.setText('')
        self.ui.widget_new_flashcard.ui.rbtn_priority.setEnabled(False)

    def _editFlashcard(self, checked):
        btn_edit_flashcard = self.sender()
        list_flashcards_item: QListWidgetItem = btn_edit_flashcard.parent()
        list_flashcards_item.ui.fld_phrase.setReadOnly(not checked)
        list_flashcards_item.ui.fld_definition.setReadOnly(not checked)
        list_flashcards_item.ui.rbtn_priority.setEnabled(checked)
        if not checked:
            flashcard = list_flashcards_item.flashcard
            try:
                flashcard.phrase = list_flashcards_item.ui.fld_phrase.text()
                flashcard.definition = list_flashcards_item.ui.fld_definition.text()
                flashcard.priority = list_flashcards_item.ui.rbtn_priority.isChecked()
            except Exception as e:
                print(e)
            self._initialiseSet(self.session.opened_set)

    def _deleteFlashcard(self):
        btn_delete_flashcard = self.sender()
        list_flashcards_widget: ListFlashcardsWidget = btn_delete_flashcard.parent()
        flashcard: Flashcard = list_flashcards_widget.flashcard
        flashcards_set: FlashcardsSet = self.session.opened_set
        flashcards_set.remove_flashcard(flashcard)
        self._initialiseSet(self.session.opened_set)

def guiMain(args):
    app = QApplication(args)
    window = FlashcardWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)