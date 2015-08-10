import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import color
import assertMy
import filerCodecs

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		fileName = os.path.join(currentFolder, '../poligon/file.data')
		result = filerCodecs.read(fileName)
		print('result')
		print(repr(result))
		# expected = ""
		# assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()