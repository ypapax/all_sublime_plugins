
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import pyFind
import unittest
import sys
import color




import navigateToModel
        

class Test(unittest.TestCase):
    def test_testName(self):
        color.blue("test here baby")
        currentFolder = os.path.dirname(os.path.realpath(__file__))
        filename1 = os.path.join(currentFolder, '../testPoligon/py/a.py')
        position1 = len("""import b_model

import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color



class Test(unittest.TestCase):
    
    def test_bigFile(self):
        color.blue("test here baby")
        

        expected = ['', 'startsLikeCodeNumber']
        


        result = b_model.getO""")
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('filename1: ', filename1, 'position1 = ', position1)
        result = navigateToModel.filenameAndPositionTransform(filename1, position1)

        expected = ('/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo/testPoligon/py/b_model.py', len("""import re
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
def """))
        print(result)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()     
