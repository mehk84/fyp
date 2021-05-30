################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

import sys
import cv2
import numpy as np
import platform
from PyQt5.QtCore import QDir, Qt, QUrl
from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QApplication,QLabel, QFileDialog, QStyle, QVBoxLayout)
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from moviepy.editor import *

# GUI FILE
from app_modules import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('YouTube Monetization Assistant')
        UIFunctions.labelTitle(self, 'YouTube Monetization Assistant')
        UIFunctions.labelDescription(self, 'Set text')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.btn_Compression.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Compression_page))
        self.ui.btn_Home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home_page))
        self.ui.btn_Face_recognition.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.facialrecognition_page_1))
        self.ui.btn_performrecognition.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.facialrecognition_page2))
        self.ui.btn_Speech_removal.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.speechremoval_page))
        self.ui.btn_Editing.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.editing_page))
        self.ui.btn_speed.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.speed_page))
        self.ui.btn_color.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.color_page))
        self.ui.btn_merge.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.merge_page))
        self.ui.btn_trim.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.trim_page))
        self.ui.btn_compressvideo.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.compression_page2))
        self.ui.btn_startediting.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        self.ui.btn_uploadvideo.clicked.connect(self.choosevideo)
        self.ui.btn_choosesecondclip.clicked.connect(self.choosevideo2)
        self.ui.btn_choosethirdclip.clicked.connect(self.choosevideo3)
        self.ui.btn_mirror.clicked.connect(self.show_popup1)

        self.ui.btn_applymerge.clicked.connect(self.show_popup2)
        self.ui.btn_applytrim.clicked.connect(self.trim)
        self.ui.btn_applyspeedeffect.clicked.connect(self.Effects_speed)
        self.ui.btn_applycoloreffect.clicked.connect(self.Effects_color)
        self.ui.btn_applycompression.clicked.connect(self.compression)
        self.ui.btn_previewcompression.clicked.connect(self.previewvideo)
        self.ui.btn_previewcoloreffect.clicked.connect(self.previewvideo)
        self.ui.btn_previewmerge.clicked.connect(self.previewvideo)
        self.ui.btn_previewtrim.clicked.connect(self.previewvideo)
        self.ui.btn_previewspeedeffect.clicked.connect(self.previewvideo)
        self.ui.btn_performblur.clicked.connect(self.facialrecogntion)



        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home_page)   
        ## ==> END ##

        


        

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        


        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



       



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    #Upload Video Function
    def choosevideo(self):
        global fileName
        global clip1
        fileName, _ = QFileDialog.getOpenFileName(self, "Choose Video File",QDir.homePath())
        clip1=VideoFileClip(fileName)
        print(type(fileName))
        if fileName :
            msg2=QMessageBox()
            msg2.setWindowTitle("YouTube Monetization Assistant")
            msg2.setText("Your Video has been Uploaded")
            x=msg2.exec_()
        else:
            msg2=QMessageBox()
            msg2.setWindowTitle("YouTube Monetization Assistant")
            msg2.setText("Your Video did not upload!")
            x=msg2.exec_()
    #Upload Videos for merging
    def choosevideo2(self):
        global fileName2
        global clip2
        fileName2, _ = QFileDialog.getOpenFileName(self, "Choose Video File 2",QDir.homePath())
        self.ui.label_secondclip.setText(fileName2)
        clip2=VideoFileClip(fileName2)
        if fileName2 :
            msg2=QMessageBox()
            msg2.setWindowTitle("YouTube Monetization Assistant")
            msg2.setText("Your Video has been Uploaded")
            x=msg2.exec_()
        else:
            msg2=QMessageBox()
            msg2.setWindowTitle("YouTube Monetization Assistant")
            msg2.setText("Your Video did not upload!")
            x=msg2.exec_()

    def choosevideo3(self):
        global fileName3
        global clip3
        fileName3, _ = QFileDialog.getOpenFileName(self, "Open Movie",QDir.homePath())
        self.ui.label_secondclip.setText(fileName3)
        clip3=VideoFileClip(fileName3)
        if fileName :
            msg2=QMessageBox()
            msg2.setWindowTitle("YouTube Monetization Assistant")
            msg2.setText("Your Video has been Uploaded")
            x=msg2.exec_()

        else:
            msg2=QMessageBox()
            msg2.setWindowTitle("YouTube Monetization Assistant")
            msg2.setText("Your Video did not upload!")
            x=msg2.exec_()

    #Merge Popup
    def show_popup2(self):
        msg=QMessageBox()
        msg.setWindowTitle("YouTube Monetization Assistant")
        msg.setText("Do you want to perform Merging?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)

        msg.buttonClicked.connect(self.popup_button2)

        x=msg.exec_()

    def popup_button2(self,i):
        global currentvideofile
        global status
        status=i.text()
        if status=="&Yes":
            final_clip=concatenate_videoclips([clip1,clip2,clip3])
            final_clip.write_videofile("Merge. YouTube Monetization Assistant Work.mp4")
            currentvideofile="Merge. YouTube Monetization Assistant Work.mp4"
            msg2=QMessageBox()
            msg2.setWindowTitle("YouTube Monetization Assistant")
            msg2.setText("Done! Your masterpiece has been created and saved as Merge. YouTube Monetization Work.mp4")
            x=msg2.exec_()



    #Mirror Popup
    def show_popup1(self):
        msg=QMessageBox()
        msg.setWindowTitle("YouTube Monetization Assistant")
        msg.setText("Do you want to perform Mirroring?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Yes)
        msg.setDefaultButton(QMessageBox.Yes)

        msg.buttonClicked.connect(self.popup_button1)

        x=msg.exec_()

    def popup_button1(self,i):
        global status
        status=i.text()
        if status=="&Yes":
            clip_mirror=clip1.fx(vfx.mirror_x)
            clip_mirror.write_videofile("Mirror. YouTube Monetization Work.mp4")
            msg2=QMessageBox()
            msg2.setWindowTitle("YouTube Monetization Assistant")
            msg2.setText("Done! Your masterpiece has been created and saved as Mirror. YouTube Monetization Work.mp4")
            x=msg2.exec_()

    #Speed function
    def Effects_speed(self):
        global currentvideofile
        speed=float(self.ui.speed_value.text())
        clip_speed=clip1.fx(vfx.speedx,speed)
        clip_speed.write_videofile("Speed. YouTube Monetization Work.mp4")
        currentvideofile="Speed. YouTube Monetization Assistant Work.mp4"
        msg2=QMessageBox()
        msg2.setWindowTitle("YouTube Monetization Assistant")
        msg2.setText("Done! Your masterpiece has been created and saved as Speed. YouTube Monetization Work.mp4")
        x=msg2.exec_()

    #Resize function

    #Color Function
    def Effects_color(self):
        global currentvideofile

        Darkness=float(self.ui.darkness_value.text())
        clip_color=clip1.fx(vfx.colorx, Darkness)
        clip_color.write_videofile("Color. YouTube Monetization Assistant Work.mp4")
        currentvideofile="Color. YouTube Monetization Assistant Work.mp4"
        msg2=QMessageBox()
        msg2.setWindowTitle("YouTube Monetization Assistant")
        msg2.setText("Done! Your masterpiece has been created and saved as Color. YouTube Monetization Work.mp4")
        x=msg2.exec_()

    
    #Trim Function
    def trim(self):
        global currentvideofile
        s_point=float(self.ui.starting_point.text())
        e_point=float(self.ui.ending_point.text())
        clip_trim=clip1.cutout(s_point,e_point)
        msg2=QMessageBox()
        msg2.setWindowTitle("YouTube Monetization Assistant")
        msg2.setText("Please wait while your video is trimmed")
        x=msg2.exec_()
        clip_trim.write_videofile("Trim. YouTube Monetization Assistant Work.mp4")
        currentvideofile="Trim. YouTube Monetization Assistant Work.mp4"
        msg3=QMessageBox()
        msg3.setWindowTitle("YouTube Monetization Assistant")
        msg3.setText("Done! Your masterpiece has been created and saved as Trim. YouTube Monetization Work.mp4")
        x=msg3.exec_()

    def compression(self):
        global currentvideofile
        c_rate=float(self.ui.comp_rate.currentText())
        c_rate=c_rate/100
        msg2=QMessageBox()
        msg2.setWindowTitle("YouTube Monetization Assistant")
        msg2.setText("Please wait while your video is Compressed")
        x=msg2.exec_()
        compressed_video=clip1.resize(c_rate)
        compressed_video.write_videofile("Compressed. YouTube Monetization Assistant Work.mp4")
        currentvideofile="Compressed. YouTube Monetization Assistant Work.mp4"
        msg3=QMessageBox()
        msg3.setWindowTitle("YouTube Monetization Assistant")
        msg3.setText("Done! Your masterpiece has been created and saved as Compressed. YouTube Monetization Work.mp4")
        x=msg3.exec_()

    def previewvideo(self):
        capture=cv2.VideoCapture(currentvideofile)
        if (capture.isOpened()==False):
            print("Video Did not open")
        while(capture.isOpened()):
            ret,frame=capture.read()
            if ret==True:
                cv2.imshow("Frame",frame)
                if cv2.waitKey(25) & 0xFF==ord('q'):
                    break
            else:
                break
        capture.release()
        cv2.destroyAllWindows()
    def facialrecogntion(self):

        def resize(img, new_width=500):
            height,width,_ = img.shape
            ratio = height/width
            new_height = int(ratio*new_width)
            return cv2.resize(img,(new_width,new_height))

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

        cap = cv2.VideoCapture(fileName)

        while True:
            _, frame = cap.read()
            frame = resize(frame)
            detections = face_cascade.detectMultiScale(frame,scaleFactor = 1.1, minNeighbors=6)

            for face in detections:
                x,y,w,h = face
                frame[y:y+h, x:x+w] = cv2.GaussianBlur(frame[y:y+h, x:x+w], (15,15), cv2.BORDER_DEFAULT)


                cv2.imshow("output",frame)
                if cv2.waitKey(1) == 27:
                    break

        cap.release()
        cv2.destroyAllWindows()



    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
