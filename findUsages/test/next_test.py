import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
from findUsagesModel import FindUsagesModel

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		findUsagesModel = FindUsagesModel(os.path.join(currentFolder, 'dataPoligon/'))
		findUsagesModel.i.currentSet(('/path/to/first.py', 1))
		result = findUsagesModel.next()

		color.red('result')
		print(repr(result))
		expected = ('/path/to/second.py', 2, '2 of 3')
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()