import unittest
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '..'))
import color
import sys
import iterationsClass as ic
		

class Test(unittest.TestCase):
	def test_testName(self):
		i = ic.Iterations()
		inputFileNameLine1 = "/pathTo/file:55"
		inputFileNameLine2 = "/pathTo/file:55"
		i.clear()
		i.add(inputFileNameLine1)
		i.add(inputFileNameLine2)
		
		i.currentSet(inputFileNameLine1)
		i.next()

		result1 = i.remove(inputFileNameLine1)

		expected1 = inputFileNameLine2

		self.assertEqual(result1, expected1)
		
		result = i.all()
		
		expected = [inputFileNameLine2]
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()		
