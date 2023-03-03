import sys
import os

class SingletonInstance:
    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

class ProgramDir:
    MAIN_DIR = os.path.dirname(__file__)
    RES_DIR = os.path.join(MAIN_DIR,"res")
    GUI_DIR = os.path.join(MAIN_DIR,"gui")
    def __init__(self):
        self.InitPath()
        
    def append_path(self, path):
        if path not in sys.path:
            sys.path.append(path)
    def InitPath(self):
        self.append_path(self.MAIN_DIR)
        self.append_path(self.RES_DIR)
        self.append_path(self.GUI_DIR)

class MainData(SingletonInstance):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.dir = ProgramDir()