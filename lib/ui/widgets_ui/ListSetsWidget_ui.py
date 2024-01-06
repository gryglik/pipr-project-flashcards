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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QSizePolicy,
    QWidget)

from lib.ui.widgets_basic import PushButton
import resources_rc

class Ui_ListSetsWidget(object):
    def setupUi(self, ListSetsWidget):
        if not ListSetsWidget.objectName():
            ListSetsWidget.setObjectName(u"ListSetsWidget")
        ListSetsWidget.resize(451, 108)
        self.horizontalLayout = QHBoxLayout(ListSetsWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 18, 20, 20)
        self.fld_set_name = QLineEdit(ListSetsWidget)
        self.fld_set_name.setObjectName(u"fld_set_name")
        self.fld_set_name.setFrame(False)

        self.horizontalLayout.addWidget(self.fld_set_name)

        self.btn_edit_set_name = PushButton(ListSetsWidget)
        self.btn_edit_set_name.setObjectName(u"btn_edit_set_name")
        self.btn_edit_set_name.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_edit_set_name.sizePolicy().hasHeightForWidth())
        self.btn_edit_set_name.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(13)
        self.btn_edit_set_name.setFont(font)
        icon = QIcon()
        icon.addFile(u":/lib/ui/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/lib/ui/icons/ready.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_edit_set_name.setIcon(icon)
        self.btn_edit_set_name.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_edit_set_name)

        self.btn_delete_set = PushButton(ListSetsWidget)
        self.btn_delete_set.setObjectName(u"btn_delete_set")
        self.btn_delete_set.setEnabled(True)
        sizePolicy.setHeightForWidth(self.btn_delete_set.sizePolicy().hasHeightForWidth())
        self.btn_delete_set.setSizePolicy(sizePolicy)
        self.btn_delete_set.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/lib/ui/icons/thrash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_set.setIcon(icon1)
        self.btn_delete_set.setCheckable(False)

        self.horizontalLayout.addWidget(self.btn_delete_set)


        self.retranslateUi(ListSetsWidget)

        QMetaObject.connectSlotsByName(ListSetsWidget)
    # setupUi

    def retranslateUi(self, ListSetsWidget):
        ListSetsWidget.setWindowTitle(QCoreApplication.translate("ListSetsWidget", u"Form", None))
        self.btn_edit_set_name.setText("")
        self.btn_delete_set.setText("")
    # retranslateUi

