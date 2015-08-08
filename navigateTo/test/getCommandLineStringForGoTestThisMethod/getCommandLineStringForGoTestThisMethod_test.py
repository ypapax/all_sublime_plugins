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
		methodName = "myMethodName"
		result = navigateToModel.getCommandLineStringForGoTestThisMethod(methodName)
		expected = "go test -test.run myMethodName"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()