import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest')
import color
import assertMy
import generateTestFileNameForGoTest
from hamcrest import *

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = generateTestFileNameForGoTest.splitArgs("par1 int, par2 string")
		expected = [{'var': 'par1', 'varType': 'int'}, {'var': 'par2', 'varType': 'string'}]
		
		# assert_that(result == expected)
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()