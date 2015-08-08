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
		result = generateTestFileNameForGoTest.convertStructureListToExpected([{"var": "var1", "varType": "int"}, {"var": "var2", "varType": "string"}])
		expected = [{'varType': 'int', 'var': 'var1_expected'}, {'varType': 'string', 'var': 'var2_expected'}]
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()