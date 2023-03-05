import sys
import os

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

from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from MainData import MainData

class pageSecond(QWidget):
    def __init__(self):
        super(pageSecond, self).__init__() ## Call the inherited classes __init__ method
        self.mainData = MainData.instance()
        uic.loadUi(os.path.join(self.mainData.dir.GUI_DIR, "pageSecond.ui"), self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainData = MainData.instance(app)
    window = pageSecond()
    window.show()
    app.exec_()
    
