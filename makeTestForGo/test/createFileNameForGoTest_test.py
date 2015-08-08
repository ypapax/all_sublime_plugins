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
		testFolder = "/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest/test/poligon"
		methodName = "myMethod"
		result = generateTestFileNameForGoTest.createFileNameForGoTest(testFolder, methodName)
		expected = ("/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest/test/poligon/myMethod_test.go", 0)
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()