import yaml

# YAML 파일 로드 후 데이터 리턴
def load_yaml(path):
    data = None
    try:
        with open(path) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
    except:
        pass
    return data

# YAML 파일 유니코드로 저장
def save_yaml(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data,f,allow_unicode=True)
    except:
        pass

def main():
    #테스트 1
    test_data = {"떠든사람":["홍길동","고길동","박나래","이승기"]}
    test_data["안떠든사람"]=["홍진영","아이유"]
    save_yaml("test.yaml", test_data)
    data = load_yaml("test.yaml")
    print(data)
    
    #테스트2
    test_data = {"홍길동":32, "박나래":34, "고길동":40}
    save_yaml("test2.yaml", test_data)
    data = load_yaml("test2.yaml")
    print(data)

if __name__ == '__main__':
    main()