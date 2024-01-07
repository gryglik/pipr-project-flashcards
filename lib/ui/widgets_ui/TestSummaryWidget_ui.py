# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestSummaryWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_TestSummaryWidget(object):
    def setupUi(self, TestSummaryWidget):
        if not TestSummaryWidget.objectName():
            TestSummaryWidget.setObjectName(u"TestSummaryWidget")
        TestSummaryWidget.resize(522, 300)
        self.gridLayout = QGridLayout(TestSummaryWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_accuracy = QLabel(TestSummaryWidget)
        self.lbl_accuracy.setObjectName(u"lbl_accuracy")
        font = QFont()
        font.setBold(True)
        self.lbl_accuracy.setFont(font)

        self.gridLayout.addWidget(self.lbl_accuracy, 0, 0, 1, 1)

        self.fld_accuracy = QLineEdit(TestSummaryWidget)
        self.fld_accuracy.setObjectName(u"fld_accuracy")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fld_accuracy.sizePolicy().hasHeightForWidth())
        self.fld_accuracy.setSizePolicy(sizePolicy)
        self.fld_accuracy.setFont(font)
        self.fld_accuracy.setFrame(False)
        self.fld_accuracy.setReadOnly(True)

        self.gridLayout.addWidget(self.fld_accuracy, 0, 1, 1, 1)

        self.lbl_question_count = QLabel(TestSummaryWidget)
        self.lbl_question_count.setObjectName(u"lbl_question_count")

        self.gridLayout.addWidget(self.lbl_question_count, 1, 0, 1, 1)

        self.fld_question_count = QLineEdit(TestSummaryWidget)
        self.fld_question_count.setObjectName(u"fld_question_count")
        sizePolicy.setHeightForWidth(self.fld_question_count.sizePolicy().hasHeightForWidth())
        self.fld_question_count.setSizePolicy(sizePolicy)
        self.fld_question_count.setFrame(False)
        self.fld_question_count.setReadOnly(True)

        self.gridLayout.addWidget(self.fld_question_count, 1, 1, 1, 1)

        self.lbl_correct_answers = QLabel(TestSummaryWidget)
        self.lbl_correct_answers.setObjectName(u"lbl_correct_answers")

        self.gridLayout.addWidget(self.lbl_correct_answers, 2, 0, 1, 1)

        self.fld_correct_answers = QLineEdit(TestSummaryWidget)
        self.fld_correct_answers.setObjectName(u"fld_correct_answers")
        sizePolicy.setHeightForWidth(self.fld_correct_answers.sizePolicy().hasHeightForWidth())
        self.fld_correct_answers.setSizePolicy(sizePolicy)
        self.fld_correct_answers.setFrame(False)
        self.fld_correct_answers.setReadOnly(True)

        self.gridLayout.addWidget(self.fld_correct_answers, 2, 1, 1, 1)

        self.lbl_incorrect_answers = QLabel(TestSummaryWidget)
        self.lbl_incorrect_answers.setObjectName(u"lbl_incorrect_answers")

        self.gridLayout.addWidget(self.lbl_incorrect_answers, 3, 0, 1, 1)

        self.fld_incorrect_answers = QLineEdit(TestSummaryWidget)
        self.fld_incorrect_answers.setObjectName(u"fld_incorrect_answers")
        sizePolicy.setHeightForWidth(self.fld_incorrect_answers.sizePolicy().hasHeightForWidth())
        self.fld_incorrect_answers.setSizePolicy(sizePolicy)
        self.fld_incorrect_answers.setFrame(False)
        self.fld_incorrect_answers.setReadOnly(True)

        self.gridLayout.addWidget(self.fld_incorrect_answers, 3, 1, 1, 1)

        self.line = QFrame(TestSummaryWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 2)

        self.lbl_time = QLabel(TestSummaryWidget)
        self.lbl_time.setObjectName(u"lbl_time")

        self.gridLayout.addWidget(self.lbl_time, 5, 0, 1, 1)

        self.fld_time = QLineEdit(TestSummaryWidget)
        self.fld_time.setObjectName(u"fld_time")
        sizePolicy.setHeightForWidth(self.fld_time.sizePolicy().hasHeightForWidth())
        self.fld_time.setSizePolicy(sizePolicy)
        self.fld_time.setFrame(False)
        self.fld_time.setReadOnly(True)

        self.gridLayout.addWidget(self.fld_time, 5, 1, 1, 1)

        self.lbl_average_time = QLabel(TestSummaryWidget)
        self.lbl_average_time.setObjectName(u"lbl_average_time")

        self.gridLayout.addWidget(self.lbl_average_time, 6, 0, 1, 1)

        self.fld_average_time = QLineEdit(TestSummaryWidget)
        self.fld_average_time.setObjectName(u"fld_average_time")
        sizePolicy.setHeightForWidth(self.fld_average_time.sizePolicy().hasHeightForWidth())
        self.fld_average_time.setSizePolicy(sizePolicy)
        self.fld_average_time.setFrame(False)
        self.fld_average_time.setReadOnly(True)

        self.gridLayout.addWidget(self.fld_average_time, 6, 1, 1, 1)


        self.retranslateUi(TestSummaryWidget)

        QMetaObject.connectSlotsByName(TestSummaryWidget)
    # setupUi

    def retranslateUi(self, TestSummaryWidget):
        TestSummaryWidget.setWindowTitle(QCoreApplication.translate("TestSummaryWidget", u"Form", None))
        self.lbl_accuracy.setText(QCoreApplication.translate("TestSummaryWidget", u"Accuracy:", None))
        self.lbl_question_count.setText(QCoreApplication.translate("TestSummaryWidget", u"Question count", None))
        self.lbl_correct_answers.setText(QCoreApplication.translate("TestSummaryWidget", u"Correct answers:", None))
        self.lbl_incorrect_answers.setText(QCoreApplication.translate("TestSummaryWidget", u"Incorrect answers:", None))
        self.lbl_time.setText(QCoreApplication.translate("TestSummaryWidget", u"Time:", None))
        self.lbl_average_time.setText(QCoreApplication.translate("TestSummaryWidget", u"Average time per question:", None))
    # retranslateUi

