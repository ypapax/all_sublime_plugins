
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../moveNearReplace'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import filer2 as filer
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
		filename = os.path.join(currentFolder, 'files/poligon')
		filer.write(filename, inputText)
		expected = """\tdef test_testName(self):
		color.blue("test here baby")
		intpuText = 
		beatyModel.py(inputText)


	def test_testName(self):
		color.blue("test here baby")
		intpuText = 
		beatyModel.py(inputText)
		"""
		beatyModel.pyFile(filename)	
		result = filer.read(filename)
		color.red("inputText")
		print(repr(inputText))
		print(inputText)
		assertMy.stringDiffByLines(result, expected)




if __name__ == '__main__':
	unittest.main()		

		

