import os

def findFilesInFolder(path, pathList, extension, subFolders = True):
    """ Recursive function to find all files of an extention type in a folder (and optionally in all subfolders too)

    path:       Base directory to find files
    pathList:   A list that stores all paths
    extention:  File extension to find
    subFolders: Bool. If True, find files in all subfolders under path. If False, only searches files in the specified folder
    """
    
    try: # Trapping a OSError: File permissions problem I believe
        for entry in os.scandir(path):
            if entry.is_file() and entry.path.endswith(extension):
                pathList.append(entry.path)
            elif entry.is_dir() and subFolders:     # if its a directory, then repeat process as a nested function
                pathList = findFilesInFolder(entry.path, pathList, extension, subFolders)
    except OSError:
        print('Cannot access ' + path + '. Probably a permissions error')

    return pathList

dir_name = r'C:/Users/송수경/Documents/GitHub/Algorithm/test/files'
extention = ".txt"

pathList = []
pathList = findFilesInFolder(dir_name, pathList, extention, True)



'''
import os, re, glob


# 검사할 디렉토리
#directory = os.listdir('C:/Users/송수경/Documents/GitHub/Algorithm/test/files')
#os.chdir('C:/Users/송수경/Documents/GitHub/Algorithm/test/files')

directory = os.listdir('C:/Users/송수경/Documents/GitHub/Algorithm/test/files')
#텍스트 파일 검사
txtFile = glob.glob('C:/Users/송수경/Documents/GitHub/Algorithm/test/files/*.txt')


for file in directory:
    if txtFile:
        open_file = open(file,'r', encoding='UTF-8')
        read_file = open_file.read()
        regex = re.compile('ss')
        read_file = regex.sub('sk', read_file)
        write_file = open(file,'w', encoding='UTF-8')
        write_file.write(read_file)
        '''

