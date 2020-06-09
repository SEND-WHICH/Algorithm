import re  # 정규식 사용
import shutil  # 셸 유틸리티

# 어떤 파일 열지 입력 (추후에 파일탐색기?)
FILE_PATH = input("검사할 파일명을 입력하세요: ")

# 복사
shutil.copy(FILE_PATH + '.txt', FILE_PATH + '(masked).txt')
            
fname = FILE_PATH + '(masked).txt'

with open(fname, 'r', encoding='UTF8') as f:
    newline=[]
    for Word in f.readlines():
        newline.append(Word.replace("f", "바뀜"))

with open(fname, 'w', encoding='UTF8') as f:
    for line in newline:
        f.writelines(line)















'''
while True:
    line = newf.readlines() # 모든 데이터를 변수로 가져온다
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
        mask = input("메롱등록번호 패턴이 탐지되었습니다. "+Nm.group()+"\n메롱등록번호를 마스킹하시겠습니까? (Y/N)\n")
        if mask=='y':
            print(Npat.sub("\g<birth>-*******", data))
            
    elif Pm: # 여권번호 패턴일 때
        mask = input("여권번호 패턴이 탐지되었습니다. " + Pm.group()+"\n여권번호를 마스킹하시겠습니까? (Y/N)\n")
        if mask=='y':
            print(Ppat.sub("\g<Ptype>*******", data))

    elif Dm: # 운전면허번호 패턴일 때
        mask = input("운전면허번호 패턴이 탐지되었습니다. "+Dm.group()+"\n운전면허번호를 마스킹하시겠습니까? (Y/N)\n")
        if mask=='y':
            print(Dpat.sub("**-**-******-**", data))

newf.close()    
#f.close()
'''
