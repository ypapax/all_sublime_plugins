import unittest
import sys
import color
import assertMy
import generateTestFileNameFromMethodName

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		methodName = "myMethod"
		result = generateTestFileNameFromMethodName.createFileNameWithoutFolderAndExt(methodName)
		expected = ""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()