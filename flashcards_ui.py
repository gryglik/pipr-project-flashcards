# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flashcards.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setMinimumSize(QSize(850, 600))
        font = QFont()
        font.setFamilies([u"Futura"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"* {\n"
"	font-family: Futura;\n"
"}\n"
"\n"
"QPushButton {\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QListWidget {\n"
"	background-color: white;\n"
"	font-size: 20px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamilies([u"Futura"])
        font1.setPointSize(18)
        self.centralwidget.setFont(font1)
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.mainstack = QStackedWidget(self.centralwidget)
        self.mainstack.setObjectName(u"mainstack")
        self.welcome_page = QWidget()
        self.welcome_page.setObjectName(u"welcome_page")
        self.verticalLayout_2 = QVBoxLayout(self.welcome_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_1)

        self.container_welcome = QWidget(self.welcome_page)
        self.container_welcome.setObjectName(u"container_welcome")
        self.verticalLayout_4 = QVBoxLayout(self.container_welcome)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_name = QLabel(self.container_welcome)
        self.lbl_name.setObjectName(u"lbl_name")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_name.sizePolicy().hasHeightForWidth())
        self.lbl_name.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Futura"])
        font2.setPointSize(40)
        font2.setBold(False)
        self.lbl_name.setFont(font2)
        self.lbl_name.setStyleSheet(u"")
        self.lbl_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_name, 0, Qt.AlignHCenter)

        self.fld_name = QLineEdit(self.container_welcome)
        self.fld_name.setObjectName(u"fld_name")
        self.fld_name.setEnabled(True)
        sizePolicy.setHeightForWidth(self.fld_name.sizePolicy().hasHeightForWidth())
        self.fld_name.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Futura"])
        font3.setPointSize(20)
        self.fld_name.setFont(font3)
        self.fld_name.setFocusPolicy(Qt.ClickFocus)
        self.fld_name.setMaxLength(25)
        self.fld_name.setFrame(False)
        self.fld_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.fld_name, 0, Qt.AlignHCenter)

        self.btn_name = QPushButton(self.container_welcome)
        self.btn_name.setObjectName(u"btn_name")
        sizePolicy.setHeightForWidth(self.btn_name.sizePolicy().hasHeightForWidth())
        self.btn_name.setSizePolicy(sizePolicy)
        self.btn_name.setMinimumSize(QSize(80, 0))
        self.btn_name.setSizeIncrement(QSize(0, 0))
        self.btn_name.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamilies([u"Futura"])
        self.btn_name.setFont(font4)
        self.btn_name.setFocusPolicy(Qt.NoFocus)

        self.verticalLayout_4.addWidget(self.btn_name, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.container_welcome)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.mainstack.addWidget(self.welcome_page)
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.verticalLayout_6 = QVBoxLayout(self.main_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_greet = QLabel(self.main_page)
        self.lbl_greet.setObjectName(u"lbl_greet")
        self.lbl_greet.setFont(font3)

        self.verticalLayout_6.addWidget(self.lbl_greet)

        self.splitter = QSplitter(self.main_page)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.list_sets = QListWidget(self.widget)
        self.list_sets.setObjectName(u"list_sets")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.list_sets.sizePolicy().hasHeightForWidth())
        self.list_sets.setSizePolicy(sizePolicy2)
        self.list_sets.setMinimumSize(QSize(150, 0))
        font5 = QFont()
        font5.setFamilies([u"Futura"])
        font5.setKerning(True)
        self.list_sets.setFont(font5)
        self.list_sets.setFrameShape(QFrame.NoFrame)
        self.list_sets.setFrameShadow(QFrame.Plain)
        self.list_sets.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.list_sets)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_new_set = QPushButton(self.widget)
        self.btn_new_set.setObjectName(u"btn_new_set")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_new_set.sizePolicy().hasHeightForWidth())
        self.btn_new_set.setSizePolicy(sizePolicy3)
        self.btn_new_set.setMinimumSize(QSize(50, 36))
        self.btn_new_set.setFont(font4)

        self.horizontalLayout.addWidget(self.btn_new_set)

        self.btn_set_delete = QPushButton(self.widget)
        self.btn_set_delete.setObjectName(u"btn_set_delete")
        sizePolicy.setHeightForWidth(self.btn_set_delete.sizePolicy().hasHeightForWidth())
        self.btn_set_delete.setSizePolicy(sizePolicy)
        self.btn_set_delete.setMinimumSize(QSize(36, 36))
        self.btn_set_delete.setFont(font4)
        icon = QIcon()
        icon.addFile(u"icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_set_delete.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_set_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_import_set = QPushButton(self.widget)
        self.btn_import_set.setObjectName(u"btn_import_set")
        sizePolicy.setHeightForWidth(self.btn_import_set.sizePolicy().hasHeightForWidth())
        self.btn_import_set.setSizePolicy(sizePolicy)
        self.btn_import_set.setMinimumSize(QSize(36, 36))
        self.btn_import_set.setFont(font4)
        icon1 = QIcon()
        icon1.addFile(u"icons/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_import_set.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btn_import_set)

        self.btn_export_set = QPushButton(self.widget)
        self.btn_export_set.setObjectName(u"btn_export_set")
        sizePolicy.setHeightForWidth(self.btn_export_set.sizePolicy().hasHeightForWidth())
        self.btn_export_set.setSizePolicy(sizePolicy)
        self.btn_export_set.setMinimumSize(QSize(36, 36))
        self.btn_export_set.setFont(font4)
        icon2 = QIcon()
        icon2.addFile(u"icons/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_set.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btn_export_set)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.widget)
        self.stackedWidget = QStackedWidget(self.splitter)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
        self.stackedWidget.setMinimumSize(QSize(400, 0))
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.set_page = QWidget()
        self.set_page.setObjectName(u"set_page")
        self.verticalLayout_3 = QVBoxLayout(self.set_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.set_page)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.widget1 = QWidget(self.splitter_2)
        self.widget1.setObjectName(u"widget1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget1.sizePolicy().hasHeightForWidth())
        self.widget1.setSizePolicy(sizePolicy5)
        self.verticalLayout_7 = QVBoxLayout(self.widget1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(12, -1, -1, -1)
        self.widget_2 = QWidget(self.widget1)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy6)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.flashcard = QLabel(self.widget_2)
        self.flashcard.setObjectName(u"flashcard")
        sizePolicy.setHeightForWidth(self.flashcard.sizePolicy().hasHeightForWidth())
        self.flashcard.setSizePolicy(sizePolicy)
        self.flashcard.setMinimumSize(QSize(300, 200))
        self.flashcard.setSizeIncrement(QSize(30, 20))
        self.flashcard.setFrameShape(QFrame.Box)
        self.flashcard.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.flashcard, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.widget_2)

        self.flashcard_options = QWidget(self.widget1)
        self.flashcard_options.setObjectName(u"flashcard_options")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.flashcard_options.sizePolicy().hasHeightForWidth())
        self.flashcard_options.setSizePolicy(sizePolicy7)
        self.horizontalLayout_3 = QHBoxLayout(self.flashcard_options)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_previous_flashcard = QPushButton(self.flashcard_options)
        self.btn_previous_flashcard.setObjectName(u"btn_previous_flashcard")
        sizePolicy.setHeightForWidth(self.btn_previous_flashcard.sizePolicy().hasHeightForWidth())
        self.btn_previous_flashcard.setSizePolicy(sizePolicy)
        self.btn_previous_flashcard.setMinimumSize(QSize(36, 36))
        self.btn_previous_flashcard.setFont(font4)
        icon3 = QIcon()
        icon3.addFile(u"icons/l_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_previous_flashcard.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.btn_previous_flashcard)

        self.btn_next_flashcard = QPushButton(self.flashcard_options)
        self.btn_next_flashcard.setObjectName(u"btn_next_flashcard")
        sizePolicy.setHeightForWidth(self.btn_next_flashcard.sizePolicy().hasHeightForWidth())
        self.btn_next_flashcard.setSizePolicy(sizePolicy)
        self.btn_next_flashcard.setMinimumSize(QSize(36, 36))
        self.btn_next_flashcard.setFont(font4)
        icon4 = QIcon()
        icon4.addFile(u"icons/r_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next_flashcard.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.btn_next_flashcard)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addWidget(self.flashcard_options)

        self.splitter_2.addWidget(self.widget1)
        self.listFlashcards = QListWidget(self.splitter_2)
        self.listFlashcards.setObjectName(u"listFlashcards")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.listFlashcards.sizePolicy().hasHeightForWidth())
        self.listFlashcards.setSizePolicy(sizePolicy8)
        self.listFlashcards.setFrameShape(QFrame.NoFrame)
        self.listFlashcards.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listFlashcards.setUniformItemSizes(True)
        self.splitter_2.addWidget(self.listFlashcards)

        self.verticalLayout_3.addWidget(self.splitter_2)

        self.stackedWidget.addWidget(self.set_page)
        self.splitter.addWidget(self.stackedWidget)

        self.verticalLayout_6.addWidget(self.splitter)

        self.mainstack.addWidget(self.main_page)

        self.verticalLayout_5.addWidget(self.mainstack)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainstack.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Flashcards", None))
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"Hi,", None))
        self.fld_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your name...", None))
        self.btn_name.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.lbl_greet.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sets:", None))
        self.btn_new_set.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_set_delete.setText("")
        self.btn_import_set.setText("")
        self.btn_export_set.setText("")
        self.flashcard.setText("")
        self.btn_previous_flashcard.setText("")
        self.btn_next_flashcard.setText("")
    # retranslateUi

