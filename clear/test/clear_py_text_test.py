import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
sys.path.insert(0, os.path.join(currentFolder, '../../moveNearReplace'))
import clearModel as clear
import unittest
import color

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

		result = clear.py(inputText)

		color.red('result')
		print(result)
		expected = """if inlist:
			currentIndex = allList.index(current) #todo: make test to test when current item not in list
			chooseNumber =  currentIndex + 1
			if chooseNumber >= len(allList):"""
		color.red('expected')
		print(expected)
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()		
		