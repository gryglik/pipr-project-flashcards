from PySide6.QtWidgets import QPushButton, QErrorMessage, QWidget, QDialog


class PushButton(QPushButton):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setMinimumHeight(36)
        self.setMinimumWidth(36)


class Dialog(QDialog):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setBaseSize(400, 120)
        self.setMinimumWidth(36)


class ErrorDialog(QErrorMessage):
    def __init__(self, msg: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.showMessage(msg)
        self.exec()
