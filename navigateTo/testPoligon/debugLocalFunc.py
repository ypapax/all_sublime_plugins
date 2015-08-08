import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color
    
import pyFind

import re
# def getRel(linetext, fulltext):

import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
import filer2 as filer

import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/moveNearReplace')
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
    rev_a = reverseStr(part_a)
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


def findRequire(text, objectName):
    regex = "{} =.+'(.+)'".format(objectName)
    
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    color.red('regex')
    print(repr(regex))
    print('*****************************************************************')
    result = re.findall(regex, text)
    if len(result):
        return result[0]
    else:
        return None


def getPosition(filename2, regex):
    
    position2 = 0
    data2 = filer.read(filename2)
    finditer = re.finditer(regex, data2)
    indexes = [m.start(0) for m in finditer]
    if len(indexes):
        position2 = indexes[0]
    return position2        

def method(text, position):
    return getObject(text, position)[1].strip()    

def filenameAndPositionTransform(filename, position):
     
    ext = filename.split('.')[-1]    

    isPy = ext == 'py'
   
    text = filer.read(filename)
    
    filename2 = filename
    position2 = 0

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    color.red('text')
    print(text)
    print('*****************************************************************')

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    color.red('position')
    print(repr(position))
    print('*****************************************************************')


    [obj, method] = getObject(text, position)

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    color.red('obj')
    print(repr(obj))
    print('*****************************************************************')

    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    color.red('method')
    print(repr(method))
    print('*****************************************************************')
    
    if isPy:
        filename2 = pyFind.filename2(filename, obj)
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        color.red('filename2')
        print(repr(filename2))
        print('*****************************************************************')
        if method:
            regex = "def {0}\(|{0} =".format(method)
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            color.red('regex')
            print(repr(regex))
            print('*****************************************************************')
            position2 = getPosition(filename2, regex) 
            if position2 > 0:
                position2 = position2 + len("def")
    else:
        if obj:
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            color.red('text')
            print(text)
            print('*****************************************************************')

            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            color.red('obj')
            print(repr(obj))
            print('*****************************************************************')
            rel = findRequire(text, obj)
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            color.red('rel')
            print(repr(rel))
            print('*****************************************************************')

            filename2 = absRel.AbsAddExtension(filename, rel)

        regex = method + ' = '
        position2 = getPosition(filename2, regex)




    
            
    return (filename2, position2)    
    
