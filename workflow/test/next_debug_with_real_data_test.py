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
		
		secondValue = '/Users/maks/Library/Application Support/Sublime Text 3/Packages/Default/Default (OSX).sublime-commands:6'

		i.setAll(['/Users/maks/Library/Application Support/Sublime Text 3/Packages/workflow/iterations.py:8', secondValue, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/Default/Default (OSX).sublime-commands:1'])
		i.currentSet('/Users/maks/Library/Application Support/Sublime Text 3/Packages/workflow/iterations.py:8')
		
		
		i.next()

		result = i.currentGet()

		expected = secondValue
		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()		
