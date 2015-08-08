import re
# def getRel(linetext, fulltext):

def reverseStr(stra):
    return stra[::-1]
def stopChar(ch):
    stopChars = [' ', ',', '@']
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
    print('text')
    print(text)
    print ('regex = ', regex)

    result = re.findall(regex, text)

    print('result = ', result)
    result = result[0]
    return result

# def textAndPositionToRelative(text, position):
    
#     [obj, method] = getObject(text, position)
#     rel = findRequire(text, obj)
#     return (rel, method)

def filenameAndPositionTransform(filename, position):
      # # 
        # 
        #     getAbsPathAndTextToSearch = navigateToModel.py
        # else:    
        #     getAbsPathAndTextToSearch = navigateToModel.textAndPositionToAbsAndSearchForText
        # print('filename = ', filename)
    ext = filename.split('.')[-1]    
    methodToGetObjAndMethod = getPy if ext is 'py' else "getObject" 
    
    

    [obj, method] = methodToGetObjAndMethod(text, position)
    if obj:
        rel = findRequire(text, obj)
    else:
        rel = ''
    
            
    return (rel, method)    
    
# def py(text, position):