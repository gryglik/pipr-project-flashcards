# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListTestWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QSizePolicy,
    QWidget)

class Ui_ListTestWidget(object):
    def setupUi(self, ListTestWidget):
        if not ListTestWidget.objectName():
            ListTestWidget.setObjectName(u"ListTestWidget")
        ListTestWidget.resize(569, 45)
        self.horizontalLayout = QHBoxLayout(ListTestWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fld_question = QLineEdit(ListTestWidget)
        self.fld_question.setObjectName(u"fld_question")
        self.fld_question.setFrame(False)
        self.fld_question.setReadOnly(True)

        self.horizontalLayout.addWidget(self.fld_question)

        self.fld_answer = QLineEdit(ListTestWidget)
        self.fld_answer.setObjectName(u"fld_answer")
        self.fld_answer.setFrame(False)

        self.horizontalLayout.addWidget(self.fld_answer)


        self.retranslateUi(ListTestWidget)

        QMetaObject.connectSlotsByName(ListTestWidget)
    # setupUi

    def retranslateUi(self, ListTestWidget):
        ListTestWidget.setWindowTitle(QCoreApplication.translate("ListTestWidget", u"Form", None))
        self.fld_answer.setPlaceholderText(QCoreApplication.translate("ListTestWidget", u"answer...", None))
    # retranslateUi

