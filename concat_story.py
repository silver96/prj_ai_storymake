#최종데이터 CONCAT코드
import glob
import pandas as pd
import re
import os

filelist = glob.glob('./최종데이터/*.txt')

with open('total_story.txt', 'w', encoding='utf-8') as f:
    for i in range(len(filelist)):
        file_path = filelist[i]
        with open(file_path, 'r', encoding='utf-8') as d:
            print(d)
            f.write(str(d.read()))
            f.write('////////'*10 + '\n'*3)
    print(f)
