from PySide6.QtWidgets import QPushButton


class MyPushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(36)
        self.setMinimumWidth(36)
