import sys
import os

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

root_path_append("MapControl")
append_path(os.path.dirname(__file__))

# 현재 모듈이 있는 디렉토리 경로p
# m = os.path.dirname(__file__)
# sys.path.append(m)

# 1단계 상위폴더
# mm = os.path.dirname(os.path.abspath(m))
# sys.path.append(mm)

# 2단계 상위폴더
# mmm = os.path.dirname(os.path.abspath(mm))

#패키지 폴더가 이파일보다 두단계 상위폴더일 때, 패스에 추가해서...임포트
# if mmm not in sys.path:
#     sys.path.append(mmm)

#경로의 마지막 폴더이름만 가져오기
# dir_name = os.path.basename(path)


import Ros.calc_module as cm
import Module.IO.Yaml as yaml

class test_import:
    def __init__(self):
        pass

    def test(self):
        radian = cm.degree_to_radian(200)
        print(f"test {radian}")
    def yaml_test(self):
        save_data = {"a":1, "b":2}
        data = yaml.save_yaml("abc.yaml", save_data)
        data = yaml.load_yaml("abc.yaml")
        print(data)

if __name__ == "__main__":
    t = test_import()
    t.test()
    t.yaml_test()