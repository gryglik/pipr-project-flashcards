# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewFlashcardWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QRadioButton,
    QSizePolicy, QWidget)

from lib.ui.widgets_basic import PushButton
import resources_rc

class Ui_NewFlashcardsWidget(object):
    def setupUi(self, NewFlashcardsWidget):
        if not NewFlashcardsWidget.objectName():
            NewFlashcardsWidget.setObjectName(u"NewFlashcardsWidget")
        NewFlashcardsWidget.resize(499, 48)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewFlashcardsWidget.sizePolicy().hasHeightForWidth())
        NewFlashcardsWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(NewFlashcardsWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fld_phrase = QLineEdit(NewFlashcardsWidget)
        self.fld_phrase.setObjectName(u"fld_phrase")
        self.fld_phrase.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fld_phrase.sizePolicy().hasHeightForWidth())
        self.fld_phrase.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(16)
        self.fld_phrase.setFont(font)
        self.fld_phrase.setMaxLength(50)
        self.fld_phrase.setFrame(False)

        self.horizontalLayout.addWidget(self.fld_phrase)

        self.fld_definition = QLineEdit(NewFlashcardsWidget)
        self.fld_definition.setObjectName(u"fld_definition")
        self.fld_definition.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.fld_definition.sizePolicy().hasHeightForWidth())
        self.fld_definition.setSizePolicy(sizePolicy1)
        self.fld_definition.setFont(font)
        self.fld_definition.setMaxLength(50)
        self.fld_definition.setFrame(False)

        self.horizontalLayout.addWidget(self.fld_definition)

        self.rbtn_priority = QRadioButton(NewFlashcardsWidget)
        self.rbtn_priority.setObjectName(u"rbtn_priority")
        self.rbtn_priority.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rbtn_priority.sizePolicy().hasHeightForWidth())
        self.rbtn_priority.setSizePolicy(sizePolicy2)
        self.rbtn_priority.setCheckable(True)
        self.rbtn_priority.setChecked(False)

        self.horizontalLayout.addWidget(self.rbtn_priority)

        self.btn_add_flashcard = PushButton(NewFlashcardsWidget)
        self.btn_add_flashcard.setObjectName(u"btn_add_flashcard")
        self.btn_add_flashcard.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_add_flashcard.sizePolicy().hasHeightForWidth())
        self.btn_add_flashcard.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(13)
        self.btn_add_flashcard.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/lib/ui/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_flashcard.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_add_flashcard)

        self.btn_cancel_flashcard = PushButton(NewFlashcardsWidget)
        self.btn_cancel_flashcard.setObjectName(u"btn_cancel_flashcard")
        self.btn_cancel_flashcard.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.btn_cancel_flashcard.sizePolicy().hasHeightForWidth())
        self.btn_cancel_flashcard.setSizePolicy(sizePolicy3)
        self.btn_cancel_flashcard.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/lib/ui/icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel_flashcard.setIcon(icon1)
        self.btn_cancel_flashcard.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_cancel_flashcard)


        self.retranslateUi(NewFlashcardsWidget)

        QMetaObject.connectSlotsByName(NewFlashcardsWidget)
    # setupUi

    def retranslateUi(self, NewFlashcardsWidget):
        NewFlashcardsWidget.setWindowTitle(QCoreApplication.translate("NewFlashcardsWidget", u"Form", None))
        self.fld_phrase.setPlaceholderText(QCoreApplication.translate("NewFlashcardsWidget", u"phrase", None))
        self.fld_definition.setPlaceholderText(QCoreApplication.translate("NewFlashcardsWidget", u"definition", None))
        self.rbtn_priority.setText("")
        self.btn_add_flashcard.setText("")
        self.btn_cancel_flashcard.setText("")
    # retranslateUi

