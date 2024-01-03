# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListFlashcardsWidget.ui'
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

class Ui_ListFlashcardsWidget(object):
    def setupUi(self, ListFlashcardsWidget):
        if not ListFlashcardsWidget.objectName():
            ListFlashcardsWidget.setObjectName(u"ListFlashcardsWidget")
        ListFlashcardsWidget.resize(461, 44)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ListFlashcardsWidget.sizePolicy().hasHeightForWidth())
        ListFlashcardsWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(ListFlashcardsWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fld_phrase = QLineEdit(ListFlashcardsWidget)
        self.fld_phrase.setObjectName(u"fld_phrase")
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
        self.fld_phrase.setReadOnly(True)

        self.horizontalLayout.addWidget(self.fld_phrase)

        self.fld_definition = QLineEdit(ListFlashcardsWidget)
        self.fld_definition.setObjectName(u"fld_definition")
        self.fld_definition.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.fld_definition.sizePolicy().hasHeightForWidth())
        self.fld_definition.setSizePolicy(sizePolicy1)
        self.fld_definition.setFont(font)
        self.fld_definition.setMaxLength(50)
        self.fld_definition.setFrame(False)
        self.fld_definition.setReadOnly(True)

        self.horizontalLayout.addWidget(self.fld_definition)

        self.rbtn_priority = QRadioButton(ListFlashcardsWidget)
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

        self.btn_edit_flashcard = PushButton(ListFlashcardsWidget)
        self.btn_edit_flashcard.setObjectName(u"btn_edit_flashcard")
        self.btn_edit_flashcard.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_edit_flashcard.sizePolicy().hasHeightForWidth())
        self.btn_edit_flashcard.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setPointSize(13)
        self.btn_edit_flashcard.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/lib/ui/icons/ui/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"icons/ready.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_edit_flashcard.setIcon(icon)
        self.btn_edit_flashcard.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_edit_flashcard)

        self.btn_delete_flashcard = PushButton(ListFlashcardsWidget)
        self.btn_delete_flashcard.setObjectName(u"btn_delete_flashcard")
        self.btn_delete_flashcard.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.btn_delete_flashcard.sizePolicy().hasHeightForWidth())
        self.btn_delete_flashcard.setSizePolicy(sizePolicy3)
        self.btn_delete_flashcard.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/lib/ui/icons/ui/icons/thrash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_flashcard.setIcon(icon1)
        self.btn_delete_flashcard.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_delete_flashcard)


        self.retranslateUi(ListFlashcardsWidget)

        QMetaObject.connectSlotsByName(ListFlashcardsWidget)
    # setupUi

    def retranslateUi(self, ListFlashcardsWidget):
        ListFlashcardsWidget.setWindowTitle(QCoreApplication.translate("ListFlashcardsWidget", u"Form", None))
        self.rbtn_priority.setText("")
        self.btn_edit_flashcard.setText("")
        self.btn_delete_flashcard.setText("")
    # retranslateUi

