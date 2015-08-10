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
		i.realFolder()
		color.blue("test here baby")
		result = i.dataFile() 
		expected = os.path.abspath(os.path.join(currentFolder, '../data/iterations.data'))
		self.assertEqual(result, expected)

		i.testFolder()
		result = i.dataFile() 
		expected = os.path.abspath(os.path.join(currentFolder, '../testData/iterations.data'))
		self.assertEqual(result, expected)		
		

if __name__ == '__main__':
	unittest.main()		
