import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
	

import unittest
import sys
import color
import assertMy
from findUsagesModel import FindUsagesModel

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		filename = os.path.abspath(os.path.join(currentFolder, '../../util/filer2.py'))
		position = 131
		findUsagesModel = FindUsagesModel(os.path.join(currentFolder, 'dataPoligon2/'))
		result = findUsagesModel.command("find", filename, position)
		color.red('result')
		print(repr(result))
		expectedFileName = os.path.join(currentFolder, '../../moveNearReplace/replace_require_test.py')
		expected = (expectedFileName, 1194, "2 of 2")
		self.assertEquals(result, expected)

if __name__ == '__main__':
	unittest.main()