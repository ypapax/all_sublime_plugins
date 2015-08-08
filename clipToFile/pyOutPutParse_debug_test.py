


import unittest
import pyOutPutParse5 as pyOutPutParse

import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
import color


class Test(unittest.TestCase):
	def test_testName(self):
		clip = """  File "/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo/findRequire_test.py", line 17"""



		result = pyOutPutParse.parse(clip)
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		color.red('result')
		print(result)
		print('*****************************************************************')
		
	

if __name__ == '__main__':
	unittest.main()		
