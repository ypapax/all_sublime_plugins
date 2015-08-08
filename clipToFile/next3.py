
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')

import color
import util    

def next(fileNameList, fileNameWithLine):
    return get(fileNameList, fileNameWithLine, "next")

def prev(fileNameList, fileNameWithLine):
    return get(fileNameList, fileNameWithLine, "prev")


def get(fileNameList, fileNameWithLine, move):
    fileNameList = util.uniqueList(fileNameList)
    result = ""
    contains = any(fileNameWithLine in i for i in fileNameList)
    if (contains):
        index = fileNameList.index(fileNameWithLine)
        if (move=="prev"):
            index = index - 1
            if (index < 0):
                index = len(fileNameList)-1
        elif(move=="next"):    
            index = index + 1
            if (index >= len(fileNameList)):
                index = 0
        else:
            index = -1            

        result = fileNameList[index]
    else:
        (fileName, line) = fileNameWithLine.split(':')
   
        contains = any(fileName in i for i in fileNameList)
        if contains:
            result = [i for i in fileNameList if util.startsWith(i, fileName)][0]
        elif(len(fileNameList)):
            result = fileNameList[-1]
    

    return result