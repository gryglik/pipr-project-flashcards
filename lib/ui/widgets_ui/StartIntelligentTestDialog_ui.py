# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartIntelligentTestDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QProgressBar, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from lib.ui.widgets_basic import PushButton

class Ui_StartIntelligentTestDialog(object):
    def setupUi(self, StartIntelligentTestDialog):
        if not StartIntelligentTestDialog.objectName():
            StartIntelligentTestDialog.setObjectName(u"StartIntelligentTestDialog")
        StartIntelligentTestDialog.resize(500, 403)
        StartIntelligentTestDialog.setMinimumSize(QSize(500, 300))
        StartIntelligentTestDialog.setBaseSize(QSize(500, 300))
        self.verticalLayout_2 = QVBoxLayout(StartIntelligentTestDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.learning_widget = QWidget(StartIntelligentTestDialog)
        self.learning_widget.setObjectName(u"learning_widget")
        self.verticalLayout = QVBoxLayout(self.learning_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.learning_widget)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.learning_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.lbl_info = QLabel(self.learning_widget)
        self.lbl_info.setObjectName(u"lbl_info")
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.lbl_info.setFont(font)
        self.lbl_info.setWordWrap(True)

        self.verticalLayout.addWidget(self.lbl_info)


        self.verticalLayout_2.addWidget(self.learning_widget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.progressBar = QProgressBar(StartIntelligentTestDialog)
        self.progressBar.setObjectName(u"progressBar")

        self.verticalLayout_2.addWidget(self.progressBar)

        self.label_3 = QLabel(StartIntelligentTestDialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_5 = QLabel(StartIntelligentTestDialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.widget_mode_intelligent_test = QWidget(StartIntelligentTestDialog)
        self.widget_mode_intelligent_test.setObjectName(u"widget_mode_intelligent_test")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_mode_intelligent_test)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, -1, -1, -1)
        self.lbl_question_mode = QLabel(self.widget_mode_intelligent_test)
        self.lbl_question_mode.setObjectName(u"lbl_question_mode")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_question_mode.sizePolicy().hasHeightForWidth())
        self.lbl_question_mode.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.lbl_question_mode)

        self.combx_quesion_mode = QComboBox(self.widget_mode_intelligent_test)
        self.combx_quesion_mode.addItem("")
        self.combx_quesion_mode.addItem("")
        self.combx_quesion_mode.setObjectName(u"combx_quesion_mode")

        self.horizontalLayout_2.addWidget(self.combx_quesion_mode)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.widget_mode_intelligent_test)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_reset = PushButton(StartIntelligentTestDialog)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setMinimumSize(QSize(100, 36))

        self.horizontalLayout.addWidget(self.btn_reset)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_start = PushButton(StartIntelligentTestDialog)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setMinimumSize(QSize(100, 36))

        self.horizontalLayout.addWidget(self.btn_start)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(StartIntelligentTestDialog)

        QMetaObject.connectSlotsByName(StartIntelligentTestDialog)
    # setupUi

    def retranslateUi(self, StartIntelligentTestDialog):
        self.label.setText(QCoreApplication.translate("StartIntelligentTestDialog", u"Welcome to the Intelligent Learning Mode. Keep coming back here to train and see your progress in learning. ", None))
        self.label_2.setText(QCoreApplication.translate("StartIntelligentTestDialog", u"In Intelligent Learning Mode you will be provided with test containing specially selected questions to make your learning process impressively effective. ", None))
        self.lbl_info.setText(QCoreApplication.translate("StartIntelligentTestDialog", u"You havn't done test today, do it.", None))
        self.label_3.setText(QCoreApplication.translate("StartIntelligentTestDialog", u"progress", None))
        self.label_5.setText(QCoreApplication.translate("StartIntelligentTestDialog", u"mode:", None))
        self.lbl_question_mode.setText(QCoreApplication.translate("StartIntelligentTestDialog", u"Answer with:", None))
        self.combx_quesion_mode.setItemText(0, QCoreApplication.translate("StartIntelligentTestDialog", u"definitions", None))
        self.combx_quesion_mode.setItemText(1, QCoreApplication.translate("StartIntelligentTestDialog", u"phrases", None))

        self.btn_reset.setText(QCoreApplication.translate("StartIntelligentTestDialog", u"Reset", None))
        self.btn_start.setText(QCoreApplication.translate("StartIntelligentTestDialog", u"Start", None))
        pass
    # retranslateUi

