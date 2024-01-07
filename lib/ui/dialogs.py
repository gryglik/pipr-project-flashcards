from PySide6.QtWidgets import QWidget, QDialog, QListWidgetItem
from PySide6.QtCore import Qt

from lib.ui.widgets_ui.InputTextDialog_ui import Ui_InputTextDialog
from lib.ui.widgets_ui.InputUsernameDialog_ui import Ui_InputUsernameDialog
from lib.ui.widgets_ui.CreateTestDialog_ui import Ui_CreateTestDialog
from lib.ui.widgets_ui.ConductTestDialog_ui import Ui_ConductTestDialog
from lib.ui.widgets import ListTestWidget, TestSummaryWidget
from lib.ui.widgets_basic import Dialog

from flashcards_logic import Test, TestItem


class InputTextDialog(Dialog):
    """Dialog with one label and field."""
    def __init__(self, parent: QWidget | None = None) -> None:
        """Creates an instance of InputTextDialog"""
        super().__init__(parent)
        # Setuing ui
        self.ui = Ui_InputTextDialog()
        self.ui.setupUi(self)


class InputSetNameDialog(InputTextDialog):
    """Dialog to retrieve set name."""
    def __init__(self, parent: QWidget | None = None) -> None:
        """Creates an instance of InputSetName."""
        super().__init__(parent)
        # Setuping ui
        self.setWindowTitle('Create new flashcards set...')
        self.ui.label.setText('Enter name: ')
        self.ui.lineEdit.setMaxLength(50)


class GenerateTestDialog(Dialog):
    """Dialog to retrieve information to generate test."""
    def __init__(self, parent: QWidget | None = None) -> None:
        """Dialog creates an instance of GenerateTestDialog."""
        super().__init__(parent)
        # Setuping ui
        self.ui = Ui_CreateTestDialog()
        self.ui.setupUi(self)
        self.setWindowTitle('Generating new test...')
        self.ui.btn_create_test.clicked.connect(self.accept)


class ConductTestDialog(Dialog):
    """Dialog to conduct a test."""
    def __init__(self, test: Test, parent: QWidget | None = None) -> None:
        """Creates an test dialog which conducts test for given Test object."""
        super().__init__(parent)
        self.test: Test = test
        # Initialising ui
        self.ui: Ui_ConductTestDialog = self._initialiseUi()
        # Setuping test
        self._setupTest()
        # Binding actions to buttons
        self.ui.btn_check.clicked.connect(self._testResult)

    def _initialiseUi(self) -> Ui_ConductTestDialog:
        """Initialises ui."""
        self.setWindowTitle(f'Flashcards - TEST - {self.test.name()}')
        ui = Ui_ConductTestDialog()
        ui.setupUi(self)
        ui.lbl_test.setText(f'Test - {self.test.name()}')
        return ui

    def _setupTest(self):
        """Starts test and show questions"""
        # Starting test
        self.test.start()
        for test_item in self.test.get_test():
            # Setuping test item of list
            list_test_item = QListWidgetItem()
            list_test_item.setFlags(
                list_test_item.flags() ^ Qt.ItemFlag.ItemIsSelectable)
            self.ui.list_test.addItem(list_test_item)
            # Setuping item using widget
            widget = ListTestWidget(test_item, parent=self.ui.list_test)
            self.ui.list_test.setItemWidget(list_test_item, widget)
            list_test_item.setSizeHint(widget.sizeHint())
            # Asigning widget to list_test_item
            list_test_item.widget: ListTestWidget = widget

    def _testResult(self) -> None:
        """Gathers answers and returns result of the test."""
        # Gathering answers
        self._checkAnswers()
        # Setuping test summary
        self._setupTestSummary()
        # Setuping closing button
        self.ui.btn_check.setText('Close')
        self.ui.btn_check.clicked.disconnect(self._testResult)
        self.ui.btn_check.clicked.connect(self.accept)

    def _checkAnswers(self) -> None:
        """Collects entered answers and setups TestItem(s) holded
        by the list widget."""
        # Creating list of the TetsItem(s) widgets
        list_test_widgets: list[ListTestWidget] = []
        for row in range(self.ui.list_test.count()):
            # Accessing QListWidgetItem
            list_test_item: QListWidgetItem = self.ui.list_test.item(row)
            # Accessing ListTestWidget
            list_test_widget: ListTestWidget = list_test_item.widget
            list_test_widgets.append(list_test_widget)

        for widget in list_test_widgets:
            # Disabling editing
            widget.ui.fld_answer.setReadOnly(True)
            # Accessing TestItem
            test_item: TestItem = widget.test_item
            # Setuping answer
            user_answer: str = widget.ui.fld_answer.text()
            test_item.set_answer(user_answer)
            # Setuping ui
            if not test_item.result():
                widget.ui.fld_answer.setStyleSheet(
                    'border-bottom-color: red;')
            else:
                widget.ui.fld_answer.setStyleSheet(
                    'border-bottom-color: green;')

    def _setupTestSummary(self) -> None:
        """Setups and adds summary widget with results to the test list."""
        # Setuping the item of list
        list_summary_item: QListWidgetItem = QListWidgetItem()
        list_summary_item.setFlags(
                list_summary_item.flags() ^ Qt.ItemFlag.ItemIsSelectable)
        self.ui.list_test.addItem(list_summary_item)
        # Setuping item using widget
        summary_widget: TestSummaryWidget = TestSummaryWidget(self.test)
        self.ui.list_test.setItemWidget(list_summary_item, summary_widget)
        list_summary_item.setSizeHint(summary_widget.sizeHint())


class InputUsernameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_InputUsernameDialog()
        self.ui.setupUi(self)
        self.ui.btn_username.clicked.connect(self.accept)
