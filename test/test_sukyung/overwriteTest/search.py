''' 실제 test용 파일: 파일에 대해서 개인정보 검사하고 뭐뭐 나왔나 string에 저장 '''

import re  # 정규식 사용
import shutil  # 셸 유틸리티

# 어떤 파일 열지 입력 (json으로 받아오기)
# json 파일 이름: example
with open('example.json') as json_file:
    json_data = json.lead(json_file)
    # key가 json_title인 문자열 가져오기 (json_title: 검사 파일 이름)
    title = json_data["json_title"]
    print(json_string)
    # 확장자명(fileType)과 순수 파일명(fileTitle)으로 나누기
    fileTitle = title.split('.')[0]
    fileType = title.split('.')[1]
    print(fileTitle)
    print(fileType)

# 복사
shutil.copy(fileTitle+'.'+fileType, fileTitle + '(masked).' + fileType)


# 복사한 파일 이름을 매개변수에 저장     
fname = fileTitle + '(masked).' + fileType

# 개인정보 횟수 카운트 변수 선언하고 초기화
numID = 0 #주민등록번호 카운트
numPP = 0 #여권번호 카운트
numD = 0 #운전면허번호 카운트
numPH = 0 #핸드폰번호 카운트
numF = 0 #외국인등록번호 카운트
numC = 0 #신용카드번호 카운트
numHI = 0 #건강보험번호 카운트
numA = 0 #계좌번호 카운

# 읽기 모드에서 파일 열고 내용을 목록으로 복사하기
with open(fname, 'r', encoding='UTF8') as f:
    newline=[]
    for Word in f.readlines():

        '''_________________패턴 탐지_________________ '''
        #주민번호 패턴 탐지
        patternID = re.compile("(?P<birth>\d{6})[-](?P<maskID>\d{7})")
        msgID = patternID.search(Word)

        #여권번호 패턴 탐지
        patternPP = re.compile("[a-zA-Z]{2}[-~.[:space:]][0-9]{7}")
        msgPP = patternID.search(Word)

        #운전면허번호 패턴 탐지
        patternD = re.compile("(\d{2})[-]\d{2}[-]\d{6}[-]\d{2}")
        msgD = patternID.search(Word)
'''
        #핸드폰번호 패턴 탐지
        patternD = re.compile("(\d{2})[-]\d{2}[-]\d{6}[-]\d{2}")
        msgD = patternID.search(Word)

        #외국인등록번호 패턴 탐지
        patternD = re.compile("(\d{2})[-]\d{2}[-]\d{6}[-]\d{2}")
        msgD = patternID.search(Word)

        #신용카드번호 패턴 탐지
        patternD = re.compile("(\d{2})[-]\d{2}[-]\d{6}[-]\d{2}")
        msgD = patternID.search(Word)

        #건강보험번호 패턴 탐지
        patternD = re.compile("(\d{2})[-]\d{2}[-]\d{6}[-]\d{2}")
        msgD = patternID.search(Word)

        #계좌번호 패턴 탐지
        patternD = re.compile("(\d{2})[-]\d{2}[-]\d{6}[-]\d{2}")
        msgD = patternID.search(Word)
'''

        '''_________________패턴 마스킹_________________ '''
        if msgID:
            numID += 1

        if msgPP:
            numPP += 1

        if msgD:
            numD += 1

'''
# 검사 종료 후 결과 출력 (result: 문자열 저장)
 #print("< 탐지된 개인정보 목록 >")
result = '< 탐지된 개인정보 목록 >\n'
if numID > 0:
    result += "주민등록번호: " + str(numID) + "개\n"
     #print("주민등록번호: " + str(numID) + "개")
if numPP > 0:
    result += "여권번호: " + str(numPP) + "개\n"
     #print("여권번호: " + str(numPP) + "개")
if numD > 0:
    result += "운전면허번호: " + str(numD) + "개\n"
     #print("운전면허번호: " + str(numD) + "개")
if numID == 0 and numPP == 0 and numD == 0:
    result += "탐지된 개인정보가 없습니다."
     #print("탐지된 개인정보가 없습니다.")

print(result)
'''       



# 참고 사이트
# https://www.it-swarm.dev/ko/python/python%EC%97%90%EC%84%9C-%ED%85%8D%EC%8A%A4%ED%8A%B8-%ED%8C%8C%EC%9D%BC%EC%9D%98-%ED%8A%B9%EC%A0%95-%EC%A4%84-%ED%8E%B8%EC%A7%91/971925982/
# 
