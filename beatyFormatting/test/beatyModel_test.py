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
	def test_testName(self):
		color.blue("test here baby")
		intpuText = 
		beatyModel.py(inputText)	
	def test_testName(self):
		color.blue("test here baby")
		intpuText = 
		beatyModel.py(inputText)"""
		expected = """\tdef test_testName(self):\n\t\tcolor.blue("test here baby")\n\t\tintpuText = \n\t\tbeatyModel.py(inputText)\n\n\n\tdef test_testName(self):\n\t\tcolor.blue("test here baby")\n\t\tintpuText = \n\t\tbeatyModel.py(inputText)"""
		result = beatyModel.py(inputText)	
		color.red("inputText")
		print(repr(inputText))
		print(inputText)
		assertMy.stringDiffByLines(result, expected)




if __name__ == '__main__':
	unittest.main()		

		

