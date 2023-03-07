from configparser import ConfigParser
import os
from Data.MainData import DIR_SET

class Ini():
    def __init__(self, name) -> None:
        self.ConfigName = name
        self.InitConfig()

    def InitConfig(self):
        dir = DIR_SET #'./_set'
        if os.path.exists(dir) == False :
            os.makedirs(dir)
        self.file_path = os.path.join(dir,  self.ConfigName+'.ini')

        self.config = ConfigParser()
        self.config.read(self.file_path)
    
    def setValue(self, section, key, val):
        if self.config.has_section(section) == False:
            self.config.add_section(section)

        self.config.set(section, key, str(val))
        try:
            with open(self.file_path, 'w') as f:
                self.config.write(f)
        except Exception as e:
            print(e)
    
    def getValue(self, section, key, default):
        result = None
        try:
            result = self.config.get(section, key)
            print("[{}] {}: {}".format(section, key, result))
        except:
            result = default
        return result;
    
    def getFloat(self, section, key, default):
        result = None
        try:
            result = self.config.getfloat(section, key)
            print("[{}] {}: {}".format(section, key, result))
        except:
            result = default
        return result;

    def getInt(self, section, key, default):
        result = None
        try:
            result = self.config.getint(section, key)
            print("[{}] {}: {}".format(section, key, result))
        except:
            result = default
        return result;
    
    def getBool(self, section, key, default):
        result = None
        try:
            result = self.config.getboolean(section, key)
            print("[{}] {}: {}".format(section, key, result))
        except:
            result = default
        return result;
