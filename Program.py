#!/usr/bin/env python3
import sys
import platform
from PyQt5.QtWidgets import QApplication

from MainData import MainData
from gui.MainFrame import Ui_MainFrame

def IsRunning():
    isRun = False
    pid_file = 'program.pid'
    fp = open(pid_file, 'w')
    os_txt = platform.system()
    if os_txt == "Linux":
        import fcntl
        try:
            fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except:
            isRun = True
    elif os_txt == "Windows":
        import portalocker
        try:
            portalocker.lock(fp, portalocker.LOCK_EX | portalocker.LOCK_NB)
        except:
            isRun = True
    return isRun, fp

if __name__ == "__main__":
    isRun, fp= IsRunning()
    if isRun == False:
        app = QApplication(sys.argv)
        mainData = MainData.instance(app)
        window = Ui_MainFrame()
        window.show()
        app.exec_()
        print("Program End!")
    else:
        print("Aready Running!")