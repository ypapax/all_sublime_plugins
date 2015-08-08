import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest')
import color
import assertMy
import generateTestFileNameForGoTest

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		result = generateTestFileNameForGoTest.splitAndFullPrepare("int1 int, string2 *string")
		expected = ('\n\tint1 int\n\tstring2 *string', 'int1,string2', ['int1', 'string2'])
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()