import os, re, shutil

#directory = os.listdir('C:/Users/송수경/Documents/GitHub/Algorithm/test/test_sukyung/overwriteTest')
#os.chdir('C:/Users/송수경/Documents/GitHub/Algorithm/test/test_sukyung/overwriteTest')

#for file in directory:





# 어떤 파일 열지 입력 (추후에 파일탐색기?)
FILE_PATH = input("검사할 파일명을 입력하세요: ")

# 복사
shutil.copy(FILE_PATH + '.txt', FILE_PATH + '(masked).txt')
            
#f = open(FILE_PATH+'.txt', 'r', encoding='UTF8')
#newf = open(FILE_PATH + '(masked).txt', 'r+', encoding='UTF8')

file = FILE_PATH + '(masked).txt'

while True:
    open_file = open(file,'r', encoding='UTF-8')
    read_file = open_file.read()
    regex = re.compile('메롱')
    read_file = regex.sub('메롱', read_file)
    write_file = open(file,'w', encoding='UTF-8')
    write_file.write(read_file)
