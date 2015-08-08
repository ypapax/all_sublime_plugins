
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import pyFind
import unittest
import color

import navigateToModel

class Test(unittest.TestCase):
    
        

    
        #  35
    def test_getObjectDebug(self):
        color.blue("test here baby")
        

        expected = ['rf', 'sgetSorted']
        linetext = 'await rf.sgetSorted "sqlRegions", defer sqlRegions'
        position = len('await rf.sgetSor')
        actual = navigateToModel.getObject(linetext, position)
        self.assertEqual(actual, expected)    
    def test_getObject(self):
        color.blue("test here baby")
        

        expected = ['ru', 'short790']
        linetext = 'app.get ru.short790, (req, res, next)->'
        position = len('app.get ru.short79')
        actual = navigateToModel.getObject(linetext, position)
        self.assertEqual(actual, expected)
    def test_reverseStr(self):
        inp = '12345'
        expected = '54321'
        actual = navigateToModel.reverseStr(inp)
        self.assertEqual(actual, expected)
    # def test_lineAndTextToRelative(self):
    #     importText = """ru = require '../regexUrls.iced'
    #     rf = require '../../grab/redisFunc.iced'
    #     app.get ru.short790, (req, res, next)->
    #     number = req.params[0]"""
    #     linetext = 'app.get ru.short790, (req, res, next)->'
    #     position = len('app.get ru.short79')
    #     expected = ('../regexUrls.iced', 'short790')
    #     actual = navigateToModel.lineAndTextToRelative(linetext, importText, position)
    #     self.assertEqual(actual, expected)    


if __name__ == '__main__':
    unittest.main()     
