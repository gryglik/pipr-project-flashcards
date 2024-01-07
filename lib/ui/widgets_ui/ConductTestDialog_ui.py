# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConductTestDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from lib.ui.widgets_basic import PushButton

class Ui_ConductTestDialog(object):
    def setupUi(self, ConductTestDialog):
        if not ConductTestDialog.objectName():
            ConductTestDialog.setObjectName(u"ConductTestDialog")
        ConductTestDialog.resize(457, 287)
        ConductTestDialog.setMinimumSize(QSize(400, 0))
        ConductTestDialog.setBaseSize(QSize(600, 600))
        self.verticalLayout = QVBoxLayout(ConductTestDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_test = QLabel(ConductTestDialog)
        self.lbl_test.setObjectName(u"lbl_test")

        self.verticalLayout.addWidget(self.lbl_test)

        self.list_test = QListWidget(ConductTestDialog)
        self.list_test.setObjectName(u"list_test")

        self.verticalLayout.addWidget(self.list_test)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_check = PushButton(ConductTestDialog)
        self.btn_check.setObjectName(u"btn_check")
        self.btn_check.setMinimumSize(QSize(70, 36))

        self.horizontalLayout.addWidget(self.btn_check)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ConductTestDialog)

        QMetaObject.connectSlotsByName(ConductTestDialog)
    # setupUi

    def retranslateUi(self, ConductTestDialog):
        self.lbl_test.setText(QCoreApplication.translate("ConductTestDialog", u"Test", None))
        self.btn_check.setText(QCoreApplication.translate("ConductTestDialog", u"Check", None))
        pass
    # retranslateUi

