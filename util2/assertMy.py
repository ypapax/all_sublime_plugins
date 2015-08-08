import unittest

import sys
import color


import sys
import colorDiff

def isTuple(obj):
    return isinstance(obj, tuple)
def isArray(obj):
    return isinstance(obj, list)
def isString(obj):
    return isinstance(obj, basestring)

# works only for tuple of strings or tuple of arrays or mixed: tuple of strings and array
def objToStr(obj):
    if isTuple(obj):
        return tupleToString(obj)

def arrayOfAnythingToArrayOfStrings(arr):
    for index, elem in enumerate(arr):
        # unless isArray(i):
        if isArray(elem):
            elemStr =arrayToStr(elem)
        else:
            elemStr = StringToStr(elem)
        arr[index] = elemStr
        # pass
    return arr
def arrayToStr(arr):
    return "[{}]".format(", ".join(arrayOfAnythingToArrayOfStrings(arr)))
def StringToStr(string):
    return "\"{}\"".format(string)
def tupleToString(tup):
    arrCloneForTuple = list(tup)
    return "({})".format(", ".join(arrayOfAnythingToArrayOfStrings(arrCloneForTuple)))
def tupleBeatyPrint(tup):
    print(tupleToString(tup))

def beatyPrint(obj):
    if isTuple(obj):
        print(objToStr(obj))
    else:
        print(obj)

def stringDiffByLines(str1, str2):
    # color.warn('actual')
    # beatyPrint(str1)
    # color.warn('expected')
    # beatyPrint(str2)


    

    if  isinstance(str1, str):
        color.red('actual')
        color.green(str1)
        color.red('expected')
        color.warn(str2)
        colorDiff.do(str1, str2)

        assert str1.strip() == str2.strip(), "not equal"
    else:
        color.red('actual')
        print(str1)
        color.red('expected')
        print(str2)       
        assert str1 == str2, "not equal"

equals = stringDiffByLines    