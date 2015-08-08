
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import pyFind
                

import sys
import navigateToModel
		


import unittest
import sys
import color

class Test(unittest.TestCase):
	def test_testName(self):
		
                importText = """ru = require '../regexUrls.iced'
                rf = require '../../grab/redisFunc.iced'
                app.get ru.short790, (req, res, next)->
                number = req.params[0]"""

                expected = '../regexUrls.iced'
                objectName = 'ru'
                actual = navigateToModel.findRequire(importText, objectName)
                self.assertEqual(actual, expected)		

if __name__ == '__main__':
	unittest.main()		
