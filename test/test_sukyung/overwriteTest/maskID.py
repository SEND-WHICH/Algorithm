'''개인정보 패턴 탐지하고 마스킹할건지 묻고, 마스킹 하기 모듈'''

import re  # 정규식 사용
import shutil  # 셸 유틸리티

# 어떤 파일 열지 입력 (추후에 파일탐색기?)
FILE_PATH = input("검사할 파일명을 입력하세요: ")

# 복사
shutil.copy(FILE_PATH + '.txt', FILE_PATH + '(masked).txt')

# 복사한 파일 이름을 매개변수에 저장     
fname = FILE_PATH + '(masked).txt'

# 읽기 모드에서 파일 열고 내용을 목록으로 복사하기
with open(fname, 'r', encoding='UTF8') as f:
    newline=[]
    for Word in f.readlines():
        
        #주민번호 패턴 탐지
        patternID = re.compile("(?P<birth>\d{6})[-](?P<maskID>\d{7})")
        msgID = patternID.search(Word)

        # 주민번호 패턴일 때
        if msgID:
            mask = input("주민등록번호 패턴이 탐지되었습니다. "+msgID.group()+"\n주민등록번호를 마스킹하시겠습니까? (Y/N)\n")
            if mask=='y':
                print(patternID.sub("\g<birth>-*******", msgID.group()))
                newline.append(Word.replace(msgID.group(), patternID.sub("\g<birth>-*******", msgID.group())))
            else :
                newline.append(Word)
        else :
            newline.append(Word)
        

# 쓰기 모드에서 파일 열고 업데이트 된 데이터 파일에 쓰기
with open(fname, 'w', encoding='UTF8') as f:
    for line in newline:
        f.writelines(line)


# 참고 사이트
# https://www.it-swarm.dev/ko/python/python%EC%97%90%EC%84%9C-%ED%85%8D%EC%8A%A4%ED%8A%B8-%ED%8C%8C%EC%9D%BC%EC%9D%98-%ED%8A%B9%EC%A0%95-%EC%A4%84-%ED%8E%B8%EC%A7%91/971925982/
















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
