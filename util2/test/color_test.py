import re

import sys
sys.path.insert(0, '..')
import color
		


import unittest
import sys
import color

class Test(unittest.TestCase):
	def test_testName(self):
		red = color.color("1", "red")
		green = color.color("2", "green")
		yellow = color.color("3", "yellow")
		print(red + green + yellow)
	def replaceLastAndFirstQuotes(string):
		re.sub('^\'|\'$', '', string)
	def test_testNameNextLine(self):
		red = color.color(repr("\n"), "red")
		green = color.color(repr("\t"), "green")
		
		print(red + green)
		

if __name__ == '__main__':
	unittest.main()		
		