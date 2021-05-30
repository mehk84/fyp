# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashscreenOQXpmr.ui'
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

import splash_rc

class Ui_SplashScreen(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(420, 20, 331, 291))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.29, y1:0.551136, x2:1, y2:0, stop:0 rgba(179, 153, 132, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:10px solid rgb(112, 49, 55);\n"
"border-radius:120px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 180, 391, 381))
        self.label_2.setStyleSheet(u"\n"
"border:10px solid rgb(112, 49, 55) ;\n"
"border-radius: 100px;")
        self.label_2.setPixmap(QPixmap(u":/splashscreenimages/icons/default.png"))
        self.label_2.setScaledContents(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(460, 75, 261, 181))
        self.label.setPixmap(QPixmap(u":/splashscreenimages/icons/youtube-logo-png-2067.png"))
        self.label.setScaledContents(True)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(280, 450, 211, 21))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(179, 153, 132);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.557, x2:0, y2:0.545591, stop:0.920455 rgba(146, 63, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_2.raise_()
        self.frame_2.raise_()
        self.label.raise_()
        self.progressBar.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText("")
    # retranslateUi

