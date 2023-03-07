import os
import pickle

class PickleData():
    def __init__(self) -> None:
        pass
    
    def SaveData(self, data, dir:str, name:str, extension="bin"):
        if not data:
            return
        if os.path.exists(dir) == False :
            os.makedirs(dir)
        filename = name
        if extension :
            filename = "{}.{}".format(name,extension)
        try:
            with open(os.path.join(dir,filename), 'wb') as f:
                pickle.dump(data, f)
        except Exception as e:
            print(e)
    
    def LoadData(self, dir, name, extension="bin"):
        data = None
        if os.path.exists(dir) == False :
            os.makedirs(dir)
        filename = name
        if extension :
            filename = "{}.{}".format(name,extension)
        try:
            with open(os.path.join(dir,filename), 'rb') as f:
                data = pickle.load(f)
        except Exception as e:
            print(e)
        return data

class People():
    def __init__(self, name, birth, tel, addr) -> None:
        self.Name = name
        self.BirthDay = birth
        self.Telephone = tel
        self.Address = addr

def main():
    pic_test = PickleData()
    data = []
    data.append(People("홍길동","00.00.00", "000-0000-0000","집"))
    data.append(People("홍길순","01.01.01", "001-0001-0001","집"))
    data.append(People("광개토","02.02.02", "002-0002-0002","집"))
    data.append(People("이성계","33.33.33", "003-0003-0003","집"))
    
    pic_test.SaveData(data, "./_Test","people","bin")

    load_test = pic_test.LoadData("./_Test","people","bin")
    for x in load_test:
        print(x.__dict__)
  
if __name__ == '__main__':
  main()