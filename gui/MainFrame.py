#!/usr/bin/env python3
import math
import string
import sys
import os
import datetime

#단독 실행 할 때는 메인 경로 추가 해 줘야 함
if __name__ == "__main__":
    def append_path(path):
        if path not in sys.path:
            sys.path.append(path)
    def get_top_dir_path(name):
        path = os.path.dirname(__file__)
        while True:
            path = os.path.dirname(os.path.abspath(path))
            dir_name = os.path.basename(path)
            if dir_name == name:
                break
            elif  dir_name == '':
                path = None
        return path
    def root_path_append(root_name):
        path =  get_top_dir_path(root_name)
        append_path(path)
        append_path(os.path.dirname(__file__))
    root_path_append("PythonExample")

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from MainData import MainData

import gui.pageHome, gui.pageSecond, gui.pageThird

from enum import IntEnum
class PAGE_VIEW(IntEnum):
    HOME = 0,
    SECOND = 1,
    THIRD = 2,

class Ui_MainFrame(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainFrame, self).__init__()
        self.mainData = MainData.instance()
        uic.loadUi(os.path.join(self.mainData.dir.GUI_DIR, "MainFrame.ui"), self)
        self.mainData.app.aboutToQuit.connect(self.closeEvent)
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.mainData.dir.RES_DIR, "assignment_add.svg")))
        self.setWindowTitle("Python Example App")
        self.center()
        
        self.showMaximaizeMode = False
        self.CurrentView = [PAGE_VIEW.HOME,self.toolButton_1]
        self.Side_Menu_Num = 0
        self.InitTopBar()
        self.setPageButton()
        self.InitPage()

    # 화면의 가운데로 띄우기
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        quit_msg = "Do you wan't Quit?"
        reply = QMessageBox.question(self, 'Quit', quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            print('Program Close!')
            event.accept()
        else:
            print('Program Close Cancel!')
            event.ignore()

    def Screen_Maximized(self):
        if self.showMaximaizeMode == False:
            self.showMaximized()
            self.showPage(self.CurrentView[0], self.CurrentView[1])
            self.showMaximaizeMode = True
        else:
            self.showNormal()
            self.showPage(self.CurrentView[0], self.CurrentView[1])
            self.showMaximaizeMode = False

    def InitTopBar(self):
        self.btnMenu:QPushButton = self.btnMenu
        self.btnInfo:QPushButton = self.btnInfo
        self.btnMenu.clicked.connect(lambda: self.Side_Menu_Slider())
        self.btnInfo.clicked.connect(lambda: QMessageBox.warning(self, "Info", "Show Message!"))

        self.dragPos = QtCore.QPoint()
        self.lblTitle:QLabel = self.lblTitle
        self.lblTitle.mousePressEvent = self.lblAppName_mousePressEvent
        self.lblTitle.mouseMoveEvent = self.lblAppName_mouseMoveEvent
        self.lblTitle.mouseDoubleClickEvent = self.lblAppName_mouseDoubleClickEvent

    def lblAppName_mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def lblAppName_mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.dragPos = event.globalPos()

    def lblAppName_mouseDoubleClickEvent(self, event):
        self.Screen_Maximized()

    def Side_Menu_Slider(self):
        min_w = 70
        max_w = 170
        duration = 200
        if self.Side_Menu_Num == 0:
            self.animation1 = QtCore.QPropertyAnimation(self.MenuBar, b"maximumWidth")
            self.animation1.setDuration(duration)
            self.animation1.setStartValue(min_w)
            self.animation1.setEndValue(max_w)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()

            self.animation2 = QtCore.QPropertyAnimation(self.MenuBar, b"minimumWidth")
            self.animation2.setDuration(duration)
            self.animation2.setStartValue(min_w)
            self.animation2.setEndValue(max_w)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()
            self.Side_Menu_Num = 1
        else:
            self.animation1 = QtCore.QPropertyAnimation(self.MenuBar, b"maximumWidth")
            self.animation1.setDuration(duration)
            self.animation1.setStartValue(max_w)
            self.animation1.setEndValue(min_w)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()
            
            self.animation2 = QtCore.QPropertyAnimation(self.MenuBar, b"minimumWidth")
            self.animation2.setDuration(duration)
            self.animation2.setStartValue(max_w)
            self.animation2.setEndValue(min_w)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()
            self.Side_Menu_Num = 0

    def setPageButton(self):
        self.toolButton_1:QToolButton = self.toolButton_1
        self.toolButton_2:QToolButton = self.toolButton_2
        self.toolButton_3:QToolButton = self.toolButton_3
        
        self.MenuBar:QFrame = self.MenuBar

        self.toolButton_1.clicked.connect(lambda: self.showPage(PAGE_VIEW.HOME, self.toolButton_1))
        self.toolButton_2.clicked.connect(lambda: self.showPage(PAGE_VIEW.SECOND, self.toolButton_2))
        self.toolButton_3.clicked.connect(lambda: self.showPage(PAGE_VIEW.THIRD, self.toolButton_3))


    def InitPage(self):
        self.mdiArea:QMdiArea = self.mdiArea
        w = self.mdiArea.width()
        h = self.mdiArea.height()

        self.vHome = QMdiSubWindow()
        self.vHome.setWindowFlag(Qt.FramelessWindowHint)
        self.vHome.setGeometry(0, 0, w, h)
        self.vHome.setWidget(gui.pageHome.pageHome())
        self.mdiArea.addSubWindow(self.vHome)

        self.vSecond = QMdiSubWindow()
        self.vSecond.setWindowFlag(Qt.FramelessWindowHint)
        self.vSecond.setGeometry(0, 0, w, h)
        self.vSecond.setWidget(gui.pageSecond.pageSecond())
        self.mdiArea.addSubWindow(self.vSecond)

        self.vThird = QMdiSubWindow()
        self.vThird.setWindowFlag(Qt.FramelessWindowHint)
        self.vThird.setGeometry(0, 0, w, h)
        self.vThird.setWidget(gui.pageThird.pageThird())
        self.mdiArea.addSubWindow(self.vThird)

        self.showPage(PAGE_VIEW.HOME, self.toolButton_1)

    def showPage(self, page_no, selBtn):
        beforeWin = self.mdiArea.activeSubWindow()
        if page_no == PAGE_VIEW.SECOND:
            if self.vSecond.isMaximized() == False:
                self.vSecond.showMaximized()
            self.mdiArea.setActiveSubWindow(self.vSecond)
        elif page_no == PAGE_VIEW.THIRD:
            if self.vThird.isMaximized() == False:
                self.vThird.showMaximized()
            self.mdiArea.setActiveSubWindow(self.vThird)
        else:
            if self.vHome.isMaximized() == False:
                self.vHome.showMaximized()
            self.mdiArea.setActiveSubWindow(self.vHome)

        #페이지가 정상적으로 바꼈으면.. 다른창은 숨기고...버튼색바꿈.
        currentWin = self.mdiArea.activeSubWindow()
        for v in self.mdiArea.subWindowList():
            if currentWin != v:
                v.hide()
        if beforeWin != currentWin: #처음과 다르면..
            self.CurrentView = [page_no,selBtn]
            for toolBtn in self.MenuBar.findChildren(QToolButton):
                if toolBtn == selBtn:
                    self.setBgColor(toolBtn, True)
                else:
                    self.setBgColor(toolBtn, False)

    def setBgColor(self, btn, onoff):
        if onoff == True:
            btn.setStyleSheet("""
            QToolButton{
                background-color: rgb(80,80,80);
                color: gold;
                font-weight:bold;
            }
            """)
        else:
            btn.setStyleSheet("""
            QToolButton{
                background-color: rgb(20,20,20);
                color: white;
                font-weight:bold;
            }

            QToolButton:hover{
                color: gold;
                background: rgb(80,80,0);
                border: none;
            }
            """)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainData = MainData.instance(app)
    window = Ui_MainFrame()
    window.show()
    app.exec_()