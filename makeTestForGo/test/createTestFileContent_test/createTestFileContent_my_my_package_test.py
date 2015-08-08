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
		packageName = "my"
		testMethodName = "Test_myTestMethod2"
		methodName = "myMethod"
		result = generateTestFileNameForGoTest.createTestFileContent(packageName, testMethodName, methodName)
		expected = """package my
import (
	"testing"
)

func Test_myTestMethod2(t *testing.T) {
    actual := myMethod()
    var expected interface{}
    expectedJson := ``
    FromJson(expectedJson, &expected)
    Test(actual, expected, t)
}"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()