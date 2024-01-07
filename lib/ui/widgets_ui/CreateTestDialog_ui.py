# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateTestDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QSizePolicy, QSpinBox, QWidget)

from lib.ui.widgets_basic import PushButton

class Ui_CreateTestDialog(object):
    def setupUi(self, CreateTestDialog):
        if not CreateTestDialog.objectName():
            CreateTestDialog.setObjectName(u"CreateTestDialog")
        CreateTestDialog.resize(284, 83)
        self.gridLayout = QGridLayout(CreateTestDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_questions = QLabel(CreateTestDialog)
        self.lbl_questions.setObjectName(u"lbl_questions")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_questions.sizePolicy().hasHeightForWidth())
        self.lbl_questions.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.lbl_questions, 0, 0, 1, 1)

        self.spnbx_questions_number = QSpinBox(CreateTestDialog)
        self.spnbx_questions_number.setObjectName(u"spnbx_questions_number")
        self.spnbx_questions_number.setFrame(True)
        self.spnbx_questions_number.setMinimum(1)

        self.gridLayout.addWidget(self.spnbx_questions_number, 0, 1, 1, 1)

        self.btn_create_test = PushButton(CreateTestDialog)
        self.btn_create_test.setObjectName(u"btn_create_test")
        self.btn_create_test.setMinimumSize(QSize(120, 36))

        self.gridLayout.addWidget(self.btn_create_test, 1, 1, 1, 1)


        self.retranslateUi(CreateTestDialog)

        QMetaObject.connectSlotsByName(CreateTestDialog)
    # setupUi

    def retranslateUi(self, CreateTestDialog):
        CreateTestDialog.setWindowTitle(QCoreApplication.translate("CreateTestDialog", u"Dialog", None))
        self.lbl_questions.setText(QCoreApplication.translate("CreateTestDialog", u"Number of questions", None))
        self.btn_create_test.setText(QCoreApplication.translate("CreateTestDialog", u"Generate test", None))
    # retranslateUi

