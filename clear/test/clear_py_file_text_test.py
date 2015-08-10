import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '../../moveNearReplace'))
import clearModel as clear
import unittest
import color
import filer2 as filer


class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		inputText = """if inlist:
			print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
			color.red('inlist')
			print(inlist)
			print('*****************************************************************')
			currentIndex = allList.index(current) #todo: make test to test when current item not in list
			chooseNumber =  currentIndex + 1
			if chooseNumber >= len(allList):"""
		filename = os.path.join(currentFolder, 'files/printColor.poligon')

		filer.write(filename, inputText)

		clear.pyFile(filename)
		result = filer.read(filename)
		
		expected = """if inlist:
			currentIndex = allList.index(current) #todo: make test to test when current item not in list
			chooseNumber =  currentIndex + 1
			if chooseNumber >= len(allList):"""
		print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
		color.red('expected')
		print(expected)
		print('*****************************************************************')	
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()		
		