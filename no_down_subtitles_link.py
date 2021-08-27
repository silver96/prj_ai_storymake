#자동 자막 다운로드 코드로 수행되지 않은 것들 따로 추출하여 수작업으로 자막 다운로드 수행

# 모듈 임포트!
import glob
import pandas as pd
import re

df = pd.read_csv('../crawling_data/total_link_du.csv', index_col=0) # csv 파일 열어서 변수에 저장
filelist = glob.glob('./files/*.txt') # glob을 이용하여 파일명 리스트로 반환

filename = [] # 빈 리스트 생성

# 크롤링된 영상 목록
for file in filelist:
    file = file.split('[Korean] ')[1] # [Korean] 기준으로 split하고 두번째 index 가져오기
    file = file.split(' [DownSub.com]')[0] # [DownSub.com] 기준으로 split하고 첫번째 index 가져오기
    # print(file)
    file = re.compile('[^가-힣]').sub('',file) # re 모듈의 compile과 정규표현식을 이용하여 한글만 추출하고 sub을 이용하여 띄어쓰기를 치환
    print(file)
    filename.append(file) # filename 리스트에 file 추가

# 빈 리스트들 생성
links = []
notname = []

# 크롤링이 완료되지 않은 영상 링크만 수집
for i in range(len(df)):
    name = df.iloc[i, 0] # iloc을 이용하여 i번째 첫번째 열 추출
    name = re.compile('[^가-힣]').sub('', name) # re 모듈의 compile과 정규표현식을 이용하여 한글만 추출하고 sub을 이용하여 띄어쓰기를 치환
    print(name) # 출력해보기
    if name not in filename: # filename에 name에 없으면
        link = df.iloc[i, 1] # iloc을 이용하여 i번재 두번째 열 추출
        notname.append(name) # name이 없으면 notname 리스트에 추가
        links.append(link) # name이 없으면 links 리스트에 추가

print(links)

# 새로운 dataframe 생성
df2 = pd.DataFrame(columns = ['제목', 'URL'])
df2['제목'] = notname
df2['URL'] = links

print(df2)

# 생성된 dataframe 저장
df2.to_csv('nurac.csv', encoding='utf-8')
