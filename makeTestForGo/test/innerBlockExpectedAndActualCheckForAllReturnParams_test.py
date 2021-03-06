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
		inputArr=[{"var": "result1", "varType":"int"},
		{"var": "result2", "varType":"string"}]
		result = generateTestFileNameForGoTest.innerBlockExpectedAndActualCheckForAllReturnParams(inputArr)
		expected = """
	expectedJson_result1 := ``
	my.FromJson(expectedJson_result1, &result1_expected)
	my.Test(result1, result1_expected, t)
	expectedJson_result2 := ``
	my.FromJson(expectedJson_result2, &result2_expected)
	my.Test(result2, result2_expected, t)"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()