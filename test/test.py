# readline_test.py
# 정규식 사용
import re

f = open("텍스트 문서 test.txt", 'r', encoding='UTF8')
while True:
    line = f.readline()
    if not line: break
    data = line

    # 주민번호 탐지 
    pat = re.compile("(\d{6})[-]\d{7}")
    m = pat.search(data)
    if m:
        mask = input("주민번호가 탐지되었습니다. "+m.group()+"\n마스킹하시겠습니까? (Y/N)\n")
        if mask=='y':
            print(pat.sub("\g<1>-*******", data))
        else:
            print(data)
f.close()
