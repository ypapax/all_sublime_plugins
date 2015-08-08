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
		result = generateTestFileNameForGoTest.getMethodNameByLineContentGo("func OneTwoFiftyTwoAnchors() (html template.HTML) {")
		expected = "OneTwoFiftyTwoAnchors"
		assertMy.equals(result, expected)

if __name__ == '__main__':
	unittest.main()