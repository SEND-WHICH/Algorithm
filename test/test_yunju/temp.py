from struct import *
import os
import csv
import re  # 정규식 사용
import shutil  # 셸 유틸리티

from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

# 어떤 파일 열지 입력 (추후에 파일탐색기?)
FILE_PATH = input("검사할 파일명을 입력하세요: ")
#Nmask = input("주민등록번호 마스킹 여부(Y/N): ")
#Pmask = input("여권번호 마스킹 여부(Y/N): ")
Nmask = input("운전면허번호 마스킹 여부(Y/N): ")

# 복사
shutil.copy(FILE_PATH + '.docx', FILE_PATH + '(masked).docx')

data = open(FILE_PATH + '.docx', 'rb')
wordFile = data.read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

wordObj = BeautifulSoup(xml_content.decode('utf-8'))
textStrings = wordObj.findAll("w:t")

for textElem in textStrings:
    text = textElem.text
    # N 주민번호 탐지 (숫자6자리 + "-" + 숫자7자리)
    Npat = re.compile(r'(?P<birth>\d{6})[-]\d{7}|(?P<Ptype>[a-zA-Z])\d{7}|(\d{2})[-]\d{2}[-]\d{6}[-]\d{2}')
    Nm = Npat.search(text)

    if Nmask=='y':
        print(Npat.sub("**-**-******-**", text))
    # if Pmask=='y':
    #     print(Ppat.sub("\g<Ptype>*******", text))
    # if Dmask=='y':
    #     print(Dpat.sub("**-**-******-**", text))
data.close()