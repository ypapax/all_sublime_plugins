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
		packageName = "myPackage"
		testMethodName = "Test_myTestMethod2"
		methodName = "myMethod"
		result = generateTestFileNameForGoTest.createTestFileContent(packageName, testMethodName, methodName)
		expected = """package myPackage
import (
	"my"
	"testing"
)

func Test_myTestMethod2(t *testing.T) {
    actual := myMethod()
    var expected interface{}
    expectedJson := ``
    my.FromJson(expectedJson, &expected)
    my.Test(actual, expected, t)
}"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()