import os, re

directory = os.listdir('C:/Users/송수경/Documents/GitHub/Algorithm/test/test_sukyung/overwriteTest')
os.chdir('C:/Users/송수경/Documents/GitHub/Algorithm/test/test_sukyung/overwriteTest')

for file in directory:
    open_file = open(file,'r', encoding='UTF-8')
    read_file = open_file.read()
    regex = re.compile('메롱')
    read_file = regex.sub('메롱', read_file)
    write_file = open(file,'w', encoding='UTF-8')
    write_file.write(read_file)
