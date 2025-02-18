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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QVBoxLayout,
    QWidget)

from lib.ui.widgets import NewFlashcardWidget
from lib.ui.widgets_basic import PushButton
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(850, 726)
        MainWindow.setMinimumSize(QSize(850, 600))
        font = QFont()
        font.setFamilies([u"Futura"])
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"* {\n"
"	font-family: Futura;\n"
"}\n"
"\n"
"QMainWindow{\n"
"	background-color: #e4e2eb;\n"
"}\n"
"\n"
"QWidget#statistics {\n"
"	border: 3px;\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: transparent;\n"
"	border-bottom: 3px;\n"
"	border-bottom-style: solid;\n"
"	border-bottom-color: #9e5db8;\n"
"}\n"
"\n"
"QLineEdit:read-only {\n"
"	border-bottom: 3px;\n"
"	border-bottom-style: solid;\n"
"	border-bottom-color: white;\n"
"}\n"
"\n"
"QLabel#lbl_greet{\n"
"	font-size: 25px;\n"
"}\n"
"\n"
"PushButton {\n"
"	font-size: 15px;\n"
"	background-color: transparent;\n"
"	border-width: 2px;\n"
"	border-style: solid;\n"
"	border-color: #ffffff;\n"
"}\n"
"\n"
"PushButton:hover {\n"
"	border-color: #9e5db8\n"
"}\n"
"\n"
"PushButton:checked {\n"
"	border-color: #9e5db8;\n"
"	background-color: white;\n"
"}\n"
"\n"
"PushButton#btn_flashcard{\n"
"	font-size: 20px;\n"
"	border-width: 5px;\n"
"}\n"
"\n"
"PushButton#btn_priority{\n"
"	border-width: 0px;\n"
"	background-color"
                        ": transparent;\n"
"}\n"
"\n"
"QListWidget {\n"
"	background-color: transparent;\n"
"	font-size: 20px;\n"
"}\n"
"QListWidget{\n"
"	border: 3px;\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"}\n"
"QListWidget#list_sets::item:hover{\n"
"	border-bottom: 3px;\n"
"	border-style: solid;\n"
"	border-color: #9e5db8;\n"
"	background-color:\n"
"}\n"
"QListWidget#list_sets::item:selected{\n"
"	border-bottom: 3px;\n"
"	border-style: solid;\n"
"	border-color: #9e5db8;\n"
"	background-color: #e7d6ed\n"
"}\n"
"\n"
"QWidget#list_flashcards_header{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QWidget#container_lbl_sets{\n"
"	background-color: white;\n"
"}\n"
"\n"
"QWidget#learning_widget{\n"
"	border: 3px;\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"}\n"
"\n"
"QWidget#widget_mode_intelligent_test {\n"
"	border: 3px;\n"
"	border-style: solid;\n"
"	border-color: white;\n"
"}\n"
"")
        self.actionImport_Flashcards_Set = QAction(MainWindow)
        self.actionImport_Flashcards_Set.setObjectName(u"actionImport_Flashcards_Set")
        self.actionImport_Flashcards_Set.setEnabled(False)
        icon = QIcon()
        icon.addFile(u"icons/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImport_Flashcards_Set.setIcon(icon)
        self.actionExport_Flashcards_Set = QAction(MainWindow)
        self.actionExport_Flashcards_Set.setObjectName(u"actionExport_Flashcards_Set")
        self.actionExport_Flashcards_Set.setEnabled(False)
        icon1 = QIcon()
        icon1.addFile(u"icons/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExport_Flashcards_Set.setIcon(icon1)
        self.actionFlashcards = QAction(MainWindow)
        self.actionFlashcards.setObjectName(u"actionFlashcards")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamilies([u"Futura"])
        font1.setPointSize(18)
        self.centralwidget.setFont(font1)
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.container_list_sets = QWidget(self.splitter)
        self.container_list_sets.setObjectName(u"container_list_sets")
        self.verticalLayout = QVBoxLayout(self.container_list_sets)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container_lbl_sets = QWidget(self.container_list_sets)
        self.container_lbl_sets.setObjectName(u"container_lbl_sets")
        self.gridLayout_3 = QGridLayout(self.container_lbl_sets)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(12, 0, 0, 0)
        self.lbl_sets = QLabel(self.container_lbl_sets)
        self.lbl_sets.setObjectName(u"lbl_sets")
        self.lbl_sets.setMinimumSize(QSize(0, 36))

        self.gridLayout_3.addWidget(self.lbl_sets, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.container_lbl_sets)

        self.list_sets = QListWidget(self.container_list_sets)
        self.list_sets.setObjectName(u"list_sets")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_sets.sizePolicy().hasHeightForWidth())
        self.list_sets.setSizePolicy(sizePolicy)
        self.list_sets.setMinimumSize(QSize(250, 0))
        font2 = QFont()
        font2.setFamilies([u"Futura"])
        font2.setKerning(True)
        self.list_sets.setFont(font2)
        self.list_sets.setFrameShape(QFrame.NoFrame)
        self.list_sets.setFrameShadow(QFrame.Plain)
        self.list_sets.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.list_sets)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.btn_new_set = PushButton(self.container_list_sets)
        self.btn_new_set.setObjectName(u"btn_new_set")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_new_set.sizePolicy().hasHeightForWidth())
        self.btn_new_set.setSizePolicy(sizePolicy1)
        self.btn_new_set.setMinimumSize(QSize(50, 36))
        font3 = QFont()
        font3.setFamilies([u"Futura"])
        self.btn_new_set.setFont(font3)

        self.horizontalLayout.addWidget(self.btn_new_set)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_import_set = PushButton(self.container_list_sets)
        self.btn_import_set.setObjectName(u"btn_import_set")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_import_set.sizePolicy().hasHeightForWidth())
        self.btn_import_set.setSizePolicy(sizePolicy2)
        self.btn_import_set.setMinimumSize(QSize(36, 36))
        self.btn_import_set.setFont(font3)
        icon2 = QIcon()
        icon2.addFile(u":/lib/ui/icons/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_import_set.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_import_set)

        self.btn_export_set = PushButton(self.container_list_sets)
        self.btn_export_set.setObjectName(u"btn_export_set")
        sizePolicy2.setHeightForWidth(self.btn_export_set.sizePolicy().hasHeightForWidth())
        self.btn_export_set.setSizePolicy(sizePolicy2)
        self.btn_export_set.setMinimumSize(QSize(36, 36))
        self.btn_export_set.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u":/lib/ui/icons/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_set.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btn_export_set)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter.addWidget(self.container_list_sets)
        self.stack_1 = QStackedWidget(self.splitter)
        self.stack_1.setObjectName(u"stack_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.stack_1.sizePolicy().hasHeightForWidth())
        self.stack_1.setSizePolicy(sizePolicy3)
        self.stack_1.setMinimumSize(QSize(400, 0))
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_4 = QVBoxLayout(self.home_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.lbl_greet = QLabel(self.home_page)
        self.lbl_greet.setObjectName(u"lbl_greet")
        self.lbl_greet.setFont(font3)

        self.verticalLayout_4.addWidget(self.lbl_greet)

        self.label = QLabel(self.home_page)
        self.label.setObjectName(u"label")
        self.label.setMargin(0)

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.statistics = QWidget(self.home_page)
        self.statistics.setObjectName(u"statistics")
        sizePolicy2.setHeightForWidth(self.statistics.sizePolicy().hasHeightForWidth())
        self.statistics.setSizePolicy(sizePolicy2)
        self.gridLayout_2 = QGridLayout(self.statistics)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_sets_count = QLabel(self.statistics)
        self.lbl_sets_count.setObjectName(u"lbl_sets_count")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lbl_sets_count.sizePolicy().hasHeightForWidth())
        self.lbl_sets_count.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.lbl_sets_count, 0, 0, 1, 1)

        self.fld_sets_count = QLineEdit(self.statistics)
        self.fld_sets_count.setObjectName(u"fld_sets_count")
        self.fld_sets_count.setFrame(False)
        self.fld_sets_count.setReadOnly(True)

        self.gridLayout_2.addWidget(self.fld_sets_count, 0, 1, 1, 1)

        self.lbl_flashcards_count = QLabel(self.statistics)
        self.lbl_flashcards_count.setObjectName(u"lbl_flashcards_count")
        sizePolicy4.setHeightForWidth(self.lbl_flashcards_count.sizePolicy().hasHeightForWidth())
        self.lbl_flashcards_count.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.lbl_flashcards_count, 1, 0, 1, 1)

        self.fld_flashcards_count = QLineEdit(self.statistics)
        self.fld_flashcards_count.setObjectName(u"fld_flashcards_count")
        self.fld_flashcards_count.setFrame(False)
        self.fld_flashcards_count.setReadOnly(True)

        self.gridLayout_2.addWidget(self.fld_flashcards_count, 1, 1, 1, 1)

        self.lbl_time = QLabel(self.statistics)
        self.lbl_time.setObjectName(u"lbl_time")
        sizePolicy4.setHeightForWidth(self.lbl_time.sizePolicy().hasHeightForWidth())
        self.lbl_time.setSizePolicy(sizePolicy4)

        self.gridLayout_2.addWidget(self.lbl_time, 2, 0, 1, 1)

        self.fld_time = QLineEdit(self.statistics)
        self.fld_time.setObjectName(u"fld_time")
        self.fld_time.setFrame(False)
        self.fld_time.setReadOnly(True)

        self.gridLayout_2.addWidget(self.fld_time, 2, 1, 1, 1)


        self.horizontalLayout_6.addWidget(self.statistics)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 424, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.stack_1.addWidget(self.home_page)
        self.flashcards_set_page = QWidget()
        self.flashcards_set_page.setObjectName(u"flashcards_set_page")
        self.flashcards_set_page.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.flashcards_set_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout_5.setSpacing(-1)
#endif
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_homepage = PushButton(self.flashcards_set_page)
        self.btn_homepage.setObjectName(u"btn_homepage")
        self.btn_homepage.setMinimumSize(QSize(100, 36))
        icon4 = QIcon()
        icon4.addFile(u":/lib/ui/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_homepage.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.btn_homepage)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.btn_reverse = PushButton(self.flashcards_set_page)
        self.btn_reverse.setObjectName(u"btn_reverse")
        self.btn_reverse.setMinimumSize(QSize(150, 36))
        icon5 = QIcon()
        icon5.addFile(u":/lib/ui/icons/reverse.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reverse.setIcon(icon5)
        self.btn_reverse.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.btn_reverse)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.splitter_2 = QSplitter(self.flashcards_set_page)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.slider_flashcards = QWidget(self.splitter_2)
        self.slider_flashcards.setObjectName(u"slider_flashcards")
        self.slider_flashcards.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.slider_flashcards.sizePolicy().hasHeightForWidth())
        self.slider_flashcards.setSizePolicy(sizePolicy5)
        self.verticalLayout_2 = QVBoxLayout(self.slider_flashcards)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_flashcard_count = QLabel(self.slider_flashcards)
        self.lbl_flashcard_count.setObjectName(u"lbl_flashcard_count")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lbl_flashcard_count.sizePolicy().hasHeightForWidth())
        self.lbl_flashcard_count.setSizePolicy(sizePolicy6)
        self.lbl_flashcard_count.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_flashcard_count)

        self.flashcard = QWidget(self.slider_flashcards)
        self.flashcard.setObjectName(u"flashcard")
        self.flashcard.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.flashcard.sizePolicy().hasHeightForWidth())
        self.flashcard.setSizePolicy(sizePolicy7)
        self.gridLayout = QGridLayout(self.flashcard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_flashcard = PushButton(self.flashcard)
        self.btn_flashcard.setObjectName(u"btn_flashcard")
        self.btn_flashcard.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btn_flashcard.sizePolicy().hasHeightForWidth())
        self.btn_flashcard.setSizePolicy(sizePolicy2)
        self.btn_flashcard.setMinimumSize(QSize(300, 200))
        self.btn_flashcard.setFont(font3)
        self.btn_flashcard.setCheckable(True)

        self.gridLayout.addWidget(self.btn_flashcard, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.flashcard)

        self.flashcard_options = QWidget(self.slider_flashcards)
        self.flashcard_options.setObjectName(u"flashcard_options")
        self.flashcard_options.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.flashcard_options.sizePolicy().hasHeightForWidth())
        self.flashcard_options.setSizePolicy(sizePolicy6)
        self.horizontalLayout_3 = QHBoxLayout(self.flashcard_options)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, 12, 5)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_previous_flashcard = PushButton(self.flashcard_options)
        self.btn_previous_flashcard.setObjectName(u"btn_previous_flashcard")
        self.btn_previous_flashcard.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btn_previous_flashcard.sizePolicy().hasHeightForWidth())
        self.btn_previous_flashcard.setSizePolicy(sizePolicy2)
        self.btn_previous_flashcard.setMinimumSize(QSize(36, 36))
        self.btn_previous_flashcard.setFont(font3)
        icon6 = QIcon()
        icon6.addFile(u":/lib/ui/icons/l_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_previous_flashcard.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.btn_previous_flashcard)

        self.btn_next_flashcard = PushButton(self.flashcard_options)
        self.btn_next_flashcard.setObjectName(u"btn_next_flashcard")
        self.btn_next_flashcard.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btn_next_flashcard.sizePolicy().hasHeightForWidth())
        self.btn_next_flashcard.setSizePolicy(sizePolicy2)
        self.btn_next_flashcard.setMinimumSize(QSize(36, 36))
        self.btn_next_flashcard.setFont(font3)
        icon7 = QIcon()
        icon7.addFile(u":/lib/ui/icons/r_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_next_flashcard.setIcon(icon7)

        self.horizontalLayout_3.addWidget(self.btn_next_flashcard)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.flashcard_options)

        self.splitter_2.addWidget(self.slider_flashcards)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.list_flashcards_options = QVBoxLayout(self.layoutWidget)
        self.list_flashcards_options.setSpacing(5)
        self.list_flashcards_options.setObjectName(u"list_flashcards_options")
        self.list_flashcards_options.setContentsMargins(0, 0, 0, 0)
        self.widget_new_flashcard = NewFlashcardWidget(self.layoutWidget)
        self.widget_new_flashcard.setObjectName(u"widget_new_flashcard")
        self.widget_new_flashcard.setEnabled(True)

        self.list_flashcards_options.addWidget(self.widget_new_flashcard)

        self.list_flashcards_header = QWidget(self.layoutWidget)
        self.list_flashcards_header.setObjectName(u"list_flashcards_header")
        self.horizontalLayout_7 = QHBoxLayout(self.list_flashcards_header)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(12, 5, 12, 4)
        self.lbl_phrase_header = QLabel(self.list_flashcards_header)
        self.lbl_phrase_header.setObjectName(u"lbl_phrase_header")
        sizePolicy4.setHeightForWidth(self.lbl_phrase_header.sizePolicy().hasHeightForWidth())
        self.lbl_phrase_header.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.lbl_phrase_header)

        self.lbl_definition_header = QLabel(self.list_flashcards_header)
        self.lbl_definition_header.setObjectName(u"lbl_definition_header")
        sizePolicy4.setHeightForWidth(self.lbl_definition_header.sizePolicy().hasHeightForWidth())
        self.lbl_definition_header.setSizePolicy(sizePolicy4)

        self.horizontalLayout_7.addWidget(self.lbl_definition_header)

        self.horizontalSpacer_5 = QSpacerItem(120, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.list_flashcards_options.addWidget(self.list_flashcards_header)

        self.list_flashcards = QListWidget(self.layoutWidget)
        self.list_flashcards.setObjectName(u"list_flashcards")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.list_flashcards.sizePolicy().hasHeightForWidth())
        self.list_flashcards.setSizePolicy(sizePolicy8)
        self.list_flashcards.setFrameShape(QFrame.NoFrame)
        self.list_flashcards.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_flashcards.setUniformItemSizes(True)

        self.list_flashcards_options.addWidget(self.list_flashcards)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_learn = PushButton(self.layoutWidget)
        self.btn_learn.setObjectName(u"btn_learn")
        self.btn_learn.setMinimumSize(QSize(150, 36))

        self.horizontalLayout_2.addWidget(self.btn_learn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.btn_generate_test = PushButton(self.layoutWidget)
        self.btn_generate_test.setObjectName(u"btn_generate_test")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.btn_generate_test.sizePolicy().hasHeightForWidth())
        self.btn_generate_test.setSizePolicy(sizePolicy9)
        self.btn_generate_test.setMinimumSize(QSize(120, 36))

        self.horizontalLayout_2.addWidget(self.btn_generate_test)


        self.list_flashcards_options.addLayout(self.horizontalLayout_2)

        self.splitter_2.addWidget(self.layoutWidget)

        self.verticalLayout_3.addWidget(self.splitter_2)

        self.stack_1.addWidget(self.flashcards_set_page)
        self.splitter.addWidget(self.stack_1)

        self.horizontalLayout_4.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 850, 37))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuStatistics = QMenu(self.menuBar)
        self.menuStatistics.setObjectName(u"menuStatistics")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuStatistics.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionImport_Flashcards_Set)
        self.menuFile.addAction(self.actionExport_Flashcards_Set)
        self.menuHelp.addAction(self.actionFlashcards)

        self.retranslateUi(MainWindow)

        self.stack_1.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Flashcards", None))
        self.actionImport_Flashcards_Set.setText(QCoreApplication.translate("MainWindow", u"Import Flashcards Set...", None))
        self.actionExport_Flashcards_Set.setText(QCoreApplication.translate("MainWindow", u"Export Flashcards Set...", None))
        self.actionFlashcards.setText(QCoreApplication.translate("MainWindow", u"Flashcards", None))
        self.lbl_sets.setText(QCoreApplication.translate("MainWindow", u"Sets:", None))
        self.btn_new_set.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_import_set.setText("")
        self.btn_export_set.setText("")
        self.lbl_greet.setText(QCoreApplication.translate("MainWindow", u"Greetings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Your Statistics:", None))
        self.lbl_sets_count.setText(QCoreApplication.translate("MainWindow", u"Number of sets:", None))
        self.lbl_flashcards_count.setText(QCoreApplication.translate("MainWindow", u"Number of flashcards:", None))
        self.lbl_time.setText(QCoreApplication.translate("MainWindow", u"Session time (hours:minutes):", None))
        self.btn_homepage.setText(QCoreApplication.translate("MainWindow", u" Home", None))
        self.btn_reverse.setText(QCoreApplication.translate("MainWindow", u" reversed mode", None))
        self.lbl_flashcard_count.setText(QCoreApplication.translate("MainWindow", u"0 / 0", None))
        self.btn_flashcard.setText("")
        self.btn_previous_flashcard.setText("")
        self.btn_next_flashcard.setText("")
        self.lbl_phrase_header.setText(QCoreApplication.translate("MainWindow", u"phrase", None))
        self.lbl_definition_header.setText(QCoreApplication.translate("MainWindow", u"definition", None))
        self.btn_learn.setText(QCoreApplication.translate("MainWindow", u"Intelligent Learning", None))
        self.btn_generate_test.setText(QCoreApplication.translate("MainWindow", u"Generate test", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuStatistics.setTitle(QCoreApplication.translate("MainWindow", u"Statistics", None))
    # retranslateUi

