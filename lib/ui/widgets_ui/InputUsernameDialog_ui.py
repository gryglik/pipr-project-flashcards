# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InputUsernameDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from lib.ui.widgets_basic import PushButton

class Ui_InputUsernameDialog(object):
    def setupUi(self, InputUsernameDialog):
        if not InputUsernameDialog.objectName():
            InputUsernameDialog.setObjectName(u"InputUsernameDialog")
        InputUsernameDialog.resize(194, 0)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InputUsernameDialog.sizePolicy().hasHeightForWidth())
        InputUsernameDialog.setSizePolicy(sizePolicy)
        InputUsernameDialog.setBaseSize(QSize(600, 400))
        self.verticalLayout = QVBoxLayout(InputUsernameDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_1 = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_1)

        self.container_welcome = QWidget(InputUsernameDialog)
        self.container_welcome.setObjectName(u"container_welcome")
        self.verticalLayout_4 = QVBoxLayout(self.container_welcome)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_name = QLabel(self.container_welcome)
        self.lbl_name.setObjectName(u"lbl_name")
        sizePolicy.setHeightForWidth(self.lbl_name.sizePolicy().hasHeightForWidth())
        self.lbl_name.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Futura"])
        font.setPointSize(40)
        font.setBold(False)
        self.lbl_name.setFont(font)
        self.lbl_name.setStyleSheet(u"")
        self.lbl_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_name, 0, Qt.AlignHCenter)

        self.fld_username = QLineEdit(self.container_welcome)
        self.fld_username.setObjectName(u"fld_username")
        self.fld_username.setEnabled(True)
        sizePolicy.setHeightForWidth(self.fld_username.sizePolicy().hasHeightForWidth())
        self.fld_username.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Futura"])
        font1.setPointSize(20)
        self.fld_username.setFont(font1)
        self.fld_username.setFocusPolicy(Qt.StrongFocus)
        self.fld_username.setMaxLength(50)
        self.fld_username.setFrame(False)
        self.fld_username.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.fld_username, 0, Qt.AlignHCenter)

        self.btn_username = PushButton(self.container_welcome)
        self.btn_username.setObjectName(u"btn_username")
        self.btn_username.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_username.sizePolicy().hasHeightForWidth())
        self.btn_username.setSizePolicy(sizePolicy1)
        self.btn_username.setMinimumSize(QSize(80, 36))
        self.btn_username.setSizeIncrement(QSize(0, 0))
        self.btn_username.setBaseSize(QSize(0, 0))
        font2 = QFont()
        font2.setFamilies([u"Futura"])
        font2.setPointSize(6)
        self.btn_username.setFont(font2)
        self.btn_username.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_4.addWidget(self.btn_username, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.container_welcome)

        self.verticalSpacer_3 = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(InputUsernameDialog)

        QMetaObject.connectSlotsByName(InputUsernameDialog)
    # setupUi

    def retranslateUi(self, InputUsernameDialog):
        InputUsernameDialog.setWindowTitle(QCoreApplication.translate("InputUsernameDialog", u"Flashcards - Login", None))
        self.lbl_name.setText(QCoreApplication.translate("InputUsernameDialog", u"Hi,", None))
        self.fld_username.setPlaceholderText(QCoreApplication.translate("InputUsernameDialog", u"Enter your name...", None))
        self.btn_username.setText(QCoreApplication.translate("InputUsernameDialog", u"Go", None))
    # retranslateUi

