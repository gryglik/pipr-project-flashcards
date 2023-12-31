# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListRecord.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_ListRecord(object):
    def setupUi(self, ListRecord):
        if not ListRecord.objectName():
            ListRecord.setObjectName(u"ListRecord")
        self.horizontalLayout = QHBoxLayout(ListRecord)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fld_phrase = QLineEdit(ListRecord)
        self.fld_phrase.setObjectName(u"fld_phrase")
        self.fld_phrase.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fld_phrase.sizePolicy().hasHeightForWidth())
        self.fld_phrase.setSizePolicy(sizePolicy)
        self.fld_phrase.setMaxLength(50)
        self.fld_phrase.setFrame(True)
        self.fld_phrase.setReadOnly(True)

        self.horizontalLayout.addWidget(self.fld_phrase)

        self.fld_definition = QLineEdit(ListRecord)
        self.fld_definition.setObjectName(u"fld_definition")
        self.fld_definition.setEnabled(True)
        sizePolicy.setHeightForWidth(self.fld_definition.sizePolicy().hasHeightForWidth())
        self.fld_definition.setSizePolicy(sizePolicy)
        self.fld_definition.setMaxLength(50)
        self.fld_definition.setFrame(True)
        self.fld_definition.setReadOnly(True)

        self.horizontalLayout.addWidget(self.fld_definition)

        self.rbtn_priority = QRadioButton(ListRecord)
        self.rbtn_priority.setObjectName(u"rbtn_priority")
        self.rbtn_priority.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rbtn_priority.sizePolicy().hasHeightForWidth())
        self.rbtn_priority.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.rbtn_priority)

        self.btn_edit = QPushButton(ListRecord)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btn_edit.sizePolicy().hasHeightForWidth())
        self.btn_edit.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u"icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit.setIcon(icon)
        self.btn_edit.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_edit)


        self.retranslateUi(ListRecord)

        QMetaObject.connectSlotsByName(ListRecord)
    # setupUi

    def retranslateUi(self, ListRecord):
        ListRecord.setWindowTitle(QCoreApplication.translate("ListRecord", u"Form", None))
        self.fld_phrase.setText("")
        self.rbtn_priority.setText("")
        self.btn_edit.setText("")
    # retranslateUi

