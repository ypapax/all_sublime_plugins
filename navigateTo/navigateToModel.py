import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color
import os    
import pyFind

import re
# def getRel(linetext, fulltext):

import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import filer2 as filer

import sys
import absRel3 as absRel
                

def reverseStr(stra):
    return stra[::-1]
def stopChar(ch):
    stopChars = [' ', ',', '@', '(', '\n', '\t']
    return any(i for i in stopChars if i == ch)
def stopLine(ch):
    stopChars = ['\n']
    return any(i for i in stopChars if i == ch)    

def getLine(text, position):
    objectMethod = getSubstr(text, position, stopLine)    
    return objectMethod

def getSubstr(text, position, stopMethod):
    part_a = text[:position]
    print(part_a)
    print('part_a')
    rev_a = reverseStr(part_a)
    print("rev_a")
    print(rev_a)
    a = position
    for s in rev_a:
        if stopMethod(s):
            break
        a = a - 1 
    part_b = text[position:]    
    b = position
    for s in part_b:
        if stopMethod(s):
            break;
        b = b + 1

    result = text[a:b]     
    return result
def getObject(text, position):
    objectMethod = getSubstr(text, position, stopChar)    

    parts = objectMethod.split('.')
    if len(parts)==1:
        return ["", objectMethod]
    else:
        return parts

def getMethodNameGo(text, position):
    methodName = getSubstr(text, position, stopChar)    

    return methodName

def getCommandLineStringForGoTestThisMethod(methodName):
    return "go test -test.run {}".format(methodName)

def fileNameAndPositionTo_goRunTestCommand(fileName, position):
    fileText = filer.read(fileName)
    methodName=getMethodNameGo(fileText, position)

    dirName = os.path.dirname(fileName)
    command = "cd \"{}\"; TALK=1 {}".format( dirName, getCommandLineStringForGoTestThisMethod(methodName))

    return command







def findRequire(text, objectName):
    regex = "{} =.+'(.+)'".format(objectName)
    
    
    color.red('regex')
    print(repr(regex))
    
    result = re.findall(regex, text)
    if len(result):
        return result[0]
    else:
        return None


def getPositions(filename, regex):
    position2 = 0
    data2 = filer.read(filename)
    finditer = re.finditer(regex, data2)
    indexes = [m.start(0) for m in finditer]
    return indexes


def getPosition(filename2, regex):
    positions = getPositions(filename2, regex)
    if len(positions):
        return positions[0]
    else:
        return None
    # return getPosition(filename2, regex)[0]

def method(text, position):
    return getObject(text, position)[1].strip()    

def filenameAndPositionTransform(filename, position):
     
    ext = filename.split('.')[-1]    

    isPy = ext == 'py'
   
    text = filer.read(filename)
    
    filename2 = filename
    position2 = 0

    
    color.red('text')
    print(text)
    

    
    color.red('position')
    print(repr(position))
    


    [obj, method] = getObject(text, position)

    print('obj')
    print(repr(obj))
    

    print('method')
    print(repr(method))
    
    
    if isPy:
        filename2 = pyFind.filename2Total(filename, obj, method)
        print('filename2')
        print(repr(filename2))
        
        if method:
            regex = "def {0}\(|{0} =".format(method)
            
            color.red('regex')
            print(repr(regex))
            
            position2 = getPosition(filename2, regex) 
            if position2 > 0:
                position2 = position2 + len("def")
    else:
        if obj:
            
            color.red('text')
            print(text)
            

            
            color.red('obj')
            print(repr(obj))
            
            rel = findRequire(text, obj)
            
            color.red('rel')
            print(repr(rel))
            

            filename2 = absRel.AbsAddExtension(filename, rel)

        regex = method + ' = '
        position2 = getPosition(filename2, regex)




    
            
    return (filename2, position2)    
    
