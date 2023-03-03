#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication

from MainData import MainData
from gui.MainFrame import Ui_MainFrame

if __name__ == "__main__":
    import fcntl
    isRun = False
    pid_file = 'program.pid'
    fp = open(pid_file, 'w')
    try:
        fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except:
        isRun = True

    if isRun == False:
        app = QApplication(sys.argv)
        mainData = MainData.instance(app)
        window = Ui_MainFrame()
        window.show()
        app.exec_()
        print("Program End!")
    else:
        print("Aready Running!")