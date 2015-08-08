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
		fileContent = """// Sometimes we'll want to sort a collection by something
// other than its natural order. For example, suppose we
// wanted to sort strings by their length instead of
// alphabetically. Here's an example of custom sorts
// in Go.

package my

import (
	"reflect"
	"testing"

	"myColors"
)

func Test(actual interface{}, expected interface{}, t *testing.T) {
	myColors.P("actual")
	myColors.P(actual)
	myColors.P("expected")
	myColors.P(expected)
	eq := reflect.DeepEqual(actual, expected)
	if !eq {
		t.Errorf("not equal")
	}
}
"""
		result = generateTestFileNameForGoTest.getPackageName(fileContent)
		expected = "my"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()