# readline_test.py
# 정규식 사용
import re

f = open("텍스트 문서 test.txt", 'r', encoding='UTF8')
while True:
    line = f.readline()
    if not line: break
    data = line

    # 주민번호 탐지 (숫자6자리 + "-" + 숫자7자리)
    pat1 = re.compile("(\d{6})[-]\d{7}")
    m1 = pat1.search(data)
    if m1:
        mask1 = input("주민등록번호가 탐지되었습니다. "+m1.group()+"\n주민등록번호를 마스킹하시겠습니까? (Y/N)\n")
        if mask1=='y':
            print(pat1.sub("\g<1>-*******", data))
        else:
            print(data)

    # 여권번호 탐지 (신 전자 여권번호 (M1234567형태))
    pat2 = re.compile("[a-zA-Z]\d{7}")
    m2 = pat2.search(data)
    if m2:
        mask2 = input("여권번호가 탐지되었습니다. " + m2.group()+"\n여권번호를 마스킹하시겠습니까? (Y/N)\n")
        if mask2=='y':
            print(pat.sub("\g<1>*******", data))

f.close()
