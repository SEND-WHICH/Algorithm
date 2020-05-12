# readline_test.py
# 정규식 사용
import re

# 어떤 파일 열지 입력 (추후에 파일탐색기?)
FILE_PATH = input("검사할 파일명을 입력하세요: ")

f = open(FILE_PATH, 'r', encoding='UTF8')
while True:
    line = f.readline()
    if not line: break
    data = line

    # N 주민번호 탐지 (숫자6자리 + "-" + 숫자7자리)
    Npat = re.compile("(?P<birth>\d{6})[-]\d{7}")
    Nm = Npat.search(data)

    # P 여권번호 탐지 (신 전자 여권번호 (M1234567형태))
    Ppat = re.compile("(?P<Ptype>[a-zA-Z])\d{7}")
    Pm = Ppat.search(data)

    # D 운전면허번호 탐지
    Dpat = re.compile("(\d{2})[-]\d{2}[-]\d{6}[-]\d{2}")
    Dm = Dpat.search(data)

    
    if Nm: # 주민번호 패턴일 때
        mask = input("주민등록번호 패턴이 탐지되었습니다. "+Nm.group()+"\n주민등록번호를 마스킹하시겠습니까? (Y/N)\n")
        if mask=='y':
            print(Npat.sub("\g<birth>-*******", data))
        else:
            print(data)
            
    elif Pm: # 여권번호 패턴일 때
        mask = input("여권번호 패턴이 탐지되었습니다. " + Pm.group()+"\n여권번호를 마스킹하시겠습니까? (Y/N)\n")
        if mask=='y':
            print(Ppat.sub("\g<Ptype>*******", data))
        else:
            print(data)

    elif Dm: # 운전면허번호 패턴일 때
        mask = input("운전면허번호 패턴이 탐지되었습니다. "+Dm.group()+"\n운전면허번호를 마스킹하시겠습니까? (Y/N)\n")
        if mask=='y':
            print(Dpat.sub("**-**-******-**", data))
        else:
            print(data)
            

            
    
f.close()
