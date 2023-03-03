import os

#파일이있는 경로 알아내기
main_dir = os.path.dirname(__file__)

#경로아래 있는 모드 파일
def os_listdir():
    print(f"==대상 경로 파일 리스트 os.listdir()==")
    files = os.listdir(main_dir)
    for f in files:
        print(f)

#대상 경로 및 하위 디렉토리까지 모두 탐색하여 정보를 가져옴. 
def os_walk():
    for path, dirs, files in os.walk(main_dir):
        if path == main_dir: #대상 경로의 정보만 가져오기
            print(f"==대상 경로 os.walk()==")
            print("현재경로",path)
            print("하위디렉토리",dirs)
            print("파일목록",files)
        else:
            print(f"==하위 경로 os.walk()==")
            dir_name = os.path.basename(path)
            print(f"{dir_name}-현재경로",path)
            print(f"{dir_name}-하위디렉토리",dirs)
            print(f"{dir_name}-파일목록",files)


if __name__ == '__main__':
    os_listdir()
    os_walk()
