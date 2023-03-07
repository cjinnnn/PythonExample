import xml.etree.ElementTree as ET
from dict2xml import dict2xml


class XmlParser:
    def __init__(self) -> None:
        pass

    def SaveFile(self, filename, data):
        f = open(filename, "w")
        f.write(self.Parse(data))
        f.close()

    def LoadFile(self, filename, data):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                readdata = file.read()
                xml = ET.fromstring(readdata)

                for x in dir(data):
                    if xml.find(x) != None:
                        if type(data[x]) == str:
                            data[x] = xml.find(x).text
                        elif type(data[x]) == int:
                            data[x] = int(xml.find(x).text)

                # for x in dir(data):
                #     if xml.find(x) != None:
                #         if type(data.__getattribute__(x)) == str:
                #             data.__setattr__(x,xml.find(x).text)
                #         elif type(data[x]) == int:
                #             data.__setattr__(x, int(xml.find(x).text))
        except Exception as e:
            print(e)

        return data

    def Parse(self, data):
        xml = dict2xml(data.__dict__, wrap ='root', indent ="    ")
        return xml

class People():
    Name = ""
    BirthDay = ""
    Telephone = ""
    Address = ""
    age = 0
    List = []
    Dic = {}

    def __getitem__(self,key):
        return getattr(self, key)
    def __setitem__(self,key,value):
        return setattr(self, key, value)

def main():
    p = People()
    p.Name = "홍길동"
    p.BirthDay = "00.00.00"
    p.Telephone = "000-0000-0000"
    p.Address= "느그집"
    p.age= 20
    p.List = ["111","222","333","444"]
    p.Dic = {"a":1,"b":2,"c":3}

    xml = XmlParser()
    print(xml.Parse(p))
    xml.SaveFile("_Test/3.xml", p)
    p = xml.LoadFile("_Test/3.xml",p)
    print(xml.Parse(p))

if __name__ == '__main__':
  main()