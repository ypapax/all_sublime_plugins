import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import iterationsClass as ic
import unittest
import color

class Test(unittest.TestCase):
	def test_testName(self):
		i = ic.Iterations()
		i.testFolder()
		inputFileNameLine = "/pathTo/file:55"
		i.clear()
		i.add(inputFileNameLine)
		result = i.all()
		expected = [inputFileNameLine]
		self.assertEqual(result, expected)
		

if __name__ == '__main__':
	unittest.main()		
