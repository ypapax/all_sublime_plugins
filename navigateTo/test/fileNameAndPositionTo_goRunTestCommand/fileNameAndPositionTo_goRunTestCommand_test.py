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
		fileName="/Users/maks/Library/Application Support/Sublime Text 3/Packages/navigateTo/test/fileNameAndPositionTo_goRunTestCommand/poligon.go"
		pos = 285
		result = navigateToModel.fileNameAndPositionTo_goRunTestCommand(fileName, pos)
		expected = "go test -test.run Test_toJson"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()