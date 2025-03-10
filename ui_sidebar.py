﻿# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(31, 149, 239);\n"
"}\n"
"QPushButton {\n"
"	color:white;\n"
"	height:30px;\n"
"	border:none;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.icon_only_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/profile_pic.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/images/dashboard_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/images/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.profile_1 = QPushButton(self.icon_only_widget)
        self.profile_1.setObjectName(u"profile_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/profile_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/images/profile.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.profile_1.setIcon(icon1)
        self.profile_1.setCheckable(True)
        self.profile_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.profile_1)

        self.messages_1 = QPushButton(self.icon_only_widget)
        self.messages_1.setObjectName(u"messages_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/messages_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/images/messages.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.messages_1.setIcon(icon2)
        self.messages_1.setCheckable(True)
        self.messages_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.messages_1)

        self.notifications_1 = QPushButton(self.icon_only_widget)
        self.notifications_1.setObjectName(u"notifications_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/notifications_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/images/notifications.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.notifications_1.setIcon(icon3)
        self.notifications_1.setCheckable(True)
        self.notifications_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.notifications_1)

        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        icon4 = QIcon()
        icon4.addFile(u"images/settings_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/images/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon4)
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.settings_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 205, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_6 = QPushButton(self.icon_only_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u":/images/log_out_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.dashboard_1.raise_()
        self.profile_1.raise_()
        self.messages_1.raise_()
        self.notifications_1.raise_()
        self.settings_1.raise_()
        self.pushButton_6.raise_()
        self.label.raise_()

        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(31, 149, 239);\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color:white;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.icon_name_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/images/profile_pic.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_name_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_name_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.profile_2 = QPushButton(self.icon_name_widget)
        self.profile_2.setObjectName(u"profile_2")
        self.profile_2.setIcon(icon1)
        self.profile_2.setCheckable(True)
        self.profile_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.profile_2)

        self.messages_2 = QPushButton(self.icon_name_widget)
        self.messages_2.setObjectName(u"messages_2")
        self.messages_2.setIcon(icon2)
        self.messages_2.setCheckable(True)
        self.messages_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.messages_2)

        self.notifications_2 = QPushButton(self.icon_name_widget)
        self.notifications_2.setObjectName(u"notifications_2")
        self.notifications_2.setIcon(icon3)
        self.notifications_2.setCheckable(True)
        self.notifications_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.notifications_2)

        self.settings_2 = QPushButton(self.icon_name_widget)
        self.settings_2.setObjectName(u"settings_2")
        icon6 = QIcon()
        icon6.addFile(u":/images/settings_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/images/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_2.setIcon(icon6)
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 205, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_10 = QPushButton(self.icon_name_widget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setCheckable(True)
        self.pushButton_10.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.pushButton_10)


        self.gridLayout.addWidget(self.icon_name_widget, 0, 1, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.verticalLayout_5 = QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header_widget = QWidget(self.main_menu)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menu = QPushButton(self.header_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/images/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu.setIcon(icon7)
        self.menu.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.menu)

        self.horizontalSpacer_2 = QSpacerItem(155, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_14 = QPushButton(self.header_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        icon8 = QIcon()
        icon8.addFile(u":/images/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon8)

        self.horizontalLayout.addWidget(self.pushButton_14)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(154, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_15 = QPushButton(self.header_widget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"border:none;")
        icon9 = QIcon()
        icon9.addFile(u":/images/image.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_15.setIcon(icon9)

        self.horizontalLayout_4.addWidget(self.pushButton_15)


        self.verticalLayout_5.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.label_4 = QLabel(self.dashboard_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 210, 241, 91))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_4.setFont(font1)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.label_5 = QLabel(self.profile_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 160, 241, 91))
        self.label_5.setFont(font1)
        self.stackedWidget.addWidget(self.profile_page)
        self.messages_page = QWidget()
        self.messages_page.setObjectName(u"messages_page")
        self.label_6 = QLabel(self.messages_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 160, 241, 91))
        self.label_6.setFont(font1)
        self.stackedWidget.addWidget(self.messages_page)
        self.notifications_page = QWidget()
        self.notifications_page.setObjectName(u"notifications_page")
        self.label_7 = QLabel(self.notifications_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 140, 261, 91))
        self.label_7.setFont(font1)
        self.stackedWidget.addWidget(self.notifications_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label_8 = QLabel(self.settings_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(240, 140, 241, 91))
        self.label_8.setFont(font1)
        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_only_widget.setHidden)
        self.menu.toggled.connect(self.icon_name_widget.setVisible)
        self.settings_1.toggled.connect(self.settings_2.setChecked)
        self.notifications_1.toggled.connect(self.notifications_2.setChecked)
        self.messages_1.toggled.connect(self.messages_2.setChecked)
        self.profile_1.toggled.connect(self.profile_2.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.profile_2.toggled.connect(self.profile_1.setChecked)
        self.messages_2.toggled.connect(self.messages_1.setChecked)
        self.notifications_2.toggled.connect(self.notifications_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.pushButton_6.toggled.connect(MainWindow.close)
        self.pushButton_10.toggled.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.dashboard_1.setText("")
        self.profile_1.setText("")
        self.messages_1.setText("")
        self.notifications_1.setText("")
        self.settings_1.setText("")
        self.pushButton_6.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SideBar", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.profile_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.messages_2.setText(QCoreApplication.translate("MainWindow", u"Messages", None))
        self.notifications_2.setText(QCoreApplication.translate("MainWindow", u"Notifications", None))
        self.settings_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.menu.setText("")
        self.pushButton_14.setText("")
        self.pushButton_15.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dashboard Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Profile Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Messages Page", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Notifications Page", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings Page", None))
    # retranslateUi

