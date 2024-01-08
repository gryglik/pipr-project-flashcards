import sys
import time
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QListWidgetItem, QFileDialog)

from lib.ui.flashcards_ui import Ui_MainWindow
from lib.ui.widgets_basic import PushButton, ErrorDialog
from lib.ui.widgets import (
    ListSetsWidget, ListFlashcardsWidget)
from lib.ui.dialogs import (
    InputSetNameDialog, InputUsernameDialog, GenerateTestDialog,
    ConductTestDialog, StartIntelligentTestDialog)

from flashcards_logic import (
    Session, SessionStats, FlashcardsSet, Flashcard, Test)

from flashcards_io import Import, Export


class FlashcardWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui: Ui_MainWindow = self._initialiseUi()
        self.session: Session = self._initialiseSession()
        self.setWindowTitle(f'Flashcards - {self.session.username}')
        self._initialiseHomePage()
        # Initialising first flashcards set
        self.session.add_set(FlashcardsSet('My first set.'))
        self._setupListSets()
        # Initialising home page
        self._initialiseHomePage()

    def _initialiseSession(self) -> Session:
        """Initialises session."""
        session = None
        # Trying to create a session
        while not session:
            try:
                session = Session(self._getUsername())
                return session
            except Exception as e:
                ErrorDialog(str(e), parent=self)

    def _getUsername(self) -> str:
        """Returns username provided by the user."""
        # Opening dialog
        dlg_get_username = InputUsernameDialog(parent=self)
        dlg_get_username.exec()
        # Closing application if rejected dialog
        if not dlg_get_username.result():
            sys.exit()
        # Getting username value
        username = dlg_get_username.ui.fld_username.text()
        return username

    def _initialiseUi(self) -> Ui_MainWindow:
        """Initialises GUI."""
        # Creating and setuping main window
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.stack_1.setCurrentIndex(0)
        # Binding buttons to methods
        # - Home button
        ui.btn_homepage.clicked.connect(self._setupHomePage)
        # - Managing flashcards sets
        ui.btn_new_set.clicked.connect(self._createNewSet)
        ui.btn_import_set.clicked.connect(self._importSet)
        ui.btn_export_set.clicked.connect(self._exportSet)
        ui.list_sets.itemClicked.connect(
            lambda item: self._setupFlashcardsSetPage(item.flashcards_set))
        # - Previewing flashcards
        ui.btn_flashcard.clicked.connect(self._loadFlashcard)
        ui.btn_reverse.toggled.connect(self._setupSliderFlashcards)
        ui.btn_previous_flashcard.clicked.connect(self._previousFlashcard)
        ui.btn_next_flashcard.clicked.connect(self._nextFlashcard)
        # - Creating new flashcard
        ui.widget_new_flashcard.ui.btn_add_flashcard.clicked.connect(
            self._createNewFlashcard)
        ui.widget_new_flashcard.ui.btn_cancel_flashcard.clicked.connect(
            self._eraseNewFlashcard)
        # - Generating test
        ui.btn_generate_test.clicked.connect(self._generateTest)
        # - Starting intelligent learning
        ui.btn_learn.clicked.connect(self._startIntelligentLearning)
        return ui

    def _initialiseHomePage(self) -> None:
        """Initialisises home page."""
        self.ui.stack_1.setCurrentIndex(0)
        self.ui.lbl_greet.setText(f'Hi {self.session.username}')
        self._setupStats()

    def _setupHomePage(self) -> None:
        """Refreshes home page."""
        # Closing set
        self.session.close_set()
        # Refreshing sets list
        self._setupListSets()
        # Refreshing statisticcs
        self._setupStats()
        # Changing page
        self.ui.stack_1.setCurrentIndex(0)

    def _setupStats(self) -> None:
        """Refreshes statics widget on home page."""
        # Accessing statistics
        stats: SessionStats = self.session.get_stats()
        # Setuping statistics in ui
        self.ui.fld_sets_count.setText(f'{stats.flashcards_sets_count()}')
        self.ui.fld_flashcards_count.setText(f'{stats.flashcard_count()}')
        # - formating time
        session_time = stats.get_time()
        session_time_str: str = time.strftime(
            '%H:%M', time.gmtime(session_time))
        # Setuping time in ui
        self.ui.fld_time.setText(session_time_str)

    def _setupListSets(self) -> None:
        """Refreshes flashcards sets list and setups home page"""
        # Clearing list of flashcards sets
        self.ui.list_sets.clear()
        # Adding flashcards sets to the list
        for flashcards_set in self.session.flashcards_sets:
            # Creating item of list of flashcards set
            list_sets_item = QListWidgetItem()
            list_sets_item.flashcards_set: FlashcardsSet = flashcards_set
            # list_sets_item.setFlags(
            #     list_sets_item.flags() ^ Qt.ItemFlag.ItemIsSelectable)
            self.ui.list_sets.addItem(list_sets_item)
            # Setuping Item using widget
            widget = ListSetsWidget(flashcards_set, parent=self.ui.list_sets)
            self.ui.list_sets.setItemWidget(list_sets_item, widget)
            list_sets_item.setSizeHint(widget.sizeHint())
            # Binding actions to buttons
            widget.ui.btn_edit_set_name.clicked.connect(self._editSetName)
            widget.ui.btn_delete_set.clicked.connect(self._deleteSet)
            # Setuping selection if set is opened
            if flashcards_set == self.session.opened_set:
                list_sets_item.setSelected(True)
        # Updating statistics
        self._setupStats()

    def _editSetName(self, checked: bool) -> None:
        """If checked enables editing set's name provided by sender's parent,
           if not checked saves set name changes."""
        # Determining sender
        btn_edit_set_name: PushButton = self.sender()
        # Determining sender's parent
        list_sets_widget: ListSetsWidget = btn_edit_set_name.parent()
        # Accessing flashcards set
        flashcards_set: FlashcardsSet = list_sets_widget.flashcards_set
        # If not checked trying to change set name
        if not checked:
            try:
                flashcards_set.name = list_sets_widget.ui.fld_set_name.text()
                # Refreshing set list
                self._setupListSets()
            except Exception as e:
                ErrorDialog(e, parent=list_sets_widget)
        # If not checked disables editing
        list_sets_widget.ui.fld_set_name.setReadOnly(not checked)

    def _deleteSet(self) -> None:
        """If clicked removes flashcards provided by the sender's parent
           from the session."""
        # Determining sender
        btn_delete_set: PushButton = self.sender()
        # Determining sender's parent
        list_sets_widget: ListSetsWidget = btn_delete_set.parent()
        # Accessing flashcards set
        flashcards_set: FlashcardsSet = list_sets_widget.flashcards_set
        try:
            self.session.remove_set(flashcards_set)
        except Exception as e:
            ErrorDialog(str(e), parent=list_sets_widget)
        # Setuping home page if removed opened set
        if not self.session.opened_set:
            self._setupHomePage()
        else:
            self._setupListSets()

    def _createNewSet(self) -> None:
        """Creates a new set and refreshes sets list."""
        # Opening dialog
        dlg_set_name = InputSetNameDialog(self)
        dlg_set_name.exec()
        # Getting set name value
        set_name = dlg_set_name.ui.lineEdit.text()
        # Adding a new flashcards set to flashcards sets in session
        if dlg_set_name.result():
            try:
                self.session.add_set(FlashcardsSet(set_name))
            except Exception as e:
                ErrorDialog(str(e), parent=self)
        # Refreshing flashcards sets list
        return self._setupListSets()

    def _importSet(self) -> None:
        """Responsible for importing set from csv file."""
        # Opening dialog and getting file path
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Open set..', '~', 'Data (*.csv)')
        # Trying to import flashcards set to session
        try:
            import_obj = Import()
            flashcards_set = import_obj.load_flashcards_set_from_csv(file_path)
            self.session.add_set(flashcards_set)
        except Exception as e:
            ErrorDialog(str(e), parent=self)
        # Refreshing flashcards sets list
        return self._setupListSets()

    def _exportSet(self) -> None:
        """Responsible for exporting opened set to the csv file."""
        # Accessing the opened flashcards set
        flashcards_set: FlashcardsSet = self.session.opened_set
        # Opening dialog to get directory
        directory = QFileDialog.getExistingDirectory(self, 'Save set...')
        # Trying to save flashcards set
        try:
            export_obj = Export()
            export_obj.write_flashcards_set_to_csv(flashcards_set, directory)
        except Exception as e:
            ErrorDialog(str(e))

    def _setupFlashcardsSetPage(self, flashcards_set: FlashcardsSet) -> None:
        """Setups GUI to show given flashcards set."""
        # 1. Clearing list of flashcards
        self.ui.list_flashcards.clear()
        # 2. Updating current opened set reference in session
        try:
            self.session.open_set(flashcards_set)
            # 3. Initialising flashcards slider
            self._setupSliderFlashcards()
            # 4. Initialising list of flashcards
            self._setupListFlashcards()
        except Exception as e:
            ErrorDialog(str(e), parent=self.ui.list_flashcards)
        # 5. Changing home page -> set page
        self.ui.stack_1.setCurrentIndex(1)

    def _createNewFlashcard(self) -> None:
        """Creates new flashcard from the data given sender's parent widget
           and adds it to opened flashcards set."""
        # Determining the sender
        btn_create_new_flashcard: PushButton = self.sender()
        # Determining the sender's parent
        widget: ListFlashcardsWidget = btn_create_new_flashcard.parent()
        try:
            flashcard = Flashcard(
                widget.ui.fld_phrase.text(),
                widget.ui.fld_definition.text(),
                widget.ui.btn_priority.isChecked()
            )
            self.session.opened_set.add_flashcard(flashcard)
        except Exception as e:
            ErrorDialog(str(e), parent=widget)
        # Erasing widget
        self._eraseNewFlashcard()
        # Refreshing Flashcards page
        self._setupFlashcardsSetPage(self.session.opened_set)

    def _eraseNewFlashcard(self) -> None:
        """Erases widget responsible for creating new flashcard."""
        self.ui.widget_new_flashcard.ui.fld_definition.setText('')
        self.ui.widget_new_flashcard.ui.fld_phrase.setText('')
        self.ui.widget_new_flashcard.ui.btn_priority.setChecked(False)

    def _setupSliderFlashcards(self) -> None:
        """Setups first flashcard on slider."""
        if not self.session.opened_set.is_empty():
            if not self.session.opened_flashcard:
                self.session.open_flashcard(0)
            self._loadFlashcard(clicked=False)
        else:
            # Updating flashcard counter
            self.ui.lbl_flashcard_count.setText(
                self.session.flashcard_counter_info())
            # Setuping blank flashcard
            self.ui.btn_flashcard.setText('Create flashcard first')

        self.ui.btn_flashcard.setEnabled(
            not self.session.opened_set.is_empty())
        self.ui.btn_next_flashcard.setEnabled(
            not self.session.opened_set.is_empty())
        self.ui.btn_previous_flashcard.setEnabled(
            not self.session.opened_set.is_empty())

    def _loadFlashcard(self, clicked: bool = False) -> None:
        """Loads opened flashcard to slider"""
        # Updating flashcard counter
        self.ui.lbl_flashcard_count.setText(
                self.session.flashcard_counter_info())
        if self.session.opened_flashcard:
            # Setuping flashcard mode >clicked<
            self.ui.btn_flashcard.setChecked(clicked)
            # Determining reversion
            reversed = self.ui.btn_reverse.isChecked()
            if clicked == reversed:
                self.ui.btn_flashcard.setText(
                    self.session.opened_flashcard.phrase)
            else:
                self.ui.btn_flashcard.setText(
                    self.session.opened_flashcard.definition)

    def _nextFlashcard(self) -> None:
        """Loads next flashcard to slider."""
        self.session.next_flashcard()
        # Refreshing slider
        return self._loadFlashcard()

    def _previousFlashcard(self) -> None:
        """Loads previous flashcard to slider."""
        self.session.previous_flashcard()
        # Refreshing slider
        self._loadFlashcard()

    def _setupListFlashcards(self) -> None:
        """Refreshes flashcards list."""
        # Adding flashcards
        for flashcard in self.session.opened_set.flashcards:
            # Creating item of list of flashcards
            list_flashcards_item = QListWidgetItem()
            list_flashcards_item.setFlags(
                list_flashcards_item.flags() ^ Qt.ItemFlag.ItemIsSelectable)
            self.ui.list_flashcards.addItem(list_flashcards_item)
            # Setuping item using widget
            widget = ListFlashcardsWidget(
                flashcard, parent=self.ui.list_flashcards)
            self.ui.list_flashcards.setItemWidget(list_flashcards_item, widget)
            list_flashcards_item.setSizeHint(widget.sizeHint())
            # Binding actions to buttons
            widget.ui.btn_edit_flashcard.clicked.connect(self._editFlashcard)
            widget.ui.btn_delete_flashcard.clicked.connect(
                self._deleteFlashcard)

    def _editFlashcard(self, checked: bool) -> None:
        """If checked enables editing flashcards provided by sender's parent
           widget.
           If not checked saves flashcards changes."""
        # Determining the sender
        btn_edit_flashcard: PushButton = self.sender()
        # Determining the sender's parent
        parent = btn_edit_flashcard.parent()
        list_flashcards_item: ListFlashcardsWidget = parent
        # Enabling editing if checked
        # and disabling editing if not chcecked
        list_flashcards_item.ui.fld_phrase.setReadOnly(not checked)
        list_flashcards_item.ui.fld_definition.setReadOnly(not checked)
        list_flashcards_item.ui.btn_priority.setEnabled(checked)
        # If not checked saving flashcards changes
        if not checked:
            flashcard: Flashcard = list_flashcards_item.flashcard
            new_phrase = list_flashcards_item.ui.fld_phrase.text()
            new_definition = list_flashcards_item.ui.fld_definition.text()
            new_priority = list_flashcards_item.ui.btn_priority.isChecked()
            try:
                flashcard.phrase = new_phrase
                flashcard.definition = new_definition
                flashcard.priority = new_priority
            except Exception as e:
                ErrorDialog(str(e), parent=list_flashcards_item)
            # Refreshing Flashcards page
            self._setupFlashcardsSetPage(self.session.opened_set)

    def _deleteFlashcard(self) -> None:
        """Removes flashcards provided by sender's parent widget from
           the opened flashcards set."""
        # Determining sender
        btn_delete_flashcard = self.sender()
        # Determining sender's parent
        sender_parent = btn_delete_flashcard.parent()
        list_flashcards_widget: ListFlashcardsWidget = sender_parent
        # Accesing flashcard
        flashcard: Flashcard = list_flashcards_widget.flashcard
        # Trying to remove flashcard from the flashcards set
        try:
            self.session.remove_flashcard(flashcard)
        except Exception as e:
            ErrorDialog(str(e), parent=list_flashcards_widget)
        # Refreshing flashcards page
        self._setupFlashcardsSetPage(self.session.opened_set)

    def _generateTest(self) -> None:
        """Generates test and conducts it."""
        # Gathering data to create test
        try:
            test_setup = self._getTestSetup()
        except Exception as e:
            ErrorDialog(e)
        if test_setup:
            question_count, mode = test_setup
            # Trying to generate test
            try:
                test = self.session.generate_test(
                    question_count, test_mode=mode)
                self._conductTest(test)
            except Exception as e:
                ErrorDialog(str(e))

    def _getTestSetup(self) -> tuple[int, int] | None:
        """Opens dialog and returns test setup parameters."""
        # Creating dialog to get questions count and mode
        dlg_test_setup = GenerateTestDialog(parent=self)
        # If window was closed return none
        if not dlg_test_setup.exec():
            return None
        # Accessing question count
        question_count = dlg_test_setup.ui.spnbx_questions_number.value()
        # Accessing mode
        mode = dlg_test_setup.ui.combx_quesion_mode.currentIndex()
        return question_count, mode

    def _conductTest(self, test: Test) -> bool:
        """Opens dialog and conducts test."""
        try:
            dlg_test = ConductTestDialog(test, parent=self)
            dlg_test.exec()
        except Exception as e:
            ErrorDialog(str(e))
        return dlg_test.result()

    def _startIntelligentLearning(self) -> None:
        """Conducts test with learning set provided by the opened
        flashcards set.
        """
        # Getting setup of the Intelligent Learning
        mode, result = self._getIntelligentLearningSetup()

        conducted = False
        if result:
            try:
                # Creating learning test
                learning_test = self.session.learning_test(test_mode=mode)
                conducted = self._conductTest(learning_test)
            except Exception as e:
                ErrorDialog(str(e))

        # Saving test result
        if conducted:
            try:
                self.session.analyse_learning_result(learning_test)
                self.session.opened_set.set_learned_today()
            except Exception as e:
                ErrorDialog(str(e))

    def _getIntelligentLearningSetup(self) -> tuple[int, int]:
        """Get setup of the intelligent learning session
        """
        try:
            dlg_start_learning = StartIntelligentTestDialog(
                self.session.opened_set, parent=self)
            dlg_start_learning.exec()
        except Exception as e:
            ErrorDialog(str(e))
        # Accessing mode
        mode = dlg_start_learning.ui.combx_quesion_mode.currentIndex()
        # Accessing result
        result = dlg_start_learning.result()
        return mode, result


def guiMain(args):
    app = QApplication(args)
    window = FlashcardWindow()
    window.show()
    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
