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
		(packageName, testMethodName, caller, method, args, returnParams) = ("ordb", "TestRubricById", "org *Org", "GetRubricById", "orgId string, someBool bool", "orgResult *Org, ok bool")
		result = generateTestFileNameForGoTest.generateTestTextByGoFuncDeclarationParts(packageName, testMethodName, caller, method, args, returnParams)
		expected = """package ordb
import (
    "my"
	"testing"
)

func TestRubricById(t *testing.T) {
    var (
	org *Org

	orgId string
	someBool bool

	orgResult *Org
	ok bool

	orgResult_expected *Org
	ok_expected bool
        )
    orgResult,ok = org.GetRubricById(orgId,someBool)
    
	expectedJson_orgResult := ``
	my.FromJson(expectedJson_orgResult, &orgResult_expected)
	my.Test(orgResult, orgResult_expected, t)
	expectedJson_ok := ``
	my.FromJson(expectedJson_ok, &ok_expected)
	my.Test(ok, ok_expected, t)
}"""
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()