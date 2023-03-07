import json
import os

class JsonData():
    def __init__(self) -> None:
        pass

    def SaveData(self, data, dir:str, name:str, extension="json"):
        if not data:
            return
        if os.path.exists(dir) == False :
            os.makedirs(dir)
        filename = name
        if extension :
            filename = "{}.{}".format(name,extension)
        try:
            with open(os.path.join(dir,filename), 'w', encoding='utf-8') as f:
                json.dump(data, f, indent="\t", ensure_ascii=False) #한글 깨짐 방지 ensure_ascii=False
        except Exception as e:
            print(e)
    
    def LoadData(self, dir, name, extension="json"):
        data = None
        if os.path.exists(dir) == False :
            os.makedirs(dir)
        filename = name
        if extension :
            filename = "{}.{}".format(name,extension)
        try:
            with open(os.path.join(dir,filename), 'r') as f:
                data = json.load(f)
        except Exception as e:
            print(e)
        return data

def main():
    json_test = JsonData()
    data = {"떠든사람":["홍길동","고길동","박나래","이승기"]}
    data["안떠든사람"]=["홍진영","아이유"]
    
    json_test.SaveData(data, "./_Test","test","txt")

    load_test = json_test.LoadData("./_Test","test","txt")

    print(type(load_test) ,load_test)
  
if __name__ == '__main__':
  main()