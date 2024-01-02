# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListSetsWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

from basic_widgets import MyPushButton

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(342, 44)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbl_set_name = QLabel(Form)
        self.lbl_set_name.setObjectName(u"lbl_set_name")

        self.horizontalLayout.addWidget(self.lbl_set_name)

        self.btn_edit_flashcard = MyPushButton(Form)
        self.btn_edit_flashcard.setObjectName(u"btn_edit_flashcard")
        self.btn_edit_flashcard.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_edit_flashcard.sizePolicy().hasHeightForWidth())
        self.btn_edit_flashcard.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(13)
        self.btn_edit_flashcard.setFont(font)
        icon = QIcon()
        icon.addFile(u"icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"icons/ready.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_edit_flashcard.setIcon(icon)
        self.btn_edit_flashcard.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_edit_flashcard)

        self.btn_delete_set = MyPushButton(Form)
        self.btn_delete_set.setObjectName(u"btn_delete_set")
        self.btn_delete_set.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_delete_set.sizePolicy().hasHeightForWidth())
        self.btn_delete_set.setSizePolicy(sizePolicy)
        self.btn_delete_set.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"icons/thrash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_set.setIcon(icon1)
        self.btn_delete_set.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_delete_set)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_set_name.setText("")
        self.btn_edit_flashcard.setText("")
        self.btn_delete_set.setText("")
    # retranslateUi

