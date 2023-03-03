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

from enum import IntEnum
class PAGE_VIEW(IntEnum):
    MAIN = 0,

class Ui_MainFrame(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainFrame, self).__init__() ## Call the inherited classes __init__ method
        self.mainData = MainData.instance()
        uic.loadUi(os.path.join(self.mainData.dir.GUI_DIR, "MainFrame.ui"), self) #load .ui file
        self.mainData.app.aboutToQuit.connect(self.closeEvent)
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.mainData.dir.RES_DIR, "robot.png")))
        self.setWindowTitle("Python Example App")
        self.center()

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainData = MainData.instance(app)
    window = Ui_MainFrame()
    window.show()
    app.exec_()