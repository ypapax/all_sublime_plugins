import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '..'))
sys.path.insert(0, os.path.join(currentFolder, '../../util'))
import clearModel as clear
import unittest
import color

class Test(unittest.TestCase):
	def test_testName(self):
		inputText = """hellow\n\nworld"""

		result = clear.py(inputText)
		expected = """hellow\nworld"""	
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()		
		