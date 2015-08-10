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
		
		firstValue = '/pathTo/file1:1'
		secondValue = '/pathTo/file2:2'
		lastValue = '/pathTo/file3:3'


		i.setAll([firstValue, secondValue, lastValue])
		i.currentSet(lastValue)
		
		
		i.prev()

		result = i.currentGet()

		expected = secondValue
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()		
