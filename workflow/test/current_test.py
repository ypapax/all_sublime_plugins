import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import color
import iterationsClass as ic
			

class Test(unittest.TestCase):
	def test_testName(self):
		i = ic.Iterations()
		
		color.blue("test here baby")
		fileNamePath = "/pathTo/file:23"
		i.currentSet(fileNamePath)

		result = i.currentGet()

		expected = fileNamePath

		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()		
