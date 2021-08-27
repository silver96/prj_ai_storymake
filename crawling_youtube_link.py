from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time

# 동화책, 창작동화, 전래동화, 명작동화, 오디오북 링크
search_list = ['%EB%8F%99%ED%99%94%EC%B1%85', # 동화책
               '%EC%B0%BD%EC%9E%91%EB%8F%99%ED%99%94', # 창작동화
               '%EC%A0%84%EB%9E%98%EB%8F%99%ED%99%94', # 전래동화
               '%EB%AA%85%EC%9E%91%EB%8F%99%ED%99%94', # 명작동화
               '%EC%98%A4%EB%94%94%EC%98%A4%EB%B6%81'] # 오디오북

# 검색 url query= 이후는 검색어, &sp부터는 자막 필터 url
url = 'https://www.youtube.com/results?search_query=%EB%AA%85%EC%9E%91%EB%8F%99%ED%99%94&sp=EgIoAQ%253D%253D'

# 구글 드라이버 실행
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
body = driver.find_element_by_tag_name('body')

# 빈 리스트 생성
name_list = [] # 영상 제목을 담을 리스트
url_list = [] # 영상 url을 담을 리스트

num_of_pagedowns = 1000 # 스크롤 다운 횟수 설정
while num_of_pagedowns:
    body.send_keys(Keys.PAGE_DOWN) # 크롬드라이버에 page_down 입력
    time.sleep(0.1) # 로딩될 때까지 time.sleep
    num_of_pagedowns -= 1 # 한 번 스크롤다운 할 때마다 -1

soup = bs(driver.page_source, 'html.parser') # bs4에게 html parser
name = soup.select('a#video-title') # 영상 제목 태그 지정
video_url = soup.select('a#video-title') # 영상 제목 주소 태그 지정

# 영상 제목 크롤링
for i in range(len(name)): # 영상 제목 태그 갯수만큼 반복
    print(name[i]) # 영상 제목 출력
    name_list.append(name[i].text.strip()) # 영상 제목을 name_list에 text로 추가(strip을 이용하여 공백 제거)

# 영상 주소 크롤링
for i in video_url: # url 주소 내에서 반복
    url_list.append('{}{}'.format('https://www.youtube.com', i.get('href'))) # url_list f-formating 이용하여 추가 (href와 youtube 기본 url 결합)

# 크롤링한 리스트들 dic 형태로 변환
youtubeDic = {
    '제목': name_list,
    '주소': url_list}

# dataframe화
youtubeDf = pd.DataFrame(youtubeDic)

# csv 파일로 저장
youtubeDf.to_csv('명작동화.csv', encoding='', index=False)

# 구글 드라이버 종료
driver.close()
