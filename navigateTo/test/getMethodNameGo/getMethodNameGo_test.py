import unittest
import sys
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/util')
sys.path.insert(0, '/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo')
import color
import assertMy
import navigateToModel

class Test(unittest.TestCase):
	def test_testName(self):
		color.blue("test here baby")
		text = """// Sometimes we'll want to sort a collection by something
// other than its natural order. For example, suppose we
// wanted to sort strings by their length instead of
// alphabetically. Here's an example of custom sorts
// in Go.

package elit

import (
	"encoding/json"
)

func Test_toJson(t *testing.T) {

	actual := toJson(FotoList{
		{bigFoto: "1.jpg"},
		{bigFoto: "10.jpg"},
	})
	expected := ""
	my.Test(actual, expected, t)
}
"""		
		pos = 287
		result = navigateToModel.getMethodNameGo(text, pos)
		expected = "Test_toJson"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()