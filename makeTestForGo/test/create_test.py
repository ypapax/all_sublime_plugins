import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/makeTest')
import color
import assertMy
import generateTestFileNameForGoTest
import filer2

import os
class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		fileName = os.path.dirname(os.path.realpath(__file__)) + "/poligon/forGo/testable.go"
		methodName = "myMethod"
		fileContent  = filer2.read(fileName)
		
		expected = os.path.dirname(os.path.realpath(__file__)) + "/poligon/forGo/Test_myMethod_test.go"
		if os.path.isfile(expected):
			os.remove(expected)
		result = generateTestFileNameForGoTest.create(fileName, methodName, fileContent)

		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()