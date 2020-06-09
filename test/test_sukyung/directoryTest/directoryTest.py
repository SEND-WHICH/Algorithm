import os, re

directory = os.listdir('C:/Users/송수경/Documents/GitHub/Algorithm/test/test_sukyung/directoryTest/testFiles')
os.chdir('C:/Users/송수경/Documents/GitHub/Algorithm/test/test_sukyung/directoryTest/testFiles')

index = 1

for file in directory:
    open_file = open(file,'r', encoding='UTF-8')
    print(index, "번째 파일 open")
    read_file = open_file.read()
    regex = re.compile('시험')
    read_file = regex.sub('테스트', read_file)
    print(index, "번째 파일 탐지 후 수정")
    write_file = open(file,'w', encoding='UTF-8')
    write_file.write(read_file)
    print(index, "번째 파일 write")
    index += 1
