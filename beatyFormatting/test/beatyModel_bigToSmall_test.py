import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import beatyModel
import unittest
import color
import assertMy


class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = """
	def dataFile(self):
		return os.path.join (self.dataFolder, 'iterations.data')






	def currentFile(self):
		return os.path.join (self.dataFolder, 'current.data')
"""
		expected = """
	def dataFile(self):
		return os.path.join (self.dataFolder, 'iterations.data')


	def currentFile(self):
		return os.path.join (self.dataFolder, 'current.data')"""
		result = beatyModel.py(inputText)	
		color.red("inputText")
		print(repr(inputText))
		print(inputText)
		assertMy.stringDiffByLines(result, expected)




if __name__ == '__main__':
	unittest.main()		

		

