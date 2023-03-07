import os
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml
import xmltodict
#설치해야 함 : pip install dicttoxml
#설치해야 함 : pip install xmltodict

class XmlParser:
    def __init__(self) -> None:
        pass

    def SaveFile(self, filename, data):
        with open(filename, "w", encoding='utf-8') as f:
            f.write(self.Parse(data))
            f.close()

    def LoadFile(self, filename, data):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                readdata = f.read()
                f.close()

                # 읽은 데이터를, 딕셔너리로 바꾼 뒤에, 클래스에 집어넣는다.
                xml_dic = xmltodict.parse(readdata)
                root_name = type(data).__name__
                for x in dir(data):
                    if x in xml_dic[root_name]:
                        if type(data[x]) == int:
                            data[x] = int(xml_dic[root_name][x])
                        elif type(data[x]) == float:
                            data[x] = float(xml_dic[root_name][x])
                        elif type(data[x]) == bool:
                            data[x] = bool(xml_dic[root_name][x])
                        else:
                            data[x] = xml_dic[root_name][x]
        except Exception as e:
            print(e)
        return data

    def Parse(self, data):
        xml = dicttoxml(data.__dict__, attr_type = False, custom_root=type(data).__name__)
        dom = parseString(xml)
        return dom.toprettyxml()

class People():
    Name = ""
    BirthDay = ""
    Telephone = ""
    Address = ""
    age = 0
    List = []
    Dic = {}

    # 클래스를 딕셔너리 처럼 사용하게 해주는 스페셜 펑션
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
    
    #저장
    xml = XmlParser()
    print("저장 데이터\n",xml.Parse(p))
    xml.SaveFile("_Test/0.xml", p)

    #로드
    pp = People()
    pp = xml.LoadFile("_Test/0.xml",pp)
    print("로드 데이터\n",xml.Parse(pp))

if __name__ == '__main__':
  main()


"""
    # p = People("홍길동","00.00.00", "000-0000-0000","집", 30)

    # xml = dicttoxml(p.__dict__, attr_type = False)
    # xml_decode = xml.decode()
    # SaveFile("1.xml", xml_decode)
    
    # dom = parseString(xml)
    # SaveFile("2.xml", dom.toprettyxml())

    # data = LoadFile("1.xml")
    # pXml = ET.fromstring(data)
    # p = []
    # p.append(pXml.find("Name").text)
    # p.append(pXml.find("BirthDay").text)
    # p.append(pXml.find("Telephone").text)
    # p.append(pXml.find("Address").text)
    # p.append(int(pXml.find("age").text))
    # pp = People(p[0],p[1],p[2],p[3],p[4])
    # print(p, pp)

    # res = LoadFile("1.xml")
    # my_dict = xmltodict.parse(res)

    # #새로 생성한다...
    # pp = People(my_dict["root"]["Name"],my_dict["root"]["BirthDay"],my_dict["root"]["Telephone"],my_dict["root"]["Address"],int(my_dict["root"]["age"]))
    # print(pp)

"""