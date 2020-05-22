try:
    file = open('test.txt','rb')
    while True:
        temp = file.read(1)
        if temp == '' : break
        ## temp type 'bytes'
        print("%02x "% ord(temp),end='')
        ##ex) ord('a') -> 97 chr(97) -> 'a'
    file.close()
except IOError:
    print("IO error")
#
# import re  # 정규식 사용
# import shutil  # 셸 유틸리티
#
# # 어떤 파일 열지 입력 (추후에 파일탐색기?)
# FILE_PATH = input("검사할 파일명을 입력하세요: ")
#
# # 복사
# shutil.copy(FILE_PATH + '.txt', FILE_PATH + '(masked).txt')
#
# # f = open(FILE_PATH+'.txt', 'r', encoding='UTF8')
# newf = open(FILE_PATH + '(masked).txt', 'r+', encoding='UTF8')
#
# while True:
#     line = newf.readline()
#     if not line: break
#     data = line
#
#     # N 주민번호 탐지 (숫자6자리 + "-" + 숫자7자리)
#     Npat = re.compile("(?P<birth>\d{6})[-]\d{7}")
#     Nm = Npat.search(data)
#
#     # P 여권번호 탐지 (신 전자 여권번호 (M1234567형태))
#     Ppat = re.compile("(?P<Ptype>[a-zA-Z])\d{7}")
#     Pm = Ppat.search(data)
#
#     # D 운전면허번호 탐지
#     Dpat = re.compile("(\d{2})[-]\d{2}[-]\d{6}[-]\d{2}")
#     Dm = Dpat.search(data)
#
#     if Nm:  # 주민번호 패턴일 때
#         mask = input("주민등록번호 패턴이 탐지되었습니다. " + Nm.group() + "\n주민등록번호를 마스킹하시겠습니까? (Y/N)\n")
#         if mask == 'y':
#             print(Npat.sub("\g<birth>-*******", data))
#
#     elif Pm:  # 여권번호 패턴일 때
#         mask = input("여권번호 패턴이 탐지되었습니다. " + Pm.group() + "\n여권번호를 마스킹하시겠습니까? (Y/N)\n")
#         if mask == 'y':
#             print(Ppat.sub("\g<Ptype>*******", data))
#
#     elif Dm:  # 운전면허번호 패턴일 때
#         mask = input("운전면허번호 패턴이 탐지되었습니다. " + Dm.group() + "\n운전면허번호를 마스킹하시겠습니까? (Y/N)\n")
#         if mask == 'y':
#             print(Dpat.sub("**-**-******-**", data))
#
# newf.close()

import re  # 정규식 사용

# text 읽기
file0 = open('test.txt', 'rb')
text = file0.read()
file0.close()
file1 = open('test.docx', 'rb')

text = file1.read()
print(text)
text = str(text)
Ppat = re.compile("\x39\x38\x30\x33\x30\x35\x2d\x31\x32\x33\x34\x35\x36\x37")
Pm = Ppat.search(str(text))
mask = input("여권번호 패턴이 탐지되었습니다. " + "980305-1234567" + "\n여권번호를 마스킹하시겠습니까? (Y/N)\n")
if mask == 'y':
    print(Ppat.sub("[\x39][\x38][\x30][\x33][\x30][\x35][-][\x2a][\x2a][\x2a][\x2a][\x2a][\x2a][\x2a]", text))


file1.close()
text = bytes("b'"+text+"'")
file2 = open('examine.docx', 'wb')
file2.write(text)
file2.close()


# # binary 파일( 이미지 파일 ) copy하기
# file2 = open('anonymous.png', 'rb')
# data = file2.read()
# print(type(data))        # <class 'bytes'>
# print(data)
#
# file2.close()
#
# file3 = open('example_img2.png', 'wb')
# file3.write(data)
# file3.close()
