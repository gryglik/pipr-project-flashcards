# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InputTextDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_InputTextDialog(object):
    def setupUi(self, InputTextDialog):
        if not InputTextDialog.objectName():
            InputTextDialog.setObjectName(u"InputTextDialog")
        InputTextDialog.resize(400, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InputTextDialog.sizePolicy().hasHeightForWidth())
        InputTextDialog.setSizePolicy(sizePolicy)
        InputTextDialog.setMinimumSize(QSize(400, 100))
        InputTextDialog.setMaximumSize(QSize(400, 100))
        self.gridLayout = QGridLayout(InputTextDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(InputTextDialog)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(InputTextDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        font = QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setFrame(False)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(InputTextDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)


        self.retranslateUi(InputTextDialog)
        self.buttonBox.accepted.connect(InputTextDialog.accept)
        self.buttonBox.rejected.connect(InputTextDialog.reject)

        QMetaObject.connectSlotsByName(InputTextDialog)
    # setupUi

    def retranslateUi(self, InputTextDialog):
        InputTextDialog.setWindowTitle(QCoreApplication.translate("InputTextDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("InputTextDialog", u"TextLabel", None))
    # retranslateUi

