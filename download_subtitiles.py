# 모듈 임포트!
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

df = pd.read_csv('../crawling_data/total_link_du.csv',) # csv파일 열어서 변수에 저장
df = df['주소'] # '주소' column만 추출
link = [] # 빈 리스트 생성

# 추출한 '주소' 컬럼에서 for문 반복
for d in df:
    link.append(d) # 추출한 주소 빈 리스트에 담기
# print(link[0])

# 한글 자막 추출
for i in range(0, 1401): #1401: 수집된 url총 개수 #range(len(df))
    l = link[i][-11:] # 바뀌는 마지막 11글자 인덱싱
    url = 'https://downsub.com/?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D' + l # 자막 다운로드를 위한 url 생성
    driver = webdriver.Chrome('./chromedriver.exe') # 크롬 드라이버 실행
    driver.get(url) # 드라이버에 url 주소 부여
    time.sleep(1.5) # 로딩까지 1.5초 time sleep
    try:
        for m in range(5): # 5까지 지정한 이유는 자막이 다양한 언어로 있을 경우에 한국어가 밑으로 내려가는 현상이 발생하기 때문
            try:
                btn = driver.find_element_by_xpath(f'//*[@id="app"]/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div[{m}]/button[@data-title="[TXT] Korean"]') # 한글자막 xpath 주소 부여
                btn.click() # 클릭
                time.sleep(3) # 다운로드까지 3초 time sleep
            except:
                pass # 미존재 시 pass


    except:
        continue
    driver.quit() # 드라이버 종료
