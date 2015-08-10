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
		# inputFileNameLine = "/pathTo/file:55"
		# iterations_model.clear()
		# iterations_model.add(inputFileNameLine)
		# result = iterations_model.all()
		# expected = [inputFileNameLine]
		# self.assertEqual(result, expected)
		
		iters = ic.Iterations()
		iters.testFolder()
		iters.testFolder()
		result = iters.dataFile()
		expected = os.path.abspath(os.path.join(currentFolder, '../testData/iterations.data'))
		self.assertEqual(result, expected)
		

if __name__ == '__main__':
	unittest.main()		
