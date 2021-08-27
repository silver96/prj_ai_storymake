# prj_ai_storymake

프로젝트 진행 순서

< 1. 데이터 수집 >

crawling_youtube_link.py : 유튜브 링크 수집
download_subtitiles.py : 수집한 링크에 존재하는 자막 다운
no_down_subtitles_link.py : 자동화로 다운되지 못한 링크 수작업 위한 링크 추출 
concat_story.py : 모은 동화 하나로 합침


< 2. 데이터 전처리 >

preprocess_kkm_hanspell.ipynb : kkm와 hanspell 이용하여 전처리 성능 비교 => hanspell우수
kaist_data_preprocess.ipynb : 음성학습 위한 kaist데이터로 한국어 동화 추가


< 3. 모델링 >

open ai의 인증키 활용하여 웹상에서 모델링


< 4. 모델성능확인 >

model_test.ipynb : 생성된 모델에 키워드 입력하여 비교


< 5. 음성학습 >

각 음성의 특징은 인식 되나, 잡음이 많이 섞이고 시관관계상 어플 구현 X
