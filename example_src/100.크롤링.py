import requests
import bs4


def naver_webtoon():
    req = requests.get("https://comic.naver.com/webtoon/weekday")
    html = bs4.BeautifulSoup(req.text, 'html.parser')
    columns = html.find_all('div', {'class':'col_inner'})

    for column in columns:
        day = column.find('h4').text
        webtoons = column.find_all('a', {'class' : 'title'})[:5]
        print(day)
        for index in range(len(webtoons)):
            title = webtoons[index].text
            print(f"{index+1}. {title}")
        print()

def naver_qna():
    req = requests.get("https://kin.naver.com/qna/list.naver")
    html = bs4.BeautifulSoup(req.text, 'html.parser')
    titles = html.find_all('td', {'class':'title'})
    for t in titles:
        data = t.find('a')
        title = data.text
        link = "https://kin.naver.com/"+data.attrs["href"]
        print(f"{title} : {link}")

def lotto():
    URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
    raw = requests.get(URL)
    html = bs4.BeautifulSoup(raw.text, 'html.parser')
    target = html.find('div', {'class' : 'nums'})
    balls = target.find_all("span", {'class' : 'ball_645'},)
    for ball in balls[:-1]:
        print(f"당첨번호 : {ball.text}")
    print("보너스 번호 : ", balls[-1].text)

def gmarket():
    while True:
        keyword = input("지마켓 검색 키워드 : ")
        if keyword == "q":
            break
        URL = "https://browse.gmarket.co.kr/search?keyword="+keyword
        raw = requests.get(URL)
        html = bs4.BeautifulSoup(raw.text, 'html.parser')
        target = html.find('div', {'class' : 'section__module-wrap', 'module-design-id':'15'})
        items = target.find_all("div", {'class' : 'box__item-container'})
        for item in items:
            title = item.find("span", {"class":"text__item"})
            price = item.find("strong", {"class":"text__value"})
            print(title.text,price.text)

def naver_news():
    while True:
        keyword = input("뉴스 검색 키워드 : ")
        if keyword == "q":
            break

        URL = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + keyword
        raw = requests.get(URL)
        html = bs4.BeautifulSoup(raw.text, 'html.parser')
        main_pack = html.find('div', {'class' : 'main_pack'})
        group_news = main_pack.find('ul', {'class' : 'list_news'})
        news_items = group_news.find_all('div', {'class': 'news_area'})
        for news in news_items:
            title = news.find("a", {"class":"news_tit"})
            div_desc = news.find("div", {'class': 'dsc_wrap'})
            desc = div_desc.find("a",{"class":"api_txt_lines dsc_txt_wrap"})
            link = desc["href"]
            print("제목: ",title.text)
            print("내용: ",desc.text)
            print("링크: ",link)
            print()

if __name__ == "__main__":
    naver_news()
