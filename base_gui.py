# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base_guiKVwNOH.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(100, 100, 100);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 60))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 30))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(33, 37, 43, 150);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(8, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"margin-left: 5px;")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy1.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy1)
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(44, 49, 60)\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 16777215))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy2)
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)
        self.btn_Home = QPushButton(self.frame_menus)
        self.btn_Home.setObjectName(u"btn_Home")
        self.btn_Home.setMinimumSize(QSize(0, 60))
        self.btn_Home.setStyleSheet(u"QPushButton {	\n"
"	\n"
"	\n"
"	\n"
"	background-image: url(:/16x16/icons/16x16/cil-home.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_Home)

        self.btn_Compression = QPushButton(self.frame_menus)
        self.btn_Compression.setObjectName(u"btn_Compression")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_Compression.sizePolicy().hasHeightForWidth())
        self.btn_Compression.setSizePolicy(sizePolicy3)
        self.btn_Compression.setMinimumSize(QSize(0, 60))
        self.btn_Compression.setFont(font2)
        self.btn_Compression.setLayoutDirection(Qt.LeftToRight)
        self.btn_Compression.setStyleSheet(u"QPushButton {	\n"
"	\n"
"	\n"
"	\n"
"	background-image: url(:/edits/Editingscreen images/003-compression.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_Compression)

        self.btn_Face_recognition = QPushButton(self.frame_menus)
        self.btn_Face_recognition.setObjectName(u"btn_Face_recognition")
        sizePolicy3.setHeightForWidth(self.btn_Face_recognition.sizePolicy().hasHeightForWidth())
        self.btn_Face_recognition.setSizePolicy(sizePolicy3)
        self.btn_Face_recognition.setMinimumSize(QSize(0, 60))
        self.btn_Face_recognition.setFont(font2)
        self.btn_Face_recognition.setLayoutDirection(Qt.LeftToRight)
        self.btn_Face_recognition.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/edits/Editingscreen images/001-face-detection.png);\n"
"\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_Face_recognition)

        self.btn_Speech_removal = QPushButton(self.frame_menus)
        self.btn_Speech_removal.setObjectName(u"btn_Speech_removal")
        sizePolicy3.setHeightForWidth(self.btn_Speech_removal.sizePolicy().hasHeightForWidth())
        self.btn_Speech_removal.setSizePolicy(sizePolicy3)
        self.btn_Speech_removal.setMinimumSize(QSize(0, 60))
        self.btn_Speech_removal.setFont(font2)
        self.btn_Speech_removal.setLayoutDirection(Qt.LeftToRight)
        self.btn_Speech_removal.setStyleSheet(u"QPushButton {	\n"
"	\n"
"	\n"
"	background-image: url(:/edits/Editingscreen images/005-remove.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	border-right: 5px solid rgb(44, 49, 60);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_Speech_removal)

        self.btn_Editing = QPushButton(self.frame_menus)
        self.btn_Editing.setObjectName(u"btn_Editing")
        sizePolicy3.setHeightForWidth(self.btn_Editing.sizePolicy().hasHeightForWidth())
        self.btn_Editing.setSizePolicy(sizePolicy3)
        self.btn_Editing.setMinimumSize(QSize(0, 60))
        self.btn_Editing.setFont(font2)
        self.btn_Editing.setLayoutDirection(Qt.LeftToRight)
        self.btn_Editing.setStyleSheet(u"QPushButton {	\n"
"	\n"
"	background-image: url(:/edits/Editingscreen images/002-multimedia.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_Editing)

        self.btn_YouTube_upload = QPushButton(self.frame_menus)
        self.btn_YouTube_upload.setObjectName(u"btn_YouTube_upload")
        self.btn_YouTube_upload.setMinimumSize(QSize(0, 60))
        self.btn_YouTube_upload.setStyleSheet(u"QPushButton {	\n"
"	\n"
"	\n"
"	background-image: url(:/edits/Editingscreen images/test-youtube.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 28px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menus.addWidget(self.btn_YouTube_upload)


        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy2.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy2)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.btn_settings = QPushButton(self.frame_extra_menus)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy3.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy3)
        self.btn_settings.setMinimumSize(QSize(0, 60))
        self.btn_settings.setFont(font2)
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/20x20/icons/20x20/cil-settings.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 26px solid rgb(27, 29, 35);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 26px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 26px solid rgb(85, 170, 255);\n"
"}")

        self.layout_menu_bottom.addWidget(self.btn_settings)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.Home_page = QWidget()
        self.Home_page.setObjectName(u"Home_page")
        self.verticalLayout_6 = QVBoxLayout(self.Home_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.Home_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 90))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Black")
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_5.setFont(font4)

        self.verticalLayout_6.addWidget(self.label_5)

        self.video = QWidget(self.Home_page)
        self.video.setObjectName(u"video")
        self.video.setStyleSheet(u"border:1px solid white\n"
"")

        self.verticalLayout_6.addWidget(self.video)

        self.frame_2 = QFrame(self.Home_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 120))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_uploadvideo = QPushButton(self.frame_2)
        self.btn_uploadvideo.setObjectName(u"btn_uploadvideo")
        font5 = QFont()
        font5.setFamily(u"Segoe UI Black")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.btn_uploadvideo.setFont(font5)
        self.btn_uploadvideo.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_uploadvideo)

        self.btn_startediting = QPushButton(self.frame_2)
        self.btn_startediting.setObjectName(u"btn_startediting")
        self.btn_startediting.setFont(font5)
        self.btn_startediting.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_startediting)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.Home_page)
        self.Compression_page = QWidget()
        self.Compression_page.setObjectName(u"Compression_page")
        self.verticalLayout_7 = QVBoxLayout(self.Compression_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.Compression_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 90))
        self.label_3.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_3)

        self.frame_3 = QFrame(self.Compression_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border:2px solid white;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.Compression_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 110))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_compressvideo = QPushButton(self.frame_4)
        self.btn_compressvideo.setObjectName(u"btn_compressvideo")
        self.btn_compressvideo.setMinimumSize(QSize(0, 0))
        self.btn_compressvideo.setFont(font5)
        self.btn_compressvideo.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_compressvideo)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.Compression_page)
        self.compression_page2 = QWidget()
        self.compression_page2.setObjectName(u"compression_page2")
        self.verticalLayout_23 = QVBoxLayout(self.compression_page2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_16 = QLabel(self.compression_page2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(16777215, 90))
        self.label_16.setFont(font4)

        self.verticalLayout_23.addWidget(self.label_16)

        self.frame_39 = QFrame(self.compression_page2)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.frame_39)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(280, 16777215))
        self.label_15.setFont(font5)

        self.horizontalLayout_20.addWidget(self.label_15)

        self.comp_rate = QComboBox(self.frame_39)
        self.comp_rate.addItem("")
        self.comp_rate.addItem("")
        self.comp_rate.addItem("")
        self.comp_rate.addItem("")
        self.comp_rate.addItem("")
        self.comp_rate.addItem("")
        self.comp_rate.addItem("")
        self.comp_rate.addItem("")
        self.comp_rate.addItem("")
        self.comp_rate.setObjectName(u"comp_rate")
        self.comp_rate.setMinimumSize(QSize(350, 0))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Black")
        font6.setPointSize(16)
        font6.setBold(True)
        font6.setWeight(75)
        self.comp_rate.setFont(font6)
        self.comp_rate.setStyleSheet(u"border:1px solid white;\n"
"")

        self.horizontalLayout_20.addWidget(self.comp_rate)


        self.verticalLayout_23.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.compression_page2)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_applycompression = QPushButton(self.frame_40)
        self.btn_applycompression.setObjectName(u"btn_applycompression")
        self.btn_applycompression.setFont(font5)
        self.btn_applycompression.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_22.addWidget(self.btn_applycompression)

        self.btn_previewcompression = QPushButton(self.frame_40)
        self.btn_previewcompression.setObjectName(u"btn_previewcompression")
        self.btn_previewcompression.setFont(font5)
        self.btn_previewcompression.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_22.addWidget(self.btn_previewcompression)


        self.verticalLayout_23.addWidget(self.frame_40)

        self.stackedWidget.addWidget(self.compression_page2)
        self.facialrecognition_page_1 = QWidget()
        self.facialrecognition_page_1.setObjectName(u"facialrecognition_page_1")
        self.verticalLayout_8 = QVBoxLayout(self.facialrecognition_page_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.facialrecognition_page_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 90))
        self.label_4.setFont(font4)

        self.verticalLayout_8.addWidget(self.label_4)

        self.frame_5 = QFrame(self.facialrecognition_page_1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.facialrecognition_page_1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 120))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_performrecognition = QPushButton(self.frame_6)
        self.btn_performrecognition.setObjectName(u"btn_performrecognition")
        self.btn_performrecognition.setFont(font5)
        self.btn_performrecognition.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_performrecognition)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.facialrecognition_page_1)
        self.facialrecognition_page2 = QWidget()
        self.facialrecognition_page2.setObjectName(u"facialrecognition_page2")
        self.verticalLayout_11 = QVBoxLayout(self.facialrecognition_page2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_7 = QFrame(self.facialrecognition_page2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 90))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setFont(font6)

        self.verticalLayout_12.addWidget(self.label)

        self.textEdit = QTextEdit(self.frame_7)
        self.textEdit.setObjectName(u"textEdit")
        font7 = QFont()
        font7.setFamily(u"Segoe UI Black")
        font7.setBold(True)
        font7.setWeight(75)
        self.textEdit.setFont(font7)
        self.textEdit.setStyleSheet(u"border:none;")

        self.verticalLayout_12.addWidget(self.textEdit)


        self.verticalLayout_11.addWidget(self.frame_7)

        self.Faces = QFrame(self.facialrecognition_page2)
        self.Faces.setObjectName(u"Faces")
        self.Faces.setFrameShape(QFrame.StyledPanel)
        self.Faces.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.Faces)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_10 = QFrame(self.Faces)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_10, 0, 0, 1, 1)

        self.frame_12 = QFrame(self.Faces)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border:2px solid white;\n"
"border-radius: 10px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_12, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.Faces)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_11, 0, 2, 1, 1)

        self.frame_14 = QFrame(self.Faces)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"border:2px solid white;\n"
"border-radius: 10px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_14, 1, 2, 1, 1)

        self.frame_17 = QFrame(self.Faces)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"border:2px solid white;\n"
"border-radius: 10px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_17, 2, 2, 1, 1)

        self.frame_18 = QFrame(self.Faces)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"border:2px solid white;\n"
"border-radius: 10px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_18, 2, 4, 1, 1)

        self.frame_13 = QFrame(self.Faces)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_13, 0, 4, 1, 1)

        self.frame_20 = QFrame(self.Faces)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_20, 2, 1, 1, 1)

        self.frame_19 = QFrame(self.Faces)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_19, 1, 1, 1, 1)

        self.frame_15 = QFrame(self.Faces)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border:2px solid white;\n"
"border-radius: 10px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_15, 1, 4, 1, 1)

        self.frame_8 = QFrame(self.Faces)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_8, 0, 1, 1, 1)

        self.frame_16 = QFrame(self.Faces)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"border:2px solid white;\n"
"border-radius: 10px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_16, 2, 0, 1, 1)

        self.frame_21 = QFrame(self.Faces)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_21, 0, 3, 1, 1)

        self.frame_22 = QFrame(self.Faces)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_22, 1, 3, 1, 1)

        self.frame_23 = QFrame(self.Faces)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_23, 2, 3, 1, 1)


        self.verticalLayout_11.addWidget(self.Faces)

        self.frame_9 = QFrame(self.facialrecognition_page2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 120))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btn_performblur = QPushButton(self.frame_9)
        self.btn_performblur.setObjectName(u"btn_performblur")
        self.btn_performblur.setFont(font5)
        self.btn_performblur.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_13.addWidget(self.btn_performblur)


        self.verticalLayout_11.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.facialrecognition_page2)
        self.speechremoval_page = QWidget()
        self.speechremoval_page.setObjectName(u"speechremoval_page")
        self.verticalLayout_15 = QVBoxLayout(self.speechremoval_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_24 = QFrame(self.speechremoval_page)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 90))
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_24)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_2 = QLabel(self.frame_24)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.verticalLayout_14.addWidget(self.label_2)


        self.verticalLayout_15.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.speechremoval_page)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_15.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.speechremoval_page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 110))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_removethroughout = QPushButton(self.frame_26)
        self.btn_removethroughout.setObjectName(u"btn_removethroughout")
        self.btn_removethroughout.setFont(font5)
        self.btn_removethroughout.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_removethroughout)

        self.btn_removefromspecificportion = QPushButton(self.frame_26)
        self.btn_removefromspecificportion.setObjectName(u"btn_removefromspecificportion")
        self.btn_removefromspecificportion.setFont(font5)
        self.btn_removefromspecificportion.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_removefromspecificportion)


        self.verticalLayout_15.addWidget(self.frame_26)

        self.stackedWidget.addWidget(self.speechremoval_page)
        self.editing_page = QWidget()
        self.editing_page.setObjectName(u"editing_page")
        self.verticalLayout_16 = QVBoxLayout(self.editing_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_6 = QLabel(self.editing_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 90))
        self.label_6.setFont(font4)

        self.verticalLayout_16.addWidget(self.label_6)

        self.frame_29 = QFrame(self.editing_page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"border:2px solid white;\n"
"border-radius:10px;")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_29)

        self.frame_28 = QFrame(self.editing_page)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 160))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_mirror = QPushButton(self.frame_28)
        self.btn_mirror.setObjectName(u"btn_mirror")
        self.btn_mirror.setFont(font5)
        self.btn_mirror.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_mirror)

        self.btn_speed = QPushButton(self.frame_28)
        self.btn_speed.setObjectName(u"btn_speed")
        self.btn_speed.setFont(font5)
        self.btn_speed.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_speed)

        self.btn_merge = QPushButton(self.frame_28)
        self.btn_merge.setObjectName(u"btn_merge")
        self.btn_merge.setFont(font5)
        self.btn_merge.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_merge)

        self.btn_trim = QPushButton(self.frame_28)
        self.btn_trim.setObjectName(u"btn_trim")
        self.btn_trim.setFont(font5)
        self.btn_trim.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_trim)

        self.btn_color = QPushButton(self.frame_28)
        self.btn_color.setObjectName(u"btn_color")
        self.btn_color.setFont(font5)
        self.btn_color.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_color)


        self.verticalLayout_16.addWidget(self.frame_28)

        self.stackedWidget.addWidget(self.editing_page)
        self.speed_page = QWidget()
        self.speed_page.setObjectName(u"speed_page")
        self.verticalLayout_17 = QVBoxLayout(self.speed_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_7 = QLabel(self.speed_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 90))
        self.label_7.setFont(font4)

        self.verticalLayout_17.addWidget(self.label_7)

        self.frame_27 = QFrame(self.speed_page)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_8 = QLabel(self.frame_27)
        self.label_8.setObjectName(u"label_8")
        font8 = QFont()
        font8.setFamily(u"Segoe UI Black")
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_8.setFont(font8)

        self.horizontalLayout_14.addWidget(self.label_8)

        self.speed_value = QLineEdit(self.frame_27)
        self.speed_value.setObjectName(u"speed_value")

        self.horizontalLayout_14.addWidget(self.speed_value)


        self.verticalLayout_17.addWidget(self.frame_27)

        self.frame_30 = QFrame(self.speed_page)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_applyspeedeffect = QPushButton(self.frame_30)
        self.btn_applyspeedeffect.setObjectName(u"btn_applyspeedeffect")
        self.btn_applyspeedeffect.setFont(font5)
        self.btn_applyspeedeffect.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.btn_applyspeedeffect)

        self.btn_previewspeedeffect = QPushButton(self.frame_30)
        self.btn_previewspeedeffect.setObjectName(u"btn_previewspeedeffect")
        self.btn_previewspeedeffect.setFont(font5)
        self.btn_previewspeedeffect.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_15.addWidget(self.btn_previewspeedeffect)


        self.verticalLayout_17.addWidget(self.frame_30)

        self.stackedWidget.addWidget(self.speed_page)
        self.color_page = QWidget()
        self.color_page.setObjectName(u"color_page")
        self.verticalLayout_18 = QVBoxLayout(self.color_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_10 = QLabel(self.color_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 90))
        self.label_10.setFont(font4)

        self.verticalLayout_18.addWidget(self.label_10)

        self.frame_31 = QFrame(self.color_page)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_9 = QLabel(self.frame_31)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font8)

        self.horizontalLayout_16.addWidget(self.label_9)

        self.darkness_value = QLineEdit(self.frame_31)
        self.darkness_value.setObjectName(u"darkness_value")

        self.horizontalLayout_16.addWidget(self.darkness_value)


        self.verticalLayout_18.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.color_page)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.btn_applycoloreffect = QPushButton(self.frame_32)
        self.btn_applycoloreffect.setObjectName(u"btn_applycoloreffect")
        self.btn_applycoloreffect.setFont(font5)
        self.btn_applycoloreffect.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_17.addWidget(self.btn_applycoloreffect)

        self.btn_previewcoloreffect = QPushButton(self.frame_32)
        self.btn_previewcoloreffect.setObjectName(u"btn_previewcoloreffect")
        self.btn_previewcoloreffect.setFont(font5)
        self.btn_previewcoloreffect.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_17.addWidget(self.btn_previewcoloreffect)


        self.verticalLayout_18.addWidget(self.frame_32)

        self.stackedWidget.addWidget(self.color_page)
        self.merge_page = QWidget()
        self.merge_page.setObjectName(u"merge_page")
        self.verticalLayout_19 = QVBoxLayout(self.merge_page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_11 = QLabel(self.merge_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 90))
        self.label_11.setFont(font4)

        self.verticalLayout_19.addWidget(self.label_11)

        self.frame_34 = QFrame(self.merge_page)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_35 = QFrame(self.frame_34)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_35)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.btn_choosesecondclip = QPushButton(self.frame_35)
        self.btn_choosesecondclip.setObjectName(u"btn_choosesecondclip")
        self.btn_choosesecondclip.setMaximumSize(QSize(240, 16777215))
        self.btn_choosesecondclip.setFont(font5)
        self.btn_choosesecondclip.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_20.addWidget(self.btn_choosesecondclip)

        self.btn_choosethirdclip = QPushButton(self.frame_35)
        self.btn_choosethirdclip.setObjectName(u"btn_choosethirdclip")
        self.btn_choosethirdclip.setMaximumSize(QSize(240, 16777215))
        self.btn_choosethirdclip.setFont(font5)
        self.btn_choosethirdclip.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_20.addWidget(self.btn_choosethirdclip)


        self.horizontalLayout_19.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_36)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_secondclip = QLabel(self.frame_36)
        self.label_secondclip.setObjectName(u"label_secondclip")
        self.label_secondclip.setFont(font5)

        self.verticalLayout_21.addWidget(self.label_secondclip)

        self.label_thirdclip = QLabel(self.frame_36)
        self.label_thirdclip.setObjectName(u"label_thirdclip")
        self.label_thirdclip.setFont(font5)

        self.verticalLayout_21.addWidget(self.label_thirdclip)


        self.horizontalLayout_19.addWidget(self.frame_36)


        self.verticalLayout_19.addWidget(self.frame_34)

        self.frame_33 = QFrame(self.merge_page)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.btn_applymerge = QPushButton(self.frame_33)
        self.btn_applymerge.setObjectName(u"btn_applymerge")
        self.btn_applymerge.setFont(font5)
        self.btn_applymerge.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_applymerge)

        self.btn_previewmerge = QPushButton(self.frame_33)
        self.btn_previewmerge.setObjectName(u"btn_previewmerge")
        self.btn_previewmerge.setFont(font5)
        self.btn_previewmerge.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_18.addWidget(self.btn_previewmerge)


        self.verticalLayout_19.addWidget(self.frame_33)

        self.stackedWidget.addWidget(self.merge_page)
        self.trim_page = QWidget()
        self.trim_page.setObjectName(u"trim_page")
        self.verticalLayout_22 = QVBoxLayout(self.trim_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_12 = QLabel(self.trim_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 90))
        self.label_12.setFont(font4)

        self.verticalLayout_22.addWidget(self.label_12)

        self.frame_37 = QFrame(self.trim_page)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_37)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_13 = QLabel(self.frame_37)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font8)

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.starting_point = QLineEdit(self.frame_37)
        self.starting_point.setObjectName(u"starting_point")

        self.gridLayout_2.addWidget(self.starting_point, 0, 1, 1, 1)

        self.label_14 = QLabel(self.frame_37)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font8)

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)

        self.ending_point = QLineEdit(self.frame_37)
        self.ending_point.setObjectName(u"ending_point")

        self.gridLayout_2.addWidget(self.ending_point, 1, 1, 1, 1)


        self.verticalLayout_22.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.trim_page)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btn_applytrim = QPushButton(self.frame_38)
        self.btn_applytrim.setObjectName(u"btn_applytrim")
        self.btn_applytrim.setFont(font5)
        self.btn_applytrim.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_21.addWidget(self.btn_applytrim)

        self.btn_previewtrim = QPushButton(self.frame_38)
        self.btn_previewtrim.setObjectName(u"btn_previewtrim")
        self.btn_previewtrim.setFont(font5)
        self.btn_previewtrim.setStyleSheet(u"QPushButton {	\n"
"	\n"
"    background-repeat: no-repeat;\n"
"	border:1px solid white;\n"
"	border-radius:10px;\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: center;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 28px solid rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 28px solid rgb(85, 170, 255);\n"
"}")

        self.horizontalLayout_21.addWidget(self.btn_previewtrim)


        self.verticalLayout_22.addWidget(self.frame_38)

        self.stackedWidget.addWidget(self.trim_page)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(10)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"YouTube Monetization Assitant", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.btn_Home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_Compression.setText(QCoreApplication.translate("MainWindow", u"Compress", None))
        self.btn_Face_recognition.setText(QCoreApplication.translate("MainWindow", u"Facial Recognition", None))
        self.btn_Speech_removal.setText(QCoreApplication.translate("MainWindow", u"Abusive Speech Removal", None))
        self.btn_Editing.setText(QCoreApplication.translate("MainWindow", u"Editing", None))
        self.btn_YouTube_upload.setText(QCoreApplication.translate("MainWindow", u"Upload to YouTube", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Welcome! Upload your video.", None))
        self.btn_uploadvideo.setText(QCoreApplication.translate("MainWindow", u"Upload Video", None))
        self.btn_startediting.setText(QCoreApplication.translate("MainWindow", u"Start Editing", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Video Compression", None))
        self.btn_compressvideo.setText(QCoreApplication.translate("MainWindow", u"Compress Video", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Video Compression", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Select the compression percentage", None))
        self.comp_rate.setItemText(0, QCoreApplication.translate("MainWindow", u"10", None))
        self.comp_rate.setItemText(1, QCoreApplication.translate("MainWindow", u"20", None))
        self.comp_rate.setItemText(2, QCoreApplication.translate("MainWindow", u"30", None))
        self.comp_rate.setItemText(3, QCoreApplication.translate("MainWindow", u"40", None))
        self.comp_rate.setItemText(4, QCoreApplication.translate("MainWindow", u"50", None))
        self.comp_rate.setItemText(5, QCoreApplication.translate("MainWindow", u"60", None))
        self.comp_rate.setItemText(6, QCoreApplication.translate("MainWindow", u"70", None))
        self.comp_rate.setItemText(7, QCoreApplication.translate("MainWindow", u"80", None))
        self.comp_rate.setItemText(8, QCoreApplication.translate("MainWindow", u"90", None))

        self.btn_applycompression.setText(QCoreApplication.translate("MainWindow", u"Apply compression", None))
        self.btn_previewcompression.setText(QCoreApplication.translate("MainWindow", u"Preview Compressed Video", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Facial Recoginition", None))
        self.btn_performrecognition.setText(QCoreApplication.translate("MainWindow", u"Perform Facial Recognition", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Choose a face", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Black'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2';\">Please choose a face you want to blur throughout the video</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:9pt;\">.</span></p></body></html>", None))
        self.btn_performblur.setText(QCoreApplication.translate("MainWindow", u"Perform Blur", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Abusive Speech Removal", None))
        self.btn_removethroughout.setText(QCoreApplication.translate("MainWindow", u"Remove Throughout", None))
        self.btn_removefromspecificportion.setText(QCoreApplication.translate("MainWindow", u"Remove From Specific Portion", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Basic Edits", None))
        self.btn_mirror.setText(QCoreApplication.translate("MainWindow", u"Mirror", None))
        self.btn_speed.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.btn_merge.setText(QCoreApplication.translate("MainWindow", u"Merge", None))
        self.btn_trim.setText(QCoreApplication.translate("MainWindow", u"Trim", None))
        self.btn_color.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Speed Effect", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Enter the value of speed", None))
        self.btn_applyspeedeffect.setText(QCoreApplication.translate("MainWindow", u"Apply Speed Effect", None))
        self.btn_previewspeedeffect.setText(QCoreApplication.translate("MainWindow", u"Preview Speed Effect", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Color Grading", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Enter Darkness level", None))
        self.btn_applycoloreffect.setText(QCoreApplication.translate("MainWindow", u"Apply Color Effect", None))
        self.btn_previewcoloreffect.setText(QCoreApplication.translate("MainWindow", u"Preview Color Effect", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Video Merge", None))
        self.btn_choosesecondclip.setText(QCoreApplication.translate("MainWindow", u"Choose Second Clip", None))
        self.btn_choosethirdclip.setText(QCoreApplication.translate("MainWindow", u"Choose Third Clip", None))
        self.label_secondclip.setText("")
        self.label_thirdclip.setText("")
        self.btn_applymerge.setText(QCoreApplication.translate("MainWindow", u"Apply Merge", None))
        self.btn_previewmerge.setText(QCoreApplication.translate("MainWindow", u"Preview Merge", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Trim Video", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Enter Starting Point", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Enter Ending Point", None))
        self.btn_applytrim.setText(QCoreApplication.translate("MainWindow", u"Apply Trim", None))
        self.btn_previewtrim.setText(QCoreApplication.translate("MainWindow", u"Preview Trim", None))
        self.label_credits.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

