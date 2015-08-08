import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
sys.path.insert(0, os.path.join(currentFolder, '../clipToFile'))
import pyOutPutParse5 as pyOutPutParse
import color


class Test(unittest.TestCase):
	def test_testName(self):
		clip = """File "/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo/findRequire_test.py", line 17"""



		result = pyOutPutParse.parse(clip)
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		color.red('result')
		print(result)
		print('*****************************************************************')
		self.assertEqual(result, ['/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo/findRequire_test.py:17'])
	

if __name__ == '__main__':
	unittest.main()		
